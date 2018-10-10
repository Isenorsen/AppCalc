from django.http import HttpResponse
from django.shortcuts import render
from . models import PartOfApp
from django.core.mail import send_mail
# Create your views here.

def PartsView(request):
    parts = PartOfApp.objects.all()
    context = {'parts': parts}
    return render(request, 'index.html', context)

from django.core.mail import send_mail, BadHeaderError, EmailMessage, send_mass_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subjectt']
            emailto = form.cleaned_data['emailto']
            from_email = 'ak@arcanite.ru'
            message = form.cleaned_data['message']
            try:
                message = "From: {email} \nMessage: {mesg}".format(email=str(emailto), mesg=str(message))
                subject2 = "Thanks for your feedback"
                message2 = "Our manager will contact you from 1 to 2 working days."
                send_mail(subject, message, from_email, ['ak@arcanite.ru'])
                send_mail(subject2, message2, from_email, [emailto])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return HttpResponse(request, {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message')