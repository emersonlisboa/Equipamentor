from django.db import models
from django.utils import timezone
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

import uuid # Required for unique book instances

class Local(models.Model):
    name = models.CharField(max_length=200)
    createdAt =  models.DateField(auto_now_add=True)
    list_display = ('id', 'name', 'createdAt', 'country' )
  
    LOAN_STATUS = (
        ('a', 'Ativo'),
        ('i', 'Inativo'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
 
    )
    
    class Meta:
       ordering = ['name']
       verbose_name = 'Local'
       verbose_name_plural = 'Local'
    
    def __str__(self):
        return f'{self.name}'

class Factory(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    createdAt =  models.DateField(auto_now_add=True)
    list_display = ('id', 'name', 'createdAt', 'country' )
  
    LOAN_STATUS = (
        ('a', 'Ativo'),
        ('i', 'Inativo'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
 
    )
    
    class Meta:
       ordering = ['name', 'country']
       verbose_name = 'Fabricante'
       verbose_name_plural = 'Fabricante'
    
    def __str__(self):
        return f'{self.name}'

    """Uma típica classe definindo um modelo, derivada da classe Model."""

class Equipment(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    sn = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200 )
    image = models.ImageField(max_length=100, null=True,  blank=True)
    fabricante = models.ForeignKey('Factory', on_delete=models.SET_NULL, null=True)
    local = models.ForeignKey('Local',on_delete=models.SET_NULL, null=True )
    LOAN_STATUS = (
        ('a', 'Ativo'),
        ('i', 'Inativo'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Equipamento availability',
    )
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.modelo}'
    class Meta:
       verbose_name = 'Equipamento'
       verbose_name_plural = 'Equipamento'


class Corporation(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    createdAt =  models.DateField(auto_now_add=True)
    list_display = ('id', 'name', 'createdAt', 'country' )
    local = models.ManyToManyField(Local)
    class Meta:
       ordering = ['name', 'country']
       verbose_name_plural = 'Corporação'
    def __str__(self):
        return f'{self.name}'

class Activities(models.Model):
    name = models.CharField(max_length=200)
    time = models.IntegerField( help_text='Tempo em (min)',)
    createdAt =  models.DateField(auto_now_add=True)
    list_display = ('id', 'name', 'createdAt', 'time' )
    class Meta:
       ordering = ['name', 'time']
    LOAN_STATUS = (
        ('a', 'Ativo'),
        ('i', 'Inativo'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Equipamento availability',
    )

    class Meta:
       verbose_name_plural = 'Atividades'

    def __str__(self):
        return f'{self.name}'

class Departament(models.Model):
    name = models.CharField(max_length=200)
    createdAt =  models.DateField(auto_now_add=True)
    
    LOAN_STATUS = (
        ('a', 'Ativo'),
        ('i', 'Inativo'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
 
    )
    class Meta:
       ordering = ['name']
       verbose_name = 'Departamento'
       verbose_name_plural = 'Departamento'
    
    def __str__(self):
        return f'{self.name}'

class Employeer(models.Model):
    name = models.CharField(max_length=200)
    createdAt =  models.DateField(auto_now_add=True)
    registerNumber = models.BigIntegerField()
    departament = models.ForeignKey('Departament', on_delete=models.SET_NULL, null=True)
 
    LOAN_STATUS = (
        ('a', 'Ativo'),
        ('i', 'Inativo'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
 
    )

    CARGO = (
        ('t', 'Técnico SMT'),
        ('e', 'Engenheiro SMT'),
    )
    cargo = models.CharField(
        max_length=1,
        choices=CARGO,
        blank=True,
        default='t',
 
    )
    
    class Meta:
       ordering = ['name']
       verbose_name = 'Colaborador'
       verbose_name_plural = 'Colaborador'
    def __str__(self):
        return f'{self.name}'

class MaintenanceType(models.Model):
    name = models.CharField(max_length=200)
    value = models.IntegerField()
    createdAt =  models.DateField(auto_now_add=True)

    TYPE_CHOICES = (
        ('p', 'Percurso'),
        ('h', 'Horímetro'),
        ('d', 'Dia'),
        ('c', 'Ciclo'),

    )
    typeMain = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        blank=True,
        default='d',
 
    )
   
    class Meta:
       ordering = ['name', 'typeMain', 'value']
       verbose_name_plural = 'Tipos de Manutenção'
    def __str__(self):
        return f'{self.name}'


class WorkOrder(models.Model):
    equipment = models.ForeignKey('Equipment', on_delete=models.SET_NULL, null=True)
    planDate = models.DateField(default= timezone.now())
    executedDate = models.DateField(blank = True, null=True)
    employeer = models.ForeignKey('Employeer', on_delete=models.SET_NULL, null=True)
    createdAt =  models.DateField(auto_now_add=True)

    TYPE_CHOICES = (
        ('p', 'Planejado'),
        ('e', 'Executado'),
        ('a', 'Atrasado'),
    )
    status = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        blank=True,
        default='p',
    )
    class Meta:
       ordering = ['equipment', 'planDate', 'executedDate', 'status']
       verbose_name_plural = 'Order de Serviço'
    def __str__(self):
        return f'{self.equipment}'