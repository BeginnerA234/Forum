from django.db import models

from backend import settings
from services.generate_slug import gen_slug


class Chapter(models.Model):
    """
    Раздел в котором будут создаваться темы.
    Создается с помощью админки
    """

    title = models.CharField(verbose_name='Раздел', max_length=125)

    slug = models.SlugField(verbose_name='Ссылка на раздел', max_length=200,
                            blank=True, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


class SubSection(models.Model):
    """
    Подраздел, в котором пользователи могут создавать темы.
    Создается с помощью админки
    """
    title = models.CharField(verbose_name='Подраздел', max_length=125)

    chapter = models.ForeignKey(Chapter, verbose_name='Раздел',
                                on_delete=models.PROTECT, related_name='chapter')

    slug = models.SlugField(verbose_name='Ссылка на подраздел', max_length=200,
                            blank=True, unique=True)

    class Meta:
        verbose_name = 'Подразел'
        verbose_name_plural = 'Подразделы'
        ordering = ['id']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


class Theme(models.Model):
    """
    Тема для обсуждения, которую создал пользователь
    """
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_theme',
                                on_delete=models.CASCADE, verbose_name='Пользователь создавший тему')

    sub_section = models.ForeignKey(SubSection, verbose_name='Подраздел, где находится тема',
                                    on_delete=models.PROTECT, related_name='subsection')

    title = models.CharField(verbose_name='Название темы', max_length=150)

    content = models.TextField(verbose_name='Текст к теме',
                               help_text='Комментарий превышает 5000 символов')

    slug = models.SlugField(verbose_name='Ссылка на тему', max_length=300,
                            blank=True, unique=True)

    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update = models.DateTimeField(verbose_name='Дата последнего обновления', auto_now=True)

    class Meta:
        ordering = ['update']
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Комментарий пользователя в теме
    """
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_comment',
                                on_delete=models.CASCADE, verbose_name='Владелец комментария')

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Комментарий пользователя',
                               help_text='Комментарий превышает 5000 символов')

    quote = models.ManyToManyField('self', verbose_name='Ссылки на цитаты комментарев',
                                   db_column='quote_id', symmetrical=False, blank=True,
                                   related_name='quote_comments')

    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update = models.DateTimeField(verbose_name='Дата последнего обновления', auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.creator.username
