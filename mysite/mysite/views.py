from django.shortcuts import HttpResponse
from django.http import JsonResponse

from models import * 
# Create your views here.
def index(request):
    return HttpResponse("Hello world Welcome to Python!!.")

def booklist(request):
    all_books = []
    for book in TblBook.objects.all():
        all_books.append({
            'name': book.BookName
        })
    return JsonResponse({'books': all_books})

def tblBook(request):
	 return JsonResponse({'key': 'value'}) 