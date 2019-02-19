from django.shortcuts import render

# Create your views here.

#need to be on views oage to import httptrespone
from django.http import HttpResponse


#these are the function that i made to display the response when a specific url is typed
def gogetthegood(request):
    return HttpResponse("Here you go!! totoro agenda")

#will display response
def happyhappyjoyjoy(request):
    return HttpResponse("anime and kareem kun melaati chan")