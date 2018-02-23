import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizza.settings')
import django

django.setup()
from pages.models import Topping

names = ['Roma', 'Red', 'Spinach', 'Broccoli', 'Pineapple', 'Jalapeno Peppers', 'Kalamata Olives', 'Fresh Mushrooms',
         'Green Olives', 'Green Peppers', 'Roasted Garlic', 'Hot Banana Peppers', 'Roasted Red Peppers',
         'Sun Dried Tomatoes', 'Grilled Zucchini', 'Potato slice', 'Caramelized Onions', 'Cilantro', 'Anchovies',
         'Bacon Crumble', 'Bacon Strips', 'Chicken', 'Ground Beef', 'Italian Ham', 'Spicy Italian Sausage',
         'Steak Strips', 'BBQ Steak Strips', 'Pepperoni (NY Style)', 'Pepperoni (original)', 'Salami', 'Chipotle Steak',
         'Chipotle Chicken', 'Chorizo Sausage', 'Capicollo', 'Feta Cheese', 'Parmesan Cheese', 'Extra Cheese',
         'Four Cheese', 'Goat Cheese', 'Mozzarella', 'Dairy Free Cheeze']

for n in names:
    Topping.objects.create(name=n, price=0.50)