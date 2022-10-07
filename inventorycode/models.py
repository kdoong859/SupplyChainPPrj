from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Inventory(models.Model):
    inventory_diff = models.IntegerField(blank=False, null=True)
    inventory_excess_type_usual = models.IntegerField(blank=False)
    inventory_excess_type_rec = models.IntegerField(blank=False)
    inventory_carry_cost = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_hold_cost = models.DecimalField(max_digits=5, decimal_places=2)
    unit_cost = models.DecimalField(max_digits=5, decimal_places=2)
    extra_cost = models.DecimalField(max_digits=10, decimal_places=2)


class Production(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    order_release_date = models.DateField()
    material_id = models.IntegerField(blank=True, null=True)
    order_quantity = models.IntegerField(blank=True, null=True)


class Procurement(models.Model):
    IS_RECEIVED = [('Y', 'yes'),
                   ('N', 'no'), ]
    buyer_location_id = models.IntegerField(blank=False)
    buyer_address = models.CharField(max_length=100, blank=False)
    buyer_name = models.CharField(max_length=50, blank=False)
    supplier_location_id = models.IntegerField(blank=False)
    supplier_address = models.CharField(max_length=100, blank=False)
    supplier_name = models.CharField(max_length=50, blank=False)
    status = models.BooleanField(default=True)
