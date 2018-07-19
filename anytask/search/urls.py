from django.conf.urls import url

from search import views

urlpatterns = [
    url(r'^$', views.search_page, name="search.views.search_page"),
    url(r'^users$', views.ajax_search_users, name="search.views.ajax_search_users"),
    url(r'^courses$', views.ajax_search_courses, name="search.views.ajax_search_courses"),
]
