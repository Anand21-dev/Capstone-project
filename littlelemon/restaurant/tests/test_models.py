from django.test import TestCase
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu

class TestMenuModel(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Waffle", price=20, inventory = 3)
        self.assertEqual(str(item),"Waffle : 20$")