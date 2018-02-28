from django.db import models

class Product(models.Model):
    name = models.TextField(max_length=512)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Specification(models.Model):
    product = models.ForeignKey(
        Product, related_name='products', null=True,
        on_delete=models.CASCADE)
    cpufrequency = models.FloatField(blank=True)
    cpu = models.TextField(max_length=200,blank=True)
    ram = models.IntegerField(blank=True)
    hdd = models.IntegerField(blank=True)
    imgpath = models.CharField(max_length=200,blank=True)



