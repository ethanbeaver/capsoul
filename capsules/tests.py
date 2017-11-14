# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.test import TestCase, Client

# Create your tests here.
class CapsuleViewsTestCase(TestCase):
	def testStaticMethod(self):
		client = Client()
		response = json.loads(client.get('/capsules/1/letters/2').content.decode('utf8'))
		self.assertEqual(response, {"text": "Hey, I made this capsule for you! Hope you like it", "title": "Best Wishes",
                         "owner": "rabery"})