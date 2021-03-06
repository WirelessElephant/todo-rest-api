from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jwt-auth/', obtain_jwt_token)
]
