from django.db import models


class Record(models.Model):
    heading = models.CharField(verbose_name='заголовок', max_length=100)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(verbose_name='превью', null=True, blank=True)
    date_of_creation = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    sign_of_publication = models.BooleanField(verbose_name='признак публикации', default=False)
    number_of_views = models.IntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return f"{self.heading}"

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
