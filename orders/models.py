from django.db import models

# Create your models here.


class Order(models.Model):
    marketplace = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    shipping = models.DecimalField(max_digits=5, decimal_places=2)
    address = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return 'Marketplace : {}, Amount : {}, Shipping : {}, Address : {}, LastName : {}, City : {}'\
            .format(self.marketplace, self.amount, self.shipping, self.address, self.last_name, self.city)
