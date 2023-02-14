<<<<<<< HEAD
from django.db import models
from rej_home.models import Product


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:

        orddb_table = 'Cart'ring = ['date_added']

    def __str__(self):
        return '{}'.format(self.cart_id)


class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.productPrice * self.quantity

    def __str__(self):
        return '{}'.format(self.product)
=======
from django.db import models

# Create your models here.
>>>>>>> origin/main
