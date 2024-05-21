from django.db import models
# from django.apps import cdAppConfig

# Create your models here.

class Maqola(models.Model):
    WORLD = 'world'
    LOCAL = 'local'
    SPORT = 'sport'

    TAG = (
        ('world' , WORLD),
        ('local' , LOCAL),
        ('sport' ,SPORT)
    )


    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50 ,null=True , blank=True)
    image = models.ImageField()
    tag = models.CharField(max_length=10, choices=TAG)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property  #funksiyani field dek qiladi  || xuddi o'zgaruvchidek bo'ladi .
    def imageURL(self ):
        return self.image.url

    def __str__(self):
        return f'{self.id} ---- {self.title}'