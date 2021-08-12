from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from forum.api.serializers import ChapterSerializer, ThemeSerializer
from forum.models import Chapter, Theme


class ChapterViewSet(ModelViewSet):
    """
    Вьюха разделов и подразделов
    """
    queryset = Chapter.objects.all().prefetch_related('chapter').order_by('id')
    serializer_class = ChapterSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    @action(detail=False, methods=['GET'])
    def sub_section(self, request, slug):
        """
        Подраздел с темами
        PS: ДА КАК ЭТОТ ПРЕФЕТЧ РАБОТАЕТ N+1 ЗАПРОС!!!!!!!!!!!!!!!!!!!!!1
        """
        queryset = Theme.objects.filter(sub_section__slug=slug).annotate(
            comment_count=Count('comment'),
        ).select_related('creator').prefetch_related('comment_set').order_by('update')

        serializer = ThemeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
