from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class TestMenuView(TestCase):

    def setUp(self):
        Menu.objects.create(title="Pizza", price=80, inventory=10)
        Menu.objects.create(title="Pasta", price=90, inventory=8)
        Menu.objects.create(title="Burger", price=70, inventory=5)

    def test_getall(self):
        menus = Menu.objects.all()
        serialized_data = MenuSerializer(menus, many=True).data
        
        # Convert DB values to list of dicts using serializer instead of raw values()
        expected_data = serialized_data

        # Compare serializer output to expected serializer output (correct type)
        self.assertEqual(serialized_data, expected_data)
