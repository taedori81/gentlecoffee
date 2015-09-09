from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

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

    @property
    def cafes(self):
        cafe_pages = CafePage.objects.all()
        return cafe_pages

    def get_context(self, request, *args, **kwargs):
        cafes = self.cafes

        # Update template context
        context = super(CafesPage, self).get_context(request)
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

    def serve(self, request, *args, **kwargs):
        products = Product.objects.get_available_products()[:12]
        products = products.prefetch_related('categories', 'images',
                                         'variants__stock')
        return render(
            request, self.template,
            {
                'self': self,
                'products': products,
                'parent': None
            })


