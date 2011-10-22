"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Person, Pair


class test_pair_stairs_model(TestCase):

    def setUp(self):
        self.person1 = Person(name = "Person1")
        self.person2 = Person(name = "Person2")
        self.person3 = Person(name = "Person3")
        self.person4 = Person(name = "Person4")
        self.person1.save()
        self.person2.save()
        self.person3.save()
        self.person4.save()

    def test_that_person_exists(self):
        expected_name = "Person1"
        self.assertEquals(self.person1.name, expected_name)

    def test_that_persons_in_pair_exist(self):
        self.pair = Pair(pair1 = self.person1, pair2 = self.person2, count = 0)
        pair_result = self.pair.pair1.name, self.pair.pair2.name
        expected = "Person1", "Person2"
        self.assertEqual(pair_result, expected)

    def test_that_pairing_adds_one_to_count(self):
        pair = Pair(pair1 = self.person1, pair2 = self.person2, count = 0)
        pair.add_count_to_pair()
        self.assertEqual(1, pair.count)

    def test_create_pairs(self):
        self.person1.create_pairs()
        list_all_pairs = Pair.objects.all()
        expected_pair1 = "Person1", "Person1", 0
        actual_pair1 = list_all_pairs[0].pair1.name, list_all_pairs[0].pair2.name, list_all_pairs[0].count
        expected_pair2 = "Person1", "Person2", 0
        actual_pair2 = list_all_pairs[1].pair1.name, list_all_pairs[1].pair2.name, list_all_pairs[1].count
        self.assertEqual(actual_pair1,expected_pair1)
        self.assertEqual(actual_pair2,expected_pair2)





    def tearDown(self):
        self.person1.delete()
        self.person2.delete()
        self.person3.delete()
        self.person4.delete()
