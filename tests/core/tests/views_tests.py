from django.test.testcases import TestCase
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from lists.models import Folder

from ..models import Author


class ViewTest(TestCase):

    def setUp(self):
        self.obj = Author.objects.create(name='Foo')

    def add_item(self, obj, folder_name="", next=""):
        ct = ContentType.objects.get_for_model(obj)
        data = {
                "content_type": ct.pk,
                "object_id": obj.pk,
                "folder_name": folder_name,
                }
        url = reverse('lists_item_create')
        if next:
            url = "%s?next=%s" % (url, next,)
        response = self.client.post(url, data)
        return response

    def test_add_item(self):
        response = self.add_item(self.obj)
        self.assertEqual(response.status_code, 302)
        folder = Folder.objects.get(name='')
        self.assertRedirects(response, '/favorites/folders/%s/' % folder.pk)

    def test_add_item_next(self):
        response = self.add_item(self.obj, next="/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_folders_view(self):
        self.add_item(self.obj, folder_name="")
        self.add_item(self.obj, folder_name="other folder")

        response = self.client.get(reverse('lists_folder_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _('default folder'))
        self.assertContains(response, 'other folder')

        folder = Folder.objects.get(name='')
        response = self.client.get(reverse('lists_folder_detail',
            kwargs={'pk': folder.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, unicode(self.obj))

    def test_remove_item(self):
        self.add_item(self.obj, folder_name="")

        folder = Folder.objects.get(name='')
        item = folder.item_set.all()[0]

        remove_url = reverse('lists_item_delete', kwargs={'pk': item.pk})
        response = self.client.get(remove_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(remove_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(folder.item_set.count(), 0)
