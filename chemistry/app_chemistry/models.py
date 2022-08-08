from tkinter import CASCADE
from django.db import models

# Create your models here.

class Period(models.Model):
    name = models.CharField(
        max_length=2,
        default=None
    )
    number = models.SmallIntegerField(
        null = False
    )

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(
        max_length=2,
        default=None
    )
    number = models.SmallIntegerField(
        null = False
    )

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(
        max_length = 128,
        null = False,
        blank = True
    )

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(
        max_length = 128,
        null = False,
        blank = True
    )

    def __str__(self):
        return self.name

class Value(models.Model):
    name = models.CharField(
        max_length=2,
        default=None
    )
    value = models.SmallIntegerField(
        null = False,
    )

    def __str__(self):
        return self.name

class Block(models.Model):
    name = models.CharField(
        max_length = 8,
        null = False,
        blank = True
    )

    def __str__(self):
        return self.name

class Elements(models.Model):
    name = models.CharField(
        verbose_name='Nazwa',
        max_length = 128,
        blank = True,
        null = False
    )
    symbol = models.CharField(
        verbose_name = 'Symbol',
        max_length = 8,
        blank = True,
        null = False
    )
    atomic_number = models.SmallIntegerField(
        verbose_name='Liczba atomowa',
        null = False
    )
    atomic_weight = models.FloatField(
        default = 1.0,
        verbose_name='Masa atomowa',
        null = False,
        blank = True
    )
    period = models.ForeignKey(
        Period,
        verbose_name='Okres',
        on_delete = models.CASCADE
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Grupa',
        on_delete = models.CASCADE
    )
    block = models.ForeignKey(
        Block,
        verbose_name="Blok",
        on_delete=models.CASCADE
    )
    character = models.ForeignKey(
        Character,
        verbose_name='Charakter chemiczny',
        blank=True,
        on_delete = models.CASCADE
    )
    state = models.ForeignKey(
        State,
        verbose_name='Stan skupienia',
        on_delete = models.CASCADE
    )
    value = models.CharField(
        max_length=32,
        null=False,
        blank=True,
    )
    electro_negativity = models.FloatField(
        verbose_name='Elektroujemność',
        default = 1.0,
        null = True,
        blank=True
    )
    atomic_radius = models.CharField(
        verbose_name='Promień atomu',
        max_length = 64,
        blank = True
    )
    year = models.IntegerField(
        verbose_name='Rok odkrycia',
        null=True,
        blank = True
    )
    melting_temp = models.FloatField(
        verbose_name='Temperatura topnienia',
        null = True,
        blank = True
    )
    boiling_temp = models.FloatField(
        verbose_name='Temperatura wrzenia',
        null = True,
        blank = True
    )
    is_lanthanides = models.BooleanField(
        default=False
    )
    is_actinides = models.BooleanField(
        default=False
    )
    def __str__(self):
        return self.name
