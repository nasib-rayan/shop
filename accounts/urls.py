from django.urls import path
from accounts.views import moj 
from nasibshop.views import home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import ( login_view, register_view, logout_view , #profile_view, 
#edit_account_view,
)

app_name = 'accounts'


urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    #path('<slug>',views.article_detail, name= "detail"),
    #path('<user_id>/profile/', profile_view, name='profile'),
]





