
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from nasibshop import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



app_name ="nasibshop"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.home , name= 'home'),
    path('kharid', veiws.kharid , name='kharid')
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


