from django.conf.urls  import include, url, patterns
from listen import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
  

#    url(r'^stores/(?P<store>[a-zA-Z0-9]+)/$', views.filt, name='filt'),
#    url(r'^items/(?P<item_id>\d+)/$', views.items, name='items'),
#    url(r'^search', views.search, name='search'),
#    url(r'^find/$', views.find, name='find'),
#    url(r'^about/$', views.about, name='about'),
#    url(r'^api/', include(v1_api.urls)),
#    url(r'^m/', views.m, name='m'),
#    url(r'^product/(?P<item_id>\d+)/$', views.product, name='product')
     )

     

