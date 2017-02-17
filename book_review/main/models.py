from __future__ import unicode_literals

from django.db import models


class TblBook(models.Model):
    name = models.CharField(max_length=512)

    def __unicode__(self):
        return 'TblBook id: ' + str(self.id)


class TblBookReview(models.Model):
    tbl_book = models.ForeignKey(TblBook)
    chapter = models.PositiveSmallIntegerField()
    description = models.TextField()
