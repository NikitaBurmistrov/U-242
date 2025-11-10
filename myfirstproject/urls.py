from django.contrib import admin
from django.urls import path, re_path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/', views.simple_view),
    path('complex/', views.complex_view),
    path('statfiles/', views.static_files_view),
    path('', views.index_view),
    path('about/', views.about_view),
    path('contacts/', views.contacts_view),
    path('formhtml/', views.form_html_view),
    path('fields/', views.fields_view),
    path('userdata/', views.userdata_view),
    re_path(r'^user/(?P<username>\w+)/$', views.user_profile),
    re_path(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', views.archive),
    path('search/', views.search),
]