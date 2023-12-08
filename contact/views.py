from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'New message from Jacinto.com'
            message = f'Name: {form.cleaned_data["name"]}\nEmail: {form.cleaned_data["email"]}\n\nNote:\n{form.cleaned_data["note"]}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [settings.CONTACT_EMAIL]
            print('contacted user is this -------->', settings.CONTACT_EMAIL)
            # sending
            send_mail(subject, message, from_email, recipient_list)
            return redirect('thank_you')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})


def thank_you_page(request):
    return render(request, 'thank_you.html', {})
