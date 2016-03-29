
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^me/', include('resume.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'', include('home.urls')),

]
