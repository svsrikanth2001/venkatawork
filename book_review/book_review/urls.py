from django.conf.urls import url
from django.contrib import admin

from main.views import list_books, list_chapters

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^list_books/', list_books),
    url(r'^list_chapters/', list_chapters),
]
