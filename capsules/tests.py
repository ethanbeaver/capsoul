# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

# Create your tests here.
class CapsuleViewsTestCase(TestCase):
	def testStaticMethod(self):
		client = Client()
		response = client.get('/capsules/1/letters/2').content.decode('utf8')
		self.assertEqual(response, '{"owner": "rabery", "text": "Hey, I made this capsule for you! Hope you like it", "title": "Best Wishes"}')
		