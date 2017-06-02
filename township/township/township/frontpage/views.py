#from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import WelcomeForm


def welcome(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WelcomeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WelcomeForm()

    return render(request, 'frontpage/frontpage.html', {'form': form})
