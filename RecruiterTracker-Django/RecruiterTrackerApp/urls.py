#from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'contacts', views.ContactViewset)
#router.register(r'tasks', views.TaskViewSet)
#router.register(r'users', views.UserViewSet)