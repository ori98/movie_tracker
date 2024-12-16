from django.forms import Form, CharField, widgets

class MovieSearch(Form):
    search_term = CharField(label="search_term")