from django.db import models


class News(models.Model):
    name = models.CharField('Имя', max_length=150)
    content = models.TextField('Контент', blank=True)
    likes = models.IntegerField()
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    category = models.ManyToManyField(
        'Category',
        verbose_name='Категория',
        related_name='news',
    )
    origin = models.ForeignKey(
        'Origin',
        on_delete=models.PROTECT,
        verbose_name='Источник',
        related_name='news',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    name = models.CharField('Имя категории', max_length=150, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Origin(models.Model):
    name = models.CharField('Имя источника', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'
        ordering = ['name']


class OrderedContent(News):

    class Meta:
        proxy = True
        ordering = ['-created_at']
