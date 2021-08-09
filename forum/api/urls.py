from rest_framework.routers import DefaultRouter

from forum.api.views import ChapterAndSubSectionListView, CreateThemeView

router = DefaultRouter()

router.register('', ChapterAndSubSectionListView, basename='forum')
router.register('create', CreateThemeView, basename='create')

urlpatterns = router.urls
