from django.db import IntegrityError
from django.test import TestCase
from information.models import Unit, Scaffold

class ScaffoldTest(TestCase):
    """Tests to check scaffold cases"""
    def setUp(self):
        # Create a Unit for the test
        self.unit = Unit.objects.create(unit="Test Unit")

    def test_unique_scaffold_number(self):
        """Test to check error if two scaffold number are in
        the same unit."""
        # Create the first valid scaffold number
        valid_scaffold = Scaffold.objects.create(
            scaffold_number=1,
            scaffold_location="Gate Outside",
            unit=self.unit
        )
        # Test to create a new scaffold with same number and unit.
        with self.assertRaises(IntegrityError):
            Scaffold.objects.create(
                scaffold_number=1,
                scaffold_location="Inside Gate",
                unit=self.unit
            )

    def test_creating_scaffold_number(self):
        """Test to create 2 scaffolds in the same unit"""
        scaffold1 = Scaffold.objects.create(
            scaffold_number=2,
            scaffold_location="Gate Outside",
            unit=self.unit
        )

        scaffold2 = Scaffold.objects.create(
            scaffold_number=3,
            scaffold_location="Somewhere over the rainbow",
            unit = self.unit
        )
        # Check for both scaffolds
        self.assertEqual(Scaffold.objects.filter(unit=self.unit).count(), 2)