from django.test import TestCase
from datetime import date
from .models import acd_Patents, Patents

class PatentsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        acd = acd_Patents.objects.create(
            abstract='Abstract',
            claims='Claims',
            description='Description'
        )
        cls.patent = Patents.objects.create(
            number='12345',
            title='Test Patent',
            date=date.today(),
            country='USA',
            authors='John Doe',
            mpk='MPK Code',
        )
        cls.patent.asd = acd
        cls.patent.save()

    def test_acd_patent_creation(self):
        acd = acd_Patents.objects.create(
            abstract='Abstract',
            claims='Claims',
            description='Description'
        )
        self.assertEqual(acd.abstract, 'Abstract')
        self.assertEqual(acd.claims, 'Claims')
        self.assertEqual(acd.description, 'Description')

    def test_patent_creation_no_required_fields(self):
        patent = Patents.objects.create(
            number=None,
            title=None,
            date=None,
            country=None,
            authors=None,
            mpk=None
        )
        self.assertIsNotNone(patent.id)

    def test_patent_creation_required_fields(self):
        patent = Patents.objects.create(
            number='12345',
            title='Test Patent',
            date=date.today(),
            country='USA',
            authors='John Doe',
            mpk='MPK Code',
        )
        self.assertIsNotNone(patent.id)

    def test_acd_patent_update(self):
        acd = acd_Patents.objects.create(
            abstract='Abstract',
            claims='Claims',
            description='Description'
        )
        acd.abstract = 'Updated Abstract'
        acd.claims = 'Updated Claims'
        acd.description = 'Updated Description'
        acd.save()
        updated_acd = acd_Patents.objects.get(id=acd.id)
        self.assertEqual(updated_acd.abstract, 'Updated Abstract')
        self.assertEqual(updated_acd.claims, 'Updated Claims')
        self.assertEqual(updated_acd.description, 'Updated Description')



