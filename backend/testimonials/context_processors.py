from .models import Testimonial


def testimonials(request):
    """Testimoni aktif untuk section 'Testimoni' di beranda."""
    return {"testimonials": Testimonial.objects.filter(is_active=True)}
