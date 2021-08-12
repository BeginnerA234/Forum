from rest_framework import serializers

from custom_user.api.serializers import UserFieldSerializer
from forum.models import Chapter, SubSection, Theme


class SubSectionSerializer(serializers.ModelSerializer):
    """
    Сериализатор подразделов
    """

    class Meta:
        model = SubSection
        fields = (
            'id',
            'title',
            'slug',
        )


class ChapterSerializer(serializers.ModelSerializer):
    """
    Сериализатор разделов c подразделами
    """

    sub_sections = SubSectionSerializer(source='chapter', read_only=True, many=True)

    class Meta:
        model = Chapter
        fields = (
            'id',
            'title',
            'slug',
            'sub_sections'
        )


class ThemeSerializer(serializers.ModelSerializer):
    creator = UserFieldSerializer(read_only=True)
    last_comment = serializers.SerializerMethodField(read_only=True)
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Theme
        fields = (
            'id',
            'creator',
            'title',
            'slug',
            'created',
            'comment_count',
            'last_comment'
        )

    @staticmethod
    def get_last_comment(instance):
        return instance.comment_set.values('creator', 'update').last()
