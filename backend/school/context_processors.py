from .models import Material


def materials(request):
    """Daftar materi aktif untuk dropdown 'Imogi School' di semua halaman."""
    return {"school_materials": Material.objects.filter(is_active=True)}
