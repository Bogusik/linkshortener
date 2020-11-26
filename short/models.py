from django.db import models

# Create your models here.


class Linker(models.Model):
    link_hash = models.CharField('Hash', primary_key=True, max_length=8)
    link = models.CharField('Link', max_length=300, null=False)
    visits = models.IntegerField('Visits', default=0)

    def __str__(self):
        return self.link_hash