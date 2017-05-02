#ask/qa/urls,py
from django.conf.urls import url
from . import views 


urlpatterns =  [

#	url(r'^', views.test),
	url(r'^login/', views.test, name='login'),
	url(r'^signup/', views.test, name='signup'),
	url(r'^question/', views.test, name='question'),
	url(r'^ask/', views.test, name='ask'),
	url(r'^popular/\D/', views.test, name='popular'),
	url(r'^new/', views.test, name='new'),

]
