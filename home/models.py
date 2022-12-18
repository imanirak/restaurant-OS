from wagtail.models import Page
from django.db import models
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

UNIT_OPTIONS = [
   ('tbsp', 'Tablespoon'),
   ('lbs', 'Pounds'),
]
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=100,
                            choices=UNIT_OPTIONS)
    price_per_unit = models.FloatField(default=0)
    
    def __str__(self):
        return f"""
        name={self.name}
        qty={self.quantity}
        unit={self.unit}
        unit_price={self.price_per_unit}
        """
class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
  
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
