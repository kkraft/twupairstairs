# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Person


def index(request):
    list_all_persons = Person.objects.all()
    return render_to_response('pairs/index.html', {'list_all_persons': list_all_persons})



def detail(request, pair_id):
    return HttpResponse("Your looking at pair %s." % pair_id)
