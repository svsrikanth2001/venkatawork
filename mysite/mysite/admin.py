from django.contrib import admin

from .models import TblBook
from .models import TblBookReview

@admin.register(TblBook)
class TblBookAdmin(admin.ModelAdmin):
	list_display = ['id','BookName']


@admin.register(TblBookReview)
class TblBookReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'chapter', 'desciption']