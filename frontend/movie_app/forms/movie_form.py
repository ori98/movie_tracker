from django.forms import Form, widgets, CharField, DateField, Textarea

# Create a form
class MovieCreateForm(Form):
    name = CharField(label="movie name")
    description = CharField(label="movie description", widget=Textarea, required=False)
    release_date = DateField(label="release date", widget=widgets.DateInput(attrs={'type': 'date'}))