from django.db import models

class Perfume(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='perfumes/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} — {self.brand}"


class CartItem(models.Model):
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.perfume.price

    def __str__(self):
        return f"{self.perfume.name} x {self.quantity}"
