from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("wiki/<str:title>",views.entry_page,name="entry_page"),
    path("search/",views.search_page,name="search_page"),
    path("new/",views.create_new_page,name="create_new_page"),
    path("edit/",views.edit_bar,name="edit_bar"),
    path("save_the_edit/",views.save_the_edit,name="save_the_edit"),
    path("rand/",views.rand_page,name="rand_page")
]
