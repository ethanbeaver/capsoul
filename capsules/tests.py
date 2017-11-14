# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from views import get_letters

# Create your tests here.
class CapsuleViewsTestCase(TestCase):
	def testStaticMethod(self):
		self.assertEqual(get_letters(1,2,3),{"text": "Hey, I made this capsule for you! Hope you like it", "title": "Best Wishes",
                         "owner": "rabery"})
		
