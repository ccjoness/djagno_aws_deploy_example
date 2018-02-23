from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import m2m_changed, post_save
import decimal


class User(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.ManyToManyField('Address', blank=True)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    sate = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)


class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='orders')
    total = models.CharField(max_length=20, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)

    def get_total(self):
        total = decimal.Decimal(0)
        for i in self.pizzas.all():
            total += decimal.Decimal(i.price)
        return total

    def update_price(self):
        self.total = self.get_total()
        self.save()


class Pizza(models.Model):
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    )
    SIZE_PRICES = {
        'S': decimal.Decimal(10.99),
        'M': decimal.Decimal(14.99),
        'L': decimal.Decimal(21.99),
        'XL': decimal.Decimal(30.99)
    }

    toppings = models.ManyToManyField('Topping', blank=True)
    size = models.CharField(max_length=255, choices=SIZE_CHOICES)
    price = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='pizzas')

    def get_toppings_names(self):
        return [x.name for x in self.toppings.all()]

    def get_toppings_total(self):
        total = 0
        for i in self.toppings.all():
            total += i.price
        return total

    def update_price(self):
        self.price = self.get_toppings_total() + self.SIZE_PRICES[self.size]
        self.save()

    def __str__(self):
        return '{size} - {tp}'.format(size=self.size, tp=self.get_toppings_names())


class Topping(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)

    def __str__(self):
        return self.name


def update_pizza_total(sender, **kwargs):
    print('Updating Pizza Total...')
    kwargs['instance'].update_price()


def update_order_total(sender, instance, **kwargs):
    print('Updati'
          'ng Order Total..')
    instance.order.update_price()


m2m_changed.connect(update_pizza_total, sender=Pizza.toppings.through)
m2m_changed.connect(update_order_total, sender=Pizza.toppings.through)