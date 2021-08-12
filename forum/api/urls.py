from django.urls import path

from forum.api.views import ChapterViewSet


chapter_list = ChapterViewSet.as_view({
    'get': 'list'
})

chapter_detail = ChapterViewSet.as_view({
    'get': 'retrieve'
})

chapter_subsection = ChapterViewSet.as_view({
    'get': 'sub_section'
})


urlpatterns = [
    path('', chapter_list, name='chapter-list'),
    path('chapter/<slug>', chapter_detail, name='chapter-detail'),
    path('subsection/<slug>', chapter_subsection, name='subsection'),
]
