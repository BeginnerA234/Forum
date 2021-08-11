from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from forum.api.serializers import ChapterAndSubSectionSerializer
from forum.models import Chapter


class ChapterAndSubSectionListView(ModelViewSet):
    """
    Вьюха, которая выводит разделы и подразделы
    """
    queryset = Chapter.objects.all().prefetch_related('chapter').order_by('id')
    serializer_class = ChapterAndSubSectionSerializer


    @action(detail=True, methods=['GET'])
    def sub_section(self, request, pk=None):
        print(request)