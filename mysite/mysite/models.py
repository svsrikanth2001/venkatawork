from django.db import models

class TblBook(models.Model):
    BookName = models.CharField(max_length=200)
    def __unicode__(self):
        return 'TblBook id: ' + str(self.id)
    
class TblBookReview(models.Model):
	tblbook = models.ForeignKey(TblBook, on_delete=models.CASCADE)
	chapter = models.IntegerField()
	desciption = models.TextField()