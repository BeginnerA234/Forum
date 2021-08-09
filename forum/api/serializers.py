from rest_framework import serializers

from forum.models import Chapter, SubSection, Theme, Comment


class SubSectionSerializer(serializers.ModelSerializer):
    """
    Сериализатор подразделов для просмотра.
    Создавать имеет право только администратор.
    """

    class Meta:
        model = SubSection
        fields = (
            'id',
            'title',
            'slug',
        )


class ChapterAndSubSectionSerializer(serializers.ModelSerializer):
    """
    Сериализатор разделов для просмотра.
    Создавать имеет право только администратор.
    """

    chapter = SubSectionSerializer(read_only=True, many=True)

    class Meta:
        model = Chapter
        fields = (
            'id',
            'title',
            'slug',
            'chapter'
        )


class CreateThemeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания тем.
    Создавать имеет право активный пользователь (не в бане).
    """

    class Meta:
        model = Theme
        fields = (
            'creator',
            'sub_section',
            'title',
            'content',
        )


class ThemeSerializer(serializers.ModelSerializer):
    """
    Сериализатор тем с выводом связанных комментариев
    """

    class Meta:
        model = Theme
        fields = (
            'creator',
            'sub_section',
            'title',
            'content',
        )


class CreateCommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор создания комментариев.
    Комментарии можно оставлять только в темах.
    Реализованно цитирование множества других комментариев
    """

    class Meta:
        model = Comment
        fields = (
            'creator',
            'theme',
            'comment',
            'quote',  # возможность цитирования
        )
