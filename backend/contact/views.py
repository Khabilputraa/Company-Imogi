from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .forms import ContactForm


@require_POST
def submit(request):
    """Handle the contact form. Returns plain 'OK' so the template's
    AJAX validator (php-email-form) shows the success message."""
    # Honeypot: bots fill the hidden 'website' field; humans never do.
    # Pretend success (so bots don't retry) but skip saving/emailing.
    if request.POST.get("website"):
        return HttpResponse("OK")

    form = ContactForm(request.POST)
    if not form.is_valid():
        first_error = next(iter(form.errors.values()))[0]
        return HttpResponse(first_error, status=400)

    message = form.save()

    send_mail(
        subject=f"[Website Imogi] Pesan baru: {message.subject or 'Tanpa subjek'}",
        message=(
            f"Nama       : {message.name}\n"
            f"Perusahaan : {message.company or '-'}\n"
            f"Email      : {message.email}\n"
            f"Subjek     : {message.subject or '-'}\n\n"
            f"{message.message}\n"
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
        fail_silently=True,
    )
    return HttpResponse("OK")
