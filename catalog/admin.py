from django.contrib import admin
from catalog.models import Equipment, Corporation, Factory, Activities, Local, Employeer, Departament, MaintenanceType, WorkOrder


# Adiciona colunas na view de admin
class CorporationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','createdAt', 'country')
    fields = [ 'name', 'local', 'country']
    list_filter = ('name', 'local', 'country')

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id','local' , 'sn','tag', 'modelo', 'fabricante' , 'status',  'image')
    fields = [ 'sn','tag', 'modelo', 'fabricante' , 'status','local', 'image']
    list_filter = ('status','local', 'modelo', 'fabricante')

class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country',  'createdAt', 'status')
    fields = [ 'name', 'country', 'status']
    list_filter = ('status','country')
    def __str__(self):
        return f'name'

class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time',  'createdAt', 'status')
    fields = [ 'name', 'time']
    list_filter = ('status', 'name')

class LocalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'createdAt', 'status')
    fields = [ 'name', 'status']
    list_filter = ('status', 'name')  

class EmployeerAdmin(admin.ModelAdmin):
    list_display = ('id', 'registerNumber','name', 'cargo', 'departament','createdAt',  'status')
    fields = [ 'name', 'registerNumber', 'cargo', 'departament','status']
    list_filter = ('cargo', 'status', 'departament')

class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'createdAt', 'status')
    fields = [ 'name', 'status']
    list_filter = ('name',  'status')

class MaintenanceTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'createdAt', 'value', 'typeMain')
    fields = [ 'name', 'value', 'typeMain']

class WorkOrderTypeAdmin(admin.ModelAdmin):
    list_display = ('id','equipment', 'planDate', 'executedDate', 'employeer', 'createdAt','status')
    fields = [ 'equipment', 'planDate', 'executedDate', 'employeer','status']
    list_filter = ('equipment', 'planDate', 'executedDate', 'employeer','status')

 


admin.site.register(Corporation, CorporationAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Factory, FactoryAdmin)
admin.site.register(Activities, ActivitiesAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(Employeer, EmployeerAdmin)
admin.site.register(Departament, DepartamentAdmin)
admin.site.register(MaintenanceType, MaintenanceTypeAdmin)
admin.site.register(WorkOrder, WorkOrderTypeAdmin)