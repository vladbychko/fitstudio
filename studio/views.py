from django.shortcuts import render, redirect
from .models import Trainer
from .forms import BookingForm
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.translation import gettext as _


def home(request):
    trainers = Trainer.objects.filter(is_active=True)[:3]
    return render(request, 'studio/index.html', {'trainers': trainers})


def about(request):
    return render(request, 'studio/about.html')


def programs(request):
    return render(request, 'studio/programs.html')


def trainers(request):
    trainer_list = Trainer.objects.filter(is_active=True)
    return render(request, 'studio/trainers.html', {'trainers': trainer_list})


def prices(request):
    return render(request, 'studio/prices.html')


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                _("Нова заявка"),
                f"{cd['name']}\n{cd['phone']}\n{cd['goal']}\n{cd['message']}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_FORM_RECIPIENT]
            )
            return redirect(reverse('booking') + "?success=1")
    else:
        form = BookingForm()

    return render(request, 'studio/booking.html', {
        'form': form,
        'success': request.GET.get("success") == "1"
    })
