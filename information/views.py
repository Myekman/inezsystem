from django.shortcuts import render
from django.urls import reverse_lazy
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
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Sum
from information.filters import (
    UnitFilter, 
    StaffFilter, 
    CompanyFilter,
    CompanyWorkerFilter,
    SubcontractorCompanyFilter,
    SubcontractorFilter,
    UnitListFilter,
    CarFilter,
    CarTypeFilter)
from django import forms

# Create your views here.


def index(request):
    """Index page"""
    return render(request, 'information/index.html')

# SECTION 1 - GENERAL INFROMATION

# SECTION 1 - UNITS
def unit_list(request):
    """List of all Units"""
    unitlist_filter = UnitListFilter(request.GET, queryset=Unit.objects.order_by('unit'))
    units = unitlist_filter.qs

    # COUNT UNITS
    unit_count = units.count()
    return render(request, 'information/unit_list.html',{
        'form':unitlist_filter.form,
        'units':units,
        'unit_count':unit_count,
    })

class UnitCreate(CreateView):
    """Create Unit"""
    model = Unit
    template_name = 'information/unit_create.html'
    fields = '__all__'
    success_url = reverse_lazy('information:unit_list')

class UnitEdit(UpdateView):
    """Update Unit"""
    model = Unit
    template_name = 'information/unit_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('information:unit_list')


# SECTION1.2 - COMPANIES
def company_list(request):
    """Company list"""
    company_filter = CompanyFilter(request.GET,
                              queryset=Company.objects.order_by('company_name'))
    companies = company_filter.qs
    # COUNT ANATAL COMPANIES
    company_count = companies.count()
    return render(request, 'information/company_list.html',{
        'form':company_filter.form,
        'companies':companies,
        'company_count':company_count,
    })

class CompanyCreate(CreateView):
    """Create Company"""
    model = Company
    template_name = 'information/company_create.html'
    fields = '__all__'
    success_url = reverse_lazy('information:company_list')

class CompanyEdit(UpdateView):
    """Edit a Company"""
    model = Company
    template_name = 'information/company_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('information:company_list')


# SECTION 1.2 - COMPANY WORKERS
def companyworker_list(request):
    """Companyworker (beställare) list"""
    companyworker_filter = CompanyWorkerFilter(request.GET,
                    queryset=CompanyWorker.objects.order_by('worker_firstname'))
    companyworkers = companyworker_filter.qs

    #COUNT COMPANYWORKERS
    worker_count = companyworkers.count()

    return render(request, 'information/companyworker_list.html',{
        'form':companyworker_filter.form,
        'companyworkers':companyworkers,
        'worker_count':worker_count,
    })

class CompanyWorkerCreate(CreateView):
    """Create Companyworker"""
    model = CompanyWorker
    template_name = 'information/companyworker_create.html'
    fields = '__all__'
    success_url = reverse_lazy('information:companyworker_list')

class CompanyWorkerEdit(UpdateView):
    """Edit a Companyworker"""
    model = CompanyWorker
    template_name = 'information/companyworker_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('information:companyworker_list')



# SECTION 2 - SCAFFOLDINGS
def scaffold_list(request):
    """Scaffold list"""
    unit_filter = UnitFilter(request.GET, 
                             queryset=Scaffold.objects.order_by('scaffold_number'))
    scaffolds = unit_filter.qs

    # SUM OF SCAFFOLD_CUBIC
    cubic_sum = scaffolds.aggregate(cubic_total=Sum('scaffold_cubic'))['cubic_total'] or 0
    # SUM OF SCAFFOLD_STAIR
    stair_sum = scaffolds.aggregate(stair_total=Sum('scaffold_stair'))['stair_total'] or 0
    # COUNT OF SCAFFOLDS
    scaffold_count = scaffolds.count()


    return render(request, 'information/scaffold_list.html',{
        'form': unit_filter.form,
        'scaffolds':unit_filter.qs,
        'scaffold_count':scaffold_count,
        'cubic_sum':cubic_sum,
        'stair_sum':stair_sum,
    })

class ScaffoldCreate(CreateView):
    """Only to create a scaffold"""
    model = Scaffold
    template_name = "information/scaffold_create.html"
    fields = ['scaffold_number','scaffold_location','scaffold_for','unit']
    success_url = reverse_lazy('information:scaffold_list')

class ScaffoldEdit(UpdateView):
    """Edit the Scaffold"""
    model = Scaffold
    template_name = 'information/scaffold_edit.html'
    fields = "__all__"
    success_url = reverse_lazy('information:scaffold_list')

# SECTION 3 - STAFF / SUBCONTRACTORS / SUBCOMPANY

