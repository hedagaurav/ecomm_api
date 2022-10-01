from django.db import models

# Create your models here.
'''
class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here
    product_name = models.CharField(max_length=100, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.product_name


class Cart(models.Model):
    """Model definition for Cart."""

    # TODO: Define fields here
    cart_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        """Meta definition for Cart."""

        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        """Unicode representation of Cart."""
        return self.cart_id

'''