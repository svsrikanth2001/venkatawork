from django.http import JsonResponse

from models import *


def list_books(request):
    all_books = []
    for book in TblBook.objects.all():
        all_books.append({
            'name': book.name
        })
    return JsonResponse({'books': all_books})


def list_chapters(request):
    book_id = request.GET.get('book_id', None)
    if not book_id:
        return JsonResponse({'message': 'book_id not provided'})

    try:
        chapters = TblBookReview.objects.filter(tbl_book_id=int(book_id)).order_by('id')
        all_chapters = []
        for chapter in chapters:
            all_chapters.append({
                'chapter': str(chapter.chapter),
                'description': chapter.description
            })

        return JsonResponse({'chapters': all_chapters})

    except TblBook.DoesNotExist:
        return JsonResponse({'message': 'book_id does not exist'})
