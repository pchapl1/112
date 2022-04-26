from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView



class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutMeView(TemplateView):
    template_name = 'about.html'