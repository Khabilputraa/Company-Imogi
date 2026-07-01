from .models import Product


def products(request):
    """Daftar produk aktif, tersedia di semua template (navbar & beranda)."""
    return {"products": Product.objects.filter(is_active=True)}
