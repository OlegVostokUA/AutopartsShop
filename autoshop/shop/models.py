from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', db_index=True)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=100, unique=True, null=False)
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)

    class Meta:
        ordering = ('name',)
        unique_together = (['slug', 'parent'])
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' > '.join(full_path[::-1])

    def get_absolute_url(self):
        return reverse('shop:component_list_by_category', args=[self.slug])


class Component(models.Model):
    CURRENCY_CHOICES = (
        ('UAH', 'UAH'),
        ('$', '$'),
        ('€', '€'),
    )

    tags = TaggableManager()

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='components')
    name = models.CharField(max_length=255, verbose_name='Название')
    brand = models.CharField(max_length=245, verbose_name='Бренд')
    serial_number = models.CharField(max_length=100, blank=True, default='N/A', verbose_name='Номер детали')
    description = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=255)
    price = models.DecimalField(verbose_name='Цена', max_digits=7, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default='UAH')
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'

    def __str__(self):
        return self.name

    def get_image(self):
        queryset = ComponentPhoto.objects.filter(component=self)[:1][0]
        query = queryset.image.url
        return query

    def get_absolute_url(self):
        return reverse('shop:component_detail', args=[self.id, self.slug])


class ComponentPhoto(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    image = models.ImageField(verbose_name='Изображение', upload_to='component/components/%Y/%m/%d')
    component = models.ForeignKey(Component, verbose_name='Деталь', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото детали'
        verbose_name_plural = 'Фото детали'
