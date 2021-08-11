from rest_framework.routers import DefaultRouter

from forum.api.views import ChapterAndSubSectionListView

router = DefaultRouter()

router.register('', ChapterAndSubSectionListView, basename='forum')

urlpatterns = router.urls
