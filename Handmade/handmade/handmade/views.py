from django.http import HttpResponse
from django.shortcuts import render
from models import faq_question, faq_answer


def faq(request):
    """Return FAQ page to website"""
    template = 'faq.html'
    context = {'question': faq_question, 'answer': faq_answer}
    return render(request, template, context)

def contacts(request):
    """Return static Contacts page"""
    template = 'contacts.html'
    return render(request,template)