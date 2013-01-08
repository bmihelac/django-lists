from django.conf.urls.defaults import patterns, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
        (r'^admin/', include(admin.site.urls)),
        (r'^favorites/', include('lists.urls')),
        (r'^', include('core.urls')),
)

urlpatterns += staticfiles_urlpatterns()
