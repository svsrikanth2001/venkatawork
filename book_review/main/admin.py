from django.contrib import admin

from models import *


@admin.register(TblBook)
class TblBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(TblBookReview)
class TblBookReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'chapter', 'description')
