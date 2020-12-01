from django.db import models


class Gender(models.Model):
    male = 'M'
    female = 'F'
    gender_choice = [(male, 'Male'),(female, 'Female')]
    gender = models.CharField(max_length=1, choices=gender_choice)

    def __str__(self):
        return self.gender


class Product(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    price = models.FloatField()
    description = models.CharField(max_length=2000)
    stock = models.PositiveIntegerField(default=1)
    product_image = models.ImageField(upload_to='products')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


