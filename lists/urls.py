from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
        url(r'^folders/$', views.FolderListView.as_view(),
            name="lists_folder_list"),
        url(r'^folders/(?P<pk>\d+)/$', views.FolderDetailView.as_view(),
            name="lists_folder_detail"),
        url(r'^item/add/$', views.ItemCreateView.as_view(),
            name="lists_item_create"),
        url(r'^item/remove/(?P<pk>\d+)/$', views.ItemDeleteView.as_view(),
            name="lists_item_delete"),
        )
