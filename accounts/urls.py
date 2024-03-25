from django.urls import path
from accounts import views

from nasibshop.views import home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import ( login_view, signup_view, logout_view , #profile_view, 
#edit_account_view,
)

app_name = 'accounts'


urlpatterns = [
    path('login/', login_view, name='login'),
    path('log/', log_view, name='log'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    #path('<slug>',views.article_detail, name= "detail"),
    #path('<user_id>/profile/', profile_view, name='profile'),
]





