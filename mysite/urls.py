from django.conf.urls import url, include
from django.views.generic import TemplateView

from mysite.reviews import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^reviews/$', views.review_list, name='review_list'),
    url(r'^reviews/create/$', views.review_create, name='review_create'),
    url(r'^reviews/(?P<pk>\d+)/update/$', views.review_update, name='review_update'),
    url(r'^reviews/(?P<pk>\d+)/delete/$', views.review_delete, name='review_delete'),
    url(r'^reviews/search/$',views.search, name='search'),
    url(r'^advanced/$', views.advanced, name='advanced'),
    url(r'^visualize/$', views.visualize, name='visualize'),
]
