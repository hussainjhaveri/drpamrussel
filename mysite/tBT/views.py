from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
# from django.contrib.messages.views import SuccessMessageMixin
# from django.views.generic.edit import CreateView 
# from tBT.models import Form

from .forms import Form1

# class FormCreate(SuccessMessageMixin, CreateView):
#     model = Form
#     success_url = '/success/'
#     success_message = "%(name)s was created successfully"

class Index(View):
    def get(self, request):
        form = Form1()
        context = {'form': form}
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        form = Form1(request.POST)
        if form.is_valid():
            
            messages.success(self.request, 'Form submission successful')
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            
            email = EmailMessage(
                subject= str(subject),
                body='Name: ' + str(name) + '\n'
                     + 'message: ' + str(message) + '\n'
                     + 'email: ' + str(email) + '\n'
                     + 'phonenumber: ' + str(phone) + '\n'

                ,
                from_email='aidanfire360@gmail.com',
                to=['aidanfire360@gmail.com']

            )
            email.send()
            
            return redirect(reverse('tBT:index'))
        else:
            return redirect(reverse('tBT:index'))

def services(request):
    return render(request, 'services.html')

class contactUs(View):
    def get(self, request):
        form = Form1()
        context = {'form': form}
        return render(request, 'contactUs.html', context)

    def post(self, request, *args, **kwargs):
        form = Form1(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(self.request, 'Form submission successful')
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            
            email = EmailMessage(
                subject= str(subject),
                body='Name: ' + str(name) + '\n'
                     + 'message: ' + str(message) + '\n'
                     + 'email: ' + str(email) + '\n'
                     + 'phonenumber: ' + str(phone) + '\n'

                ,
                from_email='aidanfire360@gmail.com',
                to=['aidanfire360@gmail.com']

            )
            email.send()
            
            return redirect(reverse('tBT:contactUs'))
        else:
            return redirect(reverse('tBT:contactUs'))


def about(request):
    return render(request, 'about.html')

def ugh(request):
    return render(request, 'ugh.html')

def assessments(request):
    return render(request, 'assessments.html')