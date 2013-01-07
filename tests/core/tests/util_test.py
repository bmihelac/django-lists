from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase
from django.test.client import RequestFactory

from lists import util
from lists.models import Folder

from ..models import Author


class UtilTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='foo')
        self.factory = RequestFactory()
        self.request = self.factory.get("")
        self.request.session = {}
        self.obj = Author.objects.create(name='Foo')

    def test_get_folder_from_request_for_anonymous(self):
        self.request.user = AnonymousUser()
        folder = util.get_folder_from_request(self.request, 'bar')
        self.assertIsInstance(folder, Folder)
        self.assertFalse(folder.user)

    def test_get_folder_from_request_for_user(self):
        self.request.user = self.user
        folder = util.get_folder_from_request(self.request, 'bar')
        self.assertIsInstance(folder, Folder)
        self.assertTrue(folder.user)

    def test_add_item_to_folder_for_anonymous(self):
        self.request.user = AnonymousUser()
        util.add_item_to_folder(self.request, 'bar', self.obj)
        folder = util.get_folder_from_request(self.request, 'bar')
        self.assertIn(self.obj, folder.items())

    def test_add_item_to_folder_for_user(self):
        self.request.user = self.user
        util.add_item_to_folder(self.request, 'bar', self.obj)
        folder = util.get_folder_from_request(self.request, 'bar')
        self.assertIn(self.obj, folder.items())
