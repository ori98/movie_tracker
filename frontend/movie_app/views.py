from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests

from .forms.movie_form import MovieCreateForm
from .forms.moive_search import MovieSearch

# BASE URL
base_url = "http://127.0.0.1:40069/"

def index(request):
    msg = request.GET.get("msg", None)
    context = {"msg": msg}
    return render(request, "index.html", context)

def insert(request):
    # Initializing the context
    context = {}

    if request.method == "POST":
        form = MovieCreateForm(request.POST)

        if form.is_valid():
            movie_name = form.cleaned_data["name"]
            movie_desc = form.cleaned_data["description"]
            movie_date = form.cleaned_data["release_date"]

            payload = {
                'name': movie_name,
                'description': movie_desc,
                'release_date': str(movie_date)
            }

            # Movie insertion API
            movie_insert_api_url = base_url + "add-movie"
            response = requests.post(movie_insert_api_url, json=payload)

            if response.status_code >= 200 and response.status_code <= 299:
                return HttpResponseRedirect(f"/movie-app/?msg=Movie added SUCCESSFULLY")
            else:
                return HttpResponseRedirect(f"/movie-app/?msg=Movie addition FAILED")
        
    # Else we just re-render the form
    context['form'] = MovieCreateForm()

    return render(request, "movie_adder.html", context)

def browse(request):
    context = {}
    context["form"] = MovieSearch()

    # Caching recent searches in session
    recent_search_results = request.session.get("recent_search_results", [])

    # Getting the search results
    if request.method == "POST":
        # Checking if the `Clear` button was clicked
        if 'clear' in request.POST:
            # Flushing all the data
            request.session.flush()
            return HttpResponseRedirect(reverse("movie_browse"))

        # Getting the form data
        form = MovieSearch(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data["search_term"]

        # Calling the search value from API
        api_url = base_url + "/get-movie"

        query_param = {'search_term': search_term}

        matching_movies = requests.get(api_url, params=query_param)

        if matching_movies.status_code >= 200 and matching_movies.status_code <= 299:
            results = matching_movies.json()

            # Persisting the search results to the session
            recent_search_results.insert(0, {"term": search_term, "results": results})
            # Keeping only the last 5 entries
            recent_search_results = recent_search_results[:5]
            request.session["recent_search_results"] = recent_search_results

            # Setting the context
            context["results"] = results

            # The recent search results will be part of the request.session dictionary
        else:
            context["results"] = f"No movies found with the name: {search_term}"

    return render(request, "browse.html", context)