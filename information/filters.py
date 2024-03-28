from django_filters import FilterSet, NumberFilter, CharFilter, BooleanFilter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Submit
from django import forms
from information.models import (
    Scaffold, 
    Staff, 
    Company, 
    CompanyWorker,
    SubcontractorCompany,
    Subcontractor,
    Unit,
    Car,
    CarType)

class UnitFilter(FilterSet):
    """Be able to filter on Units in Scaffold List"""
    scaffold_number = NumberFilter(label='Ställning',
                                   lookup_expr='icontains') 
    class Meta:
        model = Scaffold
        fields = {
        'unit':['exact'], 
        }
        order_by = ('scaffold_number',)


class StaffFilter(FilterSet):
    """Be able to filter on staff firstname"""
    staff_firstname = CharFilter(label="Sök Anställd (förnamn)",
                                 lookup_expr='icontains')
    class Meta:
        model = Staff
        fields = ['staff_firstname']


class CompanyFilter(FilterSet):
    """Be able to filter on Company name"""
    company_name = CharFilter(label="Sök Företag",
                              lookup_expr='icontains')
    class Meta:
        model = Company
        fields = ['company_name']


class CompanyWorkerFilter(FilterSet):
    """Be able to filter on worker, and list filter Unit"""
    worker_firstname = CharFilter(label="Sök Förnamn",
                                  lookup_expr='icontains')
    worker_lastname = CharFilter(label="Sök Efternamn",
                                 lookup_expr='icontains')

    class Meta:
        model = CompanyWorker
        fields = ['worker_firstname', 'worker_lastname', 'worker_company', 'unit']


class SubcontractorCompanyFilter(FilterSet):
    """Be able to filter on UE company"""
    sub_company = CharFilter(label="Sök UE Företag",
                             lookup_expr='icontains')
    class Meta:
        model = SubcontractorCompany
        fields = ['sub_company']


class SubcontractorFilter(FilterSet):
    """Filter on Subcontractors, and units"""
    sub_firstname = CharFilter(label="Sök Förnamn",
                                  lookup_expr='icontains')
    sub_lastname = CharFilter(label="Sök Efternamn",
                                 lookup_expr='icontains')
    
    class Meta:
        model = Subcontractor
        fields = ['sub_firstname', 'sub_lastname','sub_company']
    

class UnitListFilter(FilterSet):
    """Filter on Units"""
    unit = CharFilter(label="Enhet",
                      lookup_expr='icontains')

    class Meta:
        model = Unit
        fields = ['unit']

class CarFilter(FilterSet):
    """Filter on Reg nr and Unit"""
    car_regnr = CharFilter(label="Sök Reg Nr",
                        lookup_expr='icontains')
    
    
    class Meta:
        model = Car
        fields = ['car_regnr', 'car_type_name', 'unit',]


class CarTypeFilter(FilterSet):
    """Filter on CarType"""
    
    model = Car
    fields = ['car_type_name', 'car_name']