# SECTION 3.1 - OUR OWN STAFF
def staff_list(request):
    """Staff list"""
    staff_filter = StaffFilter(request.GET, queryset=Staff.objects.order_by('staff_firstname'))
    staffs = staff_filter.qs
    # STAFF COUNT
    staff_count = staffs.count()
    return render(request, 'information/staff_list.html',{
        'form':staff_filter.form,
        'staffs':staffs,
        'staff_count': staff_count,
    })

class StaffCreate(CreateView):
    """To add a new Staff member"""
    model = Staff
    template_name = 'information/staff_create.html'
    fields = '__all__'
    success_url = reverse_lazy('information:staff_list')

class StaffEdit(UpdateView):
    """Edit Staff member"""
    model = Staff
    template_name = 'information/staff_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('information:staff_list')

# SECTION 3.2 - SUBCOMPANIES

def uecompany_list(request):
    """UE Company list"""
    ue_filter = SubcontractorCompanyFilter(request.GET, 
                                           queryset=SubcontractorCompany.objects.order_by('sub_company'))
    ue_company = ue_filter.qs

    # UE COMPANY COUNT
    ue_count = ue_company.count()
    return render(request, 'information/ue_company_list.html', {
        'form':ue_filter.form,
        'ue_company':ue_company,
        'ue_count':ue_count,
    })
    
class UeCompanyCreate(CreateView):
    """To add new UE Companies"""
    model = SubcontractorCompany
    template_name = 'information/ue_company_create.html'
    fields = '__all__'
    success_url = reverse_lazy('information:ue_company_list')

class UeCompanyEdit(UpdateView):
    """Update UE Company"""
    model = SubcontractorCompany
    template_name = 'information/ue_company_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('information:ue_company_list')

# SECTION 3.3 - SUBCONTRACTORS (UE USERS)
    
def ueuser_list(request):
    """Subcontractor list"""
    subcontractor_filter = SubcontractorFilter(request.GET,
                            queryset=Subcontractor.objects.order_by('sub_firstname'))
    subcontractor = subcontractor_filter.qs

    # COUNT SUBCONTRACTORS
    ue_user_count = subcontractor.count()
    return render(request, 'information/ue_user_list.html',{
        'form':subcontractor_filter.form,
        'subcontractor':subcontractor,
        'ue_user_count':ue_user_count,
    })

class UeUserCreate(CreateView):
    """Create Subcontractor"""
    model = Subcontractor
    fields = '__all__'
    template_name = 'information/ue_user_create.html'
    success_url = reverse_lazy('information:ue_user_list')

class UeUserEdit(UpdateView):
    """Update Subcontractor"""
    model = Subcontractor
    fields = '__all__'
    template_name = 'information/ue_user_edit.html'
    success_url = reverse_lazy('information:ue_user_list')



# SECTION 4 - CARS

# SECTION 4.1 - CARTYPE
def car_type_list(request):
    """List of Car Types"""
    car_types_filter = CarTypeFilter(request.GET,
                                     queryset=CarType.objects.order_by('car_type_name'))
    car_types = car_types_filter.qs

    # COUNT CAR TYPES
    car_count = car_types.count()
    return render(request, 'information/car_type_list.html',{
        'form':car_types_filter.form,
        'car_types':car_types,
        'car_count':car_count,
    })
    

class CarTypeCreate(CreateView):
    """Create a Car Type"""
    model = CarType
    fields = '__all__'
    template_name = 'information/car_type_create.html'
    success_url = reverse_lazy('information:car_type_list')

class CarTypeEdit(UpdateView):
    """Update Car Type"""
    model = CarType
    fields = '__all__'
    template_name = 'information/car_type_edit.html'
    success_url = reverse_lazy('information:car_type_list')

# SECTION 4.2 - CAR
def car_list(request):
    """List of Active / Not Active Cars"""
    car_filter = CarFilter(request.GET, queryset=Car.objects.order_by('car_regnr'))
    cars = car_filter.qs

    # COUNT OF CARS
    car_not_active_count = cars.filter(car_active=False).count()
    car_active_count = cars.filter(car_active=True).count()
    return render(request, 'information/car_list.html',{
        'form':car_filter.form,
        'cars':cars,
        'car_active_count':car_active_count,
        'car_not_active_count':car_not_active_count,
    })
    

class CarCreate(CreateView):
    """Create a Car"""
    model = Car
    fields = '__all__'
    template_name = 'information/car_create.html'
    success_url = reverse_lazy('information:car_list')

class CarEdit(UpdateView):
    """Update a Car"""
    model = Car
    fields = '__all__'
    template_name = 'information/car_edit.html'
    success_url = reverse_lazy('information:car_list')




# TEST SECTION!!!!!!!!!
    
