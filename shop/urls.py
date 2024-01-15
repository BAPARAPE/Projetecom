from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.views import  login_user, logout_user
from shop import settings
from store.views import index, product_detail, add_to_cart, cart

urlpatterns = [
    path('', index, name="index"),
    path('cart', cart, name="cart"),
    path('signup', signup, name="signup"),
    path('login_user', login_user, name="login"),
    path('logout_user', logout_user, name="logout"),
    path('product/<str:slug>', product_detail, name="detail"),
    path('product/<str:slug>/add_to_cart', add_to_cart, name="add_to_cart"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
