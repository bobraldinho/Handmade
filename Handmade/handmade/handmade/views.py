from django.shortcuts import render
from .models import FaqQuestion, FaqAnswer


def faq(request):
    """Return FAQ page to website"""
    template = 'faq.html'
    context = {'questions': FaqQuestion.objects.all(), 'answers': FaqAnswer.objects.all()}
    return render(request, template, context)


def contacts(request):
    """Return static Contacts page"""
    template = 'contacts.html'
    return render(request, template)