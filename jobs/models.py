from django.db import models

from datetime import datetime

class Data(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('data',)

    def __str__(self):
        return '%s/%s/%s' % (self.data.day, self.data.month,
                             self.data.year,)


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=50)
    data = models.ForeignKey(Data, on_delete=models.CASCADE,
                             related_name='jobs')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return "%s - %s" % (self.title, self.company,)


