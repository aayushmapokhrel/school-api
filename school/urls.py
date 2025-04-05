from django.urls import path, include
from rest_framework.routers import DefaultRouter
from school.views import SchoolViewSet, StudentViewSet, TeacherViewSet

router = DefaultRouter()
router.register(r"schools", SchoolViewSet)
router.register(r"students", StudentViewSet)
router.register(r"teachers", TeacherViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
