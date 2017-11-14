# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

from database.models import Capsule

# Create your tests here.
class CapsuleViewsTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		Capsule.objects.create(unlocks_at="2017-12-10T14:30Z", owner="rabery", recipients="beavet", title= "Winter Surprise", contributors=["fennma", "delejo"], description= "A capsule that Ryan made for Ethan for being such a good ASWWU employee")
		Capsule.objects.create(unlocks_at="2018-01-10T03:00Z", owner="fennma", recipients="rabery", title= "Software Engineering", contributors=["beavet"], description= "A capsule for Software Engineering")

	def testGetAllCapsules(self):
		response = self.client.get('/capsules').content.decode('utf8')
		self.assertJSONEqual(response, '{"capsules": [{"owner": "rabery", "title": "Winter Surprise", "unlocks_at": "2017-12-10T14:30:00Z", "recipients": "beavet", "cid": 1}, {"owner": "fennma", "title": "Software Engineering", "unlocks_at": "2018-01-10T03:00:00Z", "recipients": "rabery", "cid": 2}]}')

	def testGetSpecificCapsule(self):
		response = self.client.get('/capsules/1').content.decode('utf8')
		self.assertJSONEqual(response, '{"capsules": [{"letters": "", "contributors": "[u\'fennma\', u\'delejo\']", "recipients": "beavet", "title": "Winter Surprise", "media": "", "cid": 1, "comments": "", "owner": "rabery", "unlocks_at": "2017-12-10T14:30:00Z", "description": "A capsule that Ryan made for Ethan for being such a good ASWWU employee"}]}')

	def testPostCreateCapsule(self):
		response = self.client.post('/capsules')
		self.assertEquals(response.status_code, 200)
		self.assertJSONEqual(response.content.decode('utf8'), '{"status": "resource created"}')

	def testPostUpdateCapsule(self):
		response = self.client.post('/capsules/1')
		self.assertEquals(response.status_code, 200)
		self.assertJSONEqual(response.content.decode('utf8'), '{"status": "resource created"}')

	def testStaticViewLetters(self):
		response = self.client.get('/capsules/1/letters/2').content.decode('utf8')
		self.assertJSONEqual(response, '{"text": "Hey, I made this capsule for you! Hope you like it", "title": "Best Wishes", "owner": "rabery"}')

	def testStaticGetMedia(self):
		response = self.client.get('/capsules/1/media/3').content.decode('utf8')
		self.assertJSONEqual(response,'{"owner": "rabery", "url": "http://lorempixel.com/400/400/cats/"}')

	def testStaticAddMedia(self):
		response = self.client.post('/capsules/1/media')
		self.assertEquals(response.status_code, 200)
		self.assertJSONEqual(response.content.decode('utf8'), '{"status": "resource created"}')

	def testStaticAddLetters(self):
		response = self.client.post('/capsules/1/media')
		self.assertEquals(response.status_code, 200)
		self.assertJSONEqual(response.content.decode('utf8'), '{"status": "resource created"}')

	def testStaticAddComments(self):
		response = self.client.post('/capsules/1/media')
		self.assertEquals(response.status_code, 200)
		self.assertJSONEqual(response.content.decode('utf8'), '{"status": "resource created"}')
