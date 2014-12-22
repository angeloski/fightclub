from django.conf.urls import patterns, include, url
from django.contrib import admin

from fight import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fightclub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'fight.views.home', name='home'),
)

