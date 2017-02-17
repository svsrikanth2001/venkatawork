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

def list_chapters(request):
    #book_id = request.GET.get('book_id', None)
    if not book_id:
        return JsonResponse({'message': 'book_id not provided'})

    try:
        chapters = TblBookReview.objects.filter(tblbook_id=int(1)).order_by('id')
        all_chapters = []
        for chapter in chapters:
            all_chapters.append({
                'chapter': str(chapter.chapter),
                'description': chapter.desciption
            })

        return JsonResponse({'chapters': all_chapters})

    except TblBook.DoesNotExist:
        return JsonResponse({'message': 'book_id does not exist'})
