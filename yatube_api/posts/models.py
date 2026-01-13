from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import TITLE_LEN, LETTER_LIMIT

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Слаг"
    )
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title[:TITLE_LEN]


class Post(models.Model):
    text = models.TextField(verbose_name="Текст поста")
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name="Заголовок"
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name="Изображение"
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Группа"
    )

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return self.text[:TITLE_LEN]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name="Автора"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        verbose_name="Пост"
    )
    text = models.TextField(verbose_name="Текст комментария")
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Дата добавления"
    )

    class Meta:
        default_related_name = 'comments'

    def __str__(self):
        return f'Комментарий {self.author.username} к посту {
            self.post.id}, текст: {self.text[:LETTER_LIMIT]}'
