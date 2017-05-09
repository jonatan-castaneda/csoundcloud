from django.conf.urls import url,include #agrego include
from django.contrib import admin
import csoundcloud.api_urls as api_urls#hago este import
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(api_urls)),
]
