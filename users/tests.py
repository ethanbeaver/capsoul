# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

from database.models import User

# Create your tests here.
class UserViewsTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		User.objects.create(username="test1", first_name="test", last_name="tester", date_of_birth="1999-09-09", phone=1234567890, location="in the test db")
		User.objects.create(username="anothertest", first_name="another", last_name="test", date_of_birth="1988-08-08", phone=9876543210, location="in the test db")
		User.objects.create(username="realper", first_name="real", last_name="person", date_of_birth="1992-12-02", phone=5050518212, location="the real world", date_joined="2017-11-14")

	def testGetAllUsers(self):
		response = self.client.get('/users').content.decode('utf8')
		self.assertJSONEqual(response, '{  "users": [{ "username": "test1", "first_name": "test", "last_name": "tester"}, { "username": "anothertest", "first_name": "another", "last_name": "test"}, { "username": "realper", "first_name": "real", "last_name": "person"}]}')

	def testGetSpecificUser(self):
		response = self.client.get('/users/realper').content.decode('utf8')
		self.assertJSONEqual(response, '{"users": [{"username": "realper", "first_name": "real", "last_name": "person", "is_staff": false, "phone": 5050518212, "photo": "", "is_active": true, "is_superuser": false, "date_of_birth": "1992-12-02", "last_login": null, "location": "the real world", "password": "", "email": "", "date_joined": "2017-11-14"}]}')

	def testPostUpdateUser(self):
		response = self.client.post('/users', data='{"first_name": "the", "last_name": "tester", "email": "test@test.test", "password": "test"}', content_type='application/json')
		self.assertEquals(response.status_code, 200)
		self.assertJSONEqual(response.content.decode('utf8'), '{"status": "resource created"}')
