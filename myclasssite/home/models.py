from django.db import models

# Create your models here.


class User_account(models.Model):
    class Meta:
        ordering = ["user_name"]
        verbose_name_plural = "account(for login)"
    user_name = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user_name} 的帳號"


class User_profile(models.Model):
    class Meta:
        ordering = ["user"]
        verbose_name_plural = "account(for information)"
    user = models.OneToOneField(
        User_account,
        on_delete=models.CASCADE,
        primary_key=True)
    nick_name = models.TextField(blank=True, max_length=2)
    position = models.TextField(blank=True, max_length=10)
    self_introduction = models.TextField(blank=True, max_length=200)

    def __str__(self):
        return f"{self.user}資料"
