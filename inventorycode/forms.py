from django import forms
from .models import Inventory, Production, Procurement


class NewInventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ["inventory_diff", "inventory_excess_type_usual", "inventory_excess_type_rec", "inventory_carry_cost",
                  "inventory_hold_cost", "unit_cost", "extra_cost"]


class NewProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ["order_id", "order_release_date", "material_id", "order_quantity"]


class NewProcurementForm(forms.ModelForm):
    class Meta:
        model = Procurement
        fields = ["buyer_name", "buyer_address", "buyer_location_id", "supplier_name",
                  "supplier_address", "supplier_location_id", "status"]
