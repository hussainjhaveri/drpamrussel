from urllib import request

from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .forms import Form1


class Index(View):
    def get(self, request):
        # form = Form1()
        # context = {'form': form}
        return render(request, 'index.html')

    # def post(self, request, *args, **kwargs):
    #     form = Form1(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         name = form.cleaned_data['name']
    #         phone = form.cleaned_data['phone']
    #         message = form.cleaned_data['message']
    #         email = form.cleaned_data['email']
    #         company = form.cleaned_data['company']
    #         manager = form.cleaned_data['manager']
    #         budget = form.cleaned_data['budget']

    #         email = EmailMessage(
    #             subject='Inquiry from ' + str(email),
    #             body='Name: ' + str(name) + '\n'
    #                  + 'message: ' + str(message) + '\n'
    #                  + 'email: ' + str(email) + '\n'
    #                  + 'phonenumber: ' + str(phone) + '\n'
    #                  + 'company: ' + str(company) + '\n'
    #                  + 'manager: ' + str(manager) + '\n'
    #                  + 'budget: ' + str(budget) + '\n'

    #             ,
    #             from_email='jhaverihussain@gmail.com',
    #             to=['jhaverihussain@gmail.com']

    #         )
    #         email.send()

    #         return redirect(reverse('Tedx:index'))
    #     else:
    #         return redirect(reverse('Tedx:index'))


def services(request):
    return render(request, 'services.html')


# def contactUs(request):
#     return render(request, 'contactUs.html')

class contactUs(View):
    def get(self, request):
        form = Form1()
        context = {'form': form}
        return render(request, 'contactUs.html', context)

    def post(self, request, *args, **kwargs):

        form = Form1(request.POST)  # this line loads the post data
        if form.is_valid():  # form validation
            form.save()  # saves form data in database
            name = form.cleaned_data['name']  # lines 70 - 72 turn form data into variables
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            email = EmailMessage(
                subject='HoneyBeeElectric Inquiry from ' + str(email),  # collects data into email body
                body='Name: ' + str(name) + '\n'
                     + 'message: ' + str(message) + '\n'
                     + 'email: ' + str(email) + '\n'

                ,
                from_email='aidanfire360@gmail.com',  # i find this rarely matters
                to=['aidanfire360@gmail.com']  # this on the other hand very important

            )
            email.send()  # actually send email

            return render(request, 'contactUs.html')
        else:
            return render(request, 'contactUs.html')


def about(request):
    return render(request, 'about.html')


def ugh(request):
    return render(request, 'ugh.html')
