from rest_framework import mixins

from rest_framework import viewsets

from forum.api.permissions import IsOwnerNotBlockedOrStaff
from forum.api.serializers import ChapterAndSubSectionSerializer, CreateThemeSerializer
from forum.models import Chapter, Theme


class ChapterAndSubSectionListView(mixins.ListModelMixin,
                                   viewsets.GenericViewSet):
    queryset = Chapter.objects.all().prefetch_related('chapter').order_by('id')
    serializer_class = ChapterAndSubSectionSerializer


class CreateThemeView(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Theme.objects.all()
    serializer_class = CreateThemeSerializer
    permission_classes = [IsOwnerNotBlockedOrStaff,]
