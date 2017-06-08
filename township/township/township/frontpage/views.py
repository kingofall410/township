import csv
import os
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import WelcomeForm
from .models import County, State, Muni


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

def load_data(request):
    #return HttpResponse(os.getcwd())
    with open('township/frontpage/static/frontpage/TownshipCounty.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        thestate = State.objects.get(name="Pennsylvania")
        for row in spamreader:
            townshipname = row[0]
            countyname = row[1]
            if (County.objects.filter(name=countyname)):
                thecounty = County.objects.get(name=countyname)
            else:
                thecounty = County(name=countyname, state=thestate)
                thecounty.save()
                
            township = Muni(name=townshipname, county=thecounty)
            township.save()
        return HttpResponse("data loaded")