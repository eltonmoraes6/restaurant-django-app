from django.contrib.admin import site
from django.template.response import TemplateResponse
from django.urls import path


def cms_environment(request):
    context = {
        "sections": [
            ("Homepage", "/admin/Base_App/pagesection/?page=home"),
            ("About Page", "/admin/Base_App/pagesection/?page=about"),
            ("Menu Page", "/admin/Base_App/pagesection/?page=menu"),
            ("Footer", "/admin/Base_App/pagesection/?page=footer"),
            ("Products", "/admin/Base_App/items/"),
            ("Categories", "/admin/Base_App/itemlist/"),
             ("Adicionar Categoria", "/admin/Base_App/itemlist/add/"),
        ]
    }
    return TemplateResponse(request, "admin/cms_environment.html", context)

def register_cms_admin_page():
    site.get_urls = get_urls(site.get_urls)

def get_urls(original_urls):
    def urls():
        custom = [
            path("cms-environment/", site.admin_view(cms_environment), name="cms_environment")
        ]
        return custom + original_urls()
    return urls
