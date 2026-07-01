"""URL configuration for the imogi project."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Static marketing pages (rendered from the frontend HTML as templates)
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("service-details/",
         TemplateView.as_view(template_name="service-details.html"),
         name="service_details"),

    # Dynamic blog & product pages
    path("blog/", include("blog.urls")),
    path("produk/", include("products.urls")),

    # Form endpoints
    path("contact/", include("contact.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
