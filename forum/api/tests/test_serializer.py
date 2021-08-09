from django.test import TestCase

from forum.api.serializers import ChapterAndSubSectionSerializer
from forum.models import Chapter, SubSection


class ChapterSerializerTestCase(TestCase):

    def setUp(self):
        self.chapter_1 = Chapter.objects.create(title='Основной раздел')
        self.chapter_2 = Chapter.objects.create(title='Разное')
        SubSection.objects.create(chapter=self.chapter_1, title='Общие вопросы и обсуждения')
        SubSection.objects.create(chapter=self.chapter_1, title='Рейтинговая система и статистика')
        SubSection.objects.create(chapter=self.chapter_1, title='Герои: общие обсуждения')
        SubSection.objects.create(chapter=self.chapter_2, title='Таверна')
        SubSection.objects.create(chapter=self.chapter_2, title='Музыка')

    def test_ok(self):
        queryset = Chapter.objects.all().prefetch_related('chapter').order_by('id')
        data = ChapterAndSubSectionSerializer(queryset, many=True).data

        chp1_section1, chp1_section2, chp1_section3 = list(self.chapter_1.chapter.all())
        chp2_section1, chp2_section2 = list(self.chapter_2.chapter.all())

        expected_data = [
            {
                'id': self.chapter_1.id,
                'title': self.chapter_1.title,
                'slug': self.chapter_1.slug,
                'chapter': [
                    {
                        'id': chp1_section1.id,
                        'title': chp1_section1.title,
                        'slug': chp1_section1.slug,
                    },
                    {
                        'id': chp1_section2.id,
                        'title': chp1_section2.title,
                        'slug': chp1_section2.slug,
                    },
                    {
                        'id': chp1_section3.id,
                        'title': chp1_section3.title,
                        'slug': chp1_section3.slug,
                    },
                ]
            },
            {
                'id': self.chapter_2.id,
                'title': self.chapter_2.title,
                'slug': self.chapter_2.slug,
                'chapter': [
                    {
                        'id': chp2_section1.id,
                        'title': chp2_section1.title,
                        'slug': chp2_section1.slug,
                    },
                    {
                        'id': chp2_section2.id,
                        'title': chp2_section2.title,
                        'slug': chp2_section2.slug,
                    },

                ]
            },
        ]
        self.assertEqual(expected_data, data)
