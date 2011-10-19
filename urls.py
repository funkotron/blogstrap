from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name="index"),
    url(r'^(?P<post_slug>\w+)/$', 'blog.views.post', name="view_post"),
    (r'^site-admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':  settings.STATIC_ROOT}),
)