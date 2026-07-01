from .models import Client


def clients(request):
    """Daftar klien aktif untuk carousel 'Klien Kami' di beranda."""
    return {"clients": Client.objects.filter(is_active=True)}
