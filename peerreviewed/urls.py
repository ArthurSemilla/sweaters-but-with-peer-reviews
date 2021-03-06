from django.conf.urls import include, url
from django.contrib import admin
import browse.views as bviews

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Prolly should move, but it's more of a browse thing
    url(r'^$', bviews.index, name="home"),

    # Shitty catch for need to be logged in error
    url(r'^logged_in.*', bviews.index,
        kwargs={"message": "You must be logged in to view that page."}),

    # Other modules
    url(r'^browse/', include('browse.urls')),
    url(r'^(new|edit)/', include('new.urls')),
    url(r'^delete', bviews.delete, name="delete"),
    url(r'^get/', include('ajax.urls')),
    url(r'^accounts/', include('accounts.urls')),
]
