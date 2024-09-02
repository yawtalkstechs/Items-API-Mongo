from django.test import TestCase
from .models import Item
from django.db.utils import IntegrityError
from datetime import datetime

class ItemModelTest(TestCase):

    def setUp(self):
        # Set up the initial data for the tests
        self.item = Item.objects.create(
            name="Test Item",
            description="This is a test item."
        )

    def test_item_creation(self):
        # Test that an item is created successfully
        item = Item.objects.get(name="Test Item")
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.description, "This is a test item.")
        self.assertIsNotNone(item.created_at)
        self.assertIsNotNone(item.updated_at)

    def test_item_unique_name(self):
        # Test that the name field is unique
        with self.assertRaises(IntegrityError):
            Item.objects.create(name="Test Item", description="Another item")

    def test_item_string_representation(self):
        # Test the string representation of the item
        item = Item.objects.get(name="Test Item")
        self.assertEqual(str(item), "Test Item")

    def test_item_updated_at_changes(self):
        # Test that updated_at field changes when the item is updated
        old_updated_at = self.item.updated_at
        self.item.name = "Updated Test Item"
        self.item.save()
        self.assertNotEqual(self.item.updated_at, old_updated_at)
