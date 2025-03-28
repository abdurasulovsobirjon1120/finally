from django.db import models
# from django.apps import cdAppConfig

# Create your models here.

class Maqola(models.Model):
    HOME = 'home'
    FOTOS = 'fotos'
    OUR_SERVICE = 'our_service'

    TAG = (
        ('home' , HOME),
        ('fotos' , FOTOS),
        ('our_service' ,OUR_SERVICE)
    )


    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50 ,null=True , blank=True)
    image = models.ImageField()
    tag = models.CharField(max_length=15, choices=TAG)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property  #funksiyani field dek qiladi  || xuddi o'zgaruvchidek bo'ladi .
    def imageURL(self ):
        return self.image.url

    def __str__(self):
        return f'{self.id} ---- {self.title}'