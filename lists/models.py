from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from .managers import FolderManager


class Folder(models.Model):
    user = models.ForeignKey(User,
            verbose_name=_('User'), blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)

    objects = FolderManager()

    class Meta:
        verbose_name = _('Folder')
        verbose_name_plural = _('Folders')

    def __unicode__(self):
        return self.name or ugettext('default folder')

    def items(self):
        return [obj.content_object for obj in self.item_set.all()]

    @models.permalink
    def get_absolute_url(self):
        return ('lists_folder_detail', [str(self.pk)],)


class Item(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    folder = models.ForeignKey(Folder,
            verbose_name=Folder._meta.verbose_name)
    created_on = models.DateTimeField(auto_now_add=True)
    ordering = models.PositiveIntegerField(_('Ordering'), default=0)

    class Meta:
        verbose_name = _('List item')
        verbose_name_plural = _('List items')
        ordering = ['ordering', '-created_on']
