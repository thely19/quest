from django.conf.urls import url
from basicapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form/', views.form_name_view, name='form_name'),
]
