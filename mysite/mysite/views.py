from django.shortcuts import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world Welcome to Python!!.")

def booklist(request):
    return JsonResponse({'key': 'value'}) 

def tblBook(request):
	 return JsonResponse({'key': 'value'}) 