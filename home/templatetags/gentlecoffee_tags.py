from django import template
from ..models import Area

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    return context['request'].site.root_page


@register.inclusion_tag("home/navbar/navbar.html", takes_context=True)
def display_navbar(context):
    parent = get_site_root(context)
    if context.has_key('self'):
        calling_page = context['self']
    else:
        calling_page = None

    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = menuitem.get_children().live().in_menu().exists()
        menuitem.active = (calling_page.url.startswith(menuitem.url) if calling_page else False)

    return {
        "calling_page": calling_page,
        "menuitems": menuitems,
        "request": context['request']
    }


@register.inclusion_tag('home/navbar/navbar_dropdown.html', takes_context=True)
def display_navbar_dropdown(context, parent):
    menuitems_children = parent.get_children().live().in_menu()

    return {
        "parent": parent,
        "menuitems_children": menuitems_children,
        "request": context['request'],
    }


@register.inclusion_tag('home/include/side_menu_area.html', takes_context=True)
def display_side_menu_area(context):
    request = context['request']
    areas = Area.objects.all()

    # TODO Need to build href for filter the page
    area_items = []
    for area in areas:
        item_name = area.area_name
        item_href = '?area=' + item_name
        area_items.append({"name": item_name, "href": item_href})

    return {
        "request": request,
        "areas": areas,
        "area_items": area_items
    }


@register.filter
def url_param_dict_to_list(url_items_dict):
    """Turn this dictionary into a param list for the URL"""
    params_list = ""
    for key,value in url_items_dict:
        if key != "page":
            params_list += "&%s=%s" % (key, value)

    return params_list


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.inclusion_tag('home/include/blog_item.html', takes_context=True)
def display_blog_list(context, blog_list):

    blogs = []

    for blog in blog_list:
        for block in blog.body:
            if block.block_type == 'heading':
                blog.heading = block.value
            if block.block_type == 'photo':
                blog.photo = block.value
        blogs.append(blog)
    request = context['request']
    return {
        "request": request,
        "blogs": blogs,
    }
