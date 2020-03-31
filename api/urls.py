from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from .views import Home,Generics,UpdateRetrieveDelete, ViewClass
from rest_framework import routers
router = routers.DefaultRouter()

router.register('v', ViewClass)

urlpatterns = [
    path('api-auth/',include('rest_framework.urls')),
    path('view/',include(router.urls)),
    path('generics/', Generics.as_view(), name="generics"),
    path('', Home.as_view(), name="home" ),
    path('api/token/', obtain_auth_token, name="obtainToken")
]
