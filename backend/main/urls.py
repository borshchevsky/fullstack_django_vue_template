from rest_framework.routers import DefaultRouter

from main.views import TestModelView

router = DefaultRouter()
router.register('test', TestModelView)
