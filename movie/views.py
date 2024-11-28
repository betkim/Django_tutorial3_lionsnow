from django.shortcuts import render
from django.views import generic
# Create your views here.

class MovieView(generic.TemplateView):
    template_name = 'movie/movie.html'