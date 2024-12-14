from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests

from .forms.movie_form import MovieCreateForm

def index(request):
    return render(request, "index.html")

def insert(request):
    if request.method == "POST":
        form = MovieCreateForm(request.POST)

        if form.is_valid():
            movie_name = form.cleaned_data["name"]
            movie_desc = form.cleaned_data["description"]
            movie_date = form.cleaned_data["release_date"]

            return HttpResponseRedirect("/movie-app")
        
    # Else we just re-render the form
    context = {}
    context['form'] = MovieCreateForm()

    return render(request, "movie_adder.html", context)