from rest_framework.routers import DefaultRouter

from backend.views import TestModelView

router = DefaultRouter()
router.register('test', TestModelView)
