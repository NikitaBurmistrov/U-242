
from django.db import models


class Student(models.Model):
    familia = models.CharField(max_length=50, verbose_name="фамилия")
    imy = models.CharField(max_length=50, verbose_name="имя")
    otchestvo = models.CharField(max_length=50, verbose_name="Отчество")


    birth_years = models.IntegerField(verbose_name="год рождения")


    group_number = models.CharField(max_length=10, verbose_name="номер группы")


    def __str__(self):
        return f"{self.familia} {self.imy} ({self.group_number})"