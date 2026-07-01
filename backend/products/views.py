from django.shortcuts import get_object_or_404, render

from .models import Product


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    other_products = (Product.objects.filter(is_active=True)
                      .exclude(pk=product.pk)[:3])
    return render(request, "products/detail.html", {
        "product": product,
        "other_products": other_products,
    })
