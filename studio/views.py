from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext as _

from .models import Trainer
from .forms import BookingForm


def home(request):
    # можна вивести 3 тренери на головній
    trainers = Trainer.objects.filter(is_active=True)[:3]
    return render(request, 'studio/index.html', {'trainers': trainers})


def trainers(request):
    trainers = Trainer.objects.filter(is_active=True)
    return render(request, 'studio/trainers.html', {'trainers': trainers})


def prices(request):
    return render(request, 'studio/prices.html')


def programs(request):
    return render(request, 'studio/programs.html')


def about(request):
    return render(request, 'studio/about.html')


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = _("Нова заявка з сайту FIT STUDIO")
            body = (
                f"{_('Ім’я')}: {cd['name']}\n"
                f"{_('Телефон')}: {cd['phone']}\n"
                f"{_('Ціль')}: {cd['goal']}\n"
                f"{_('Коментар')}: {cd['message']}\n"
            )
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_FORM_RECIPIENT],
            )
            return redirect(reverse('booking') + '?success=1')
    else:
        form = BookingForm()

    success = request.GET.get('success') == '1'

    return render(request, 'studio/booking.html', {
        'form': form,
        'success': success,
    })
