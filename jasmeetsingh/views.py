# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# def status(request):
#     return HttpResponse("Hello, world. You're at Jasmeet Singh's biog.")

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"