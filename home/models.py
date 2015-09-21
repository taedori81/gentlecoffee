from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db import models
from django.shortcuts import render
from django.utils import timezone

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailcore.url_routing import RouteResult
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailsearch import index
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks

from saleor.product.models import Product


class HomePage(Page):
    subtitle = models.CharField(max_length=50, blank=False,
                                default='Shop')
    description = models.CharField(max_length=255, blank=False,
                                   default='Get our favorite coffees, brewing equipment, merchandise, accessories, and more.')

    def serve(self, request, *args, **kwargs):
        products = Product.objects.get_available_products()[:4]
        products = products.prefetch_related('categories', 'images',
                                         'variants__stock')
        return render(
            request, self.template,
            {
                'self': self,
                'products': products,
                'parent': None
            })

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname='full title'),
        FieldPanel('description', classname='full'),
    ]


@register_snippet
class Area(models.Model):
    area_name = models.CharField(max_length=50)

    panels = [
        FieldPanel('area_name'),
    ]

    def __str__(self):
        return self.area_name


class CafesPage(Page):
    header = models.CharField(max_length=255, blank=False,
                              default='Find your Gentle Coffee Cafes')

    subpage_types = ['home.CafePage']

    @property
    def cafes(self):
        # Get the list of CafePage that are descendants of this page
        cafe_pages = CafePage.objects.live().descendant_of(self)

        # Order by Area name
        cafe_pages = cafe_pages.order_by('area')

        return cafe_pages
    
    def get_context(self, request, *args, **kwargs):
        # Get the list of cafe pages
        cafes = self.cafes
        filtered_cafes = None

        area = request.GET.get('area')
        if area:
            filtered_cafes = cafes.filter(area__area_name=area)

        # Search query
        search_query = request.GET.get('search', None)

        search_results = None

        if search_query:
            search_results = CafePage.objects.live().search(search_query)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(cafes, 10)  # Show 2 cafe page per page
        try:
            cafes = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            cafes = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results
            cafes = paginator.page(paginator.num_pages)

        # Update template context
        context = super(CafesPage, self).get_context(request)
        context['filtered_cafes'] = filtered_cafes
        context['search_results'] = search_results
        context['cafes'] = cafes
        return context

    content_panels = Page.content_panels + [
        FieldPanel('header', classname='full title'),
    ]


class CafePage(Page):
    cafe_name = models.CharField(max_length=100, blank=False,
                                 default='Location Name')

    cafe_logo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    cafe_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    area = models.ForeignKey(
        'home.Area',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    cafe_description = RichTextField()
    cafe_address_line_1 = models.CharField(max_length=100)
    cafe_address_line_2 = models.CharField(max_length=100)

    search_fields = Page.search_fields + (
        index.SearchField('cafe_address_line_2'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('cafe_name', classname='full title'),
        ImageChooserPanel('cafe_logo_image'),
        ImageChooserPanel('cafe_image'),
        FieldPanel('cafe_description', classname='full title'),
        SnippetChooserPanel('area', Area),
        FieldPanel('cafe_address_line_1'),
        FieldPanel('cafe_address_line_2'),
    ]


class ShopPage(Page):

    subpage_types = ['CoffeePage', 'BrewingPage', 'MerchandisePage']

    def serve(self, request, *args, **kwargs):

        products = Product.objects.get_available_products().filter(categories__name='Coffee')[:12]
        products = products.prefetch_related('categories', 'images',
                                             'variants__stock')

        return render(
            request, self.template,
            {
                'self': self,
                'products': products,
                'parent': None
            })


class CoffeePage(Page):
    pass


class BrewingPage(Page):
    pass


class MerchandisePage(Page):
    pass


class SubscribePage(Page):
    pass


class LearnPage(Page):
    subpage_types = ['home.BlogIndexPage', 'home.EventIndexPage', 'home.BrewGuidePage',
                     'home.OurStoryPage', 'home.FaqPage']


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    subpage_types = ['home.BlogPage']

    @property
    def blogs(self):
        blogs = BlogPage.objects.live().descendant_of(self)
        blogs = blogs.order_by('-date')

        return blogs

    def get_context(self, request, *args, **kwargs):
        blogs = self.blogs

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(blogs, 10)

        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        # Update template context
        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs
        return context

    content_panels = Page.content_panels + [
        FieldPanel('title', classname='full title'),
        FieldPanel('intro', classname='full'),
    ]


class BlogPage(Page):
    author = models.CharField(max_length=255, default='Gentle Coffee')
    date = models.DateField('Post Date', blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('photo', ImageChooserBlock(template='home/blocks/blog_photo.html')),

    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]


class EventIndexPage(Page):
    pass


class EventPage(Page):
    pass


class BrewGuidePage(Page):
    pass


class OurStoryPage(Page):
    pass


class FaqPage(Page):
    pass