from django.contrib import admin
from .models import (
    Unit,
    CompanyWorker,
    Company,
    WorkPerformed,
    Scaffold,
    ScaffoldType,
    Staff,
    Subcontractor,
    SubcontractorCompany,
    Car,
    CarType)
# Register your models here.

class ScaffoldAdmin(admin.ModelAdmin):
    list_display = ['scaffold_number', 'unit', 'day_created']

admin.site.register(Unit)
admin.site.register(CompanyWorker)
admin.site.register(Company)
admin.site.register(WorkPerformed)
admin.site.register(Scaffold, ScaffoldAdmin)
admin.site.register(ScaffoldType)
admin.site.register(Staff)
admin.site.register(Subcontractor)
admin.site.register(SubcontractorCompany)
admin.site.register(Car)
admin.site.register(CarType)