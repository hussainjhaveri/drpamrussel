from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .forms import Form1


class Index(View):
    def get(self, request):
        form = Form1()
        context = {'form': form}
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        form = Form1(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            company = form.cleaned_data['company']
            manager = form.cleaned_data['manager']
            budget = form.cleaned_data['budget']

            email = EmailMessage(
                subject='Inquiry from ' + str(email),
                body='Name: ' + str(name) + '\n'
                     + 'message: ' + str(message) + '\n'
                     + 'email: ' + str(email) + '\n'
                     + 'phonenumber: ' + str(phone) + '\n'
                     + 'company: ' + str(company) + '\n'
                     + 'manager: ' + str(manager) + '\n'
                     + 'budget: ' + str(budget) + '\n'


                ,
                from_email='jhaverihussain@gmail.com',
                to=['jhaverihussain@gmail.com']

            )
            email.send()

            return redirect(reverse('FishWeb:index'))
        else:
            return redirect(reverse('FishWeb:index'))
