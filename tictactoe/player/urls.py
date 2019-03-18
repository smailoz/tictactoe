from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView       #8.4 Login Logout işlemleri kütüphaneleri yükle

from .views import home, new_invitation, accept_invitation, SignUpView               # views in içindeki home classını yükle. 8.11 deki new_invitation kutup yukle

urlpatterns = [
    url(r'home$', home, name="player_home") ,                  # homeisimli uzantıyı çağır. ^ ile başlamıyor. Çünkü önünde player olacak. # 8.2 name kısmını ilave et.  
    url(r'login$', LoginView.as_view(template_name="player/login_form.html"),  name="player_login") ,                                       #8.4 Login Logout işlemleri
    url(r'logout$', LogoutView.as_view(),name="player_logout") ,                                             #8.4 Login Logout işlemleri
    url(r'new_invitation$', new_invitation, name="player_new_invitation"), # 8.11 
    url(r'accept_invitation/(?P<id>\d+)/$', accept_invitation, name="player_accept_invitation"), # 8.19 
    url(r'signup$', SignUpView.as_view(), name="player_signup") 
]                                                             