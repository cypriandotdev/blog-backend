from django.urls import path, include
import api.views as api

urlpatterns = [
    path('', api.home, name="home"),
    path("login", api.login_user, name="login"),
    path("logout", api.logout_user, name="logout"),
    path("new", api.new, name="new"),
    path("pending", api.pending, name="pending"),
    path("published", api.published, name="published"),
    path("pending/<slug:slug>", api.pending_article, name="pending_article"),
    path("published/<slug:slug>", api.published_article, name="published_article"),
    path("edit/<slug:slug>", api.edit_article, name="edit_article"),
    path("logout", api.logout_user, name="logout"),

    path("ajax/add_series_or_category", api.add_series_or_category, name="add_series_or_category"),
    path("ajax/publish", api.publish, name="publish"),
    path("ajax/delete", api.delete, name="delete"),

    path('tinymce/', include('tinymce.urls')),

]
