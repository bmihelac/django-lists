from django.test import TestCase
from django.contrib.auth.models import User

from lists.models import Folder, Item

from ..models import Author


class FolderTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='user')

    def test_create_folder(self):
        Folder.objects.create(name="folder", user=self.user)

    def test_create_folder_anonymoys(self):
        Folder.objects.create(name="folder")


class ItemTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Foo")
        self.folder = Folder.objects.create(name="folder")

    def test_create_item(self):
        Item.objects.create(content_object=self.author, folder=self.folder)
