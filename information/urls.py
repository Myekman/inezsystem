from django.urls import path
from . import views

app_name = 'information'

urlpatterns = [
     path("", views.index, name="index"),
     path("create/", views.ScaffoldCreate.as_view(), name="scaffold_create"),
     path("scaffold_list/", views.scaffold_list, name="scaffold_list"),
     path("scaffold_edit/<int:pk>", views.ScaffoldEdit.as_view(),
          name="scaffold_edit"),
     path("staff_create/", views.StaffCreate.as_view(), name="staff_create"),
     path("staff_edit/<int:pk>/", views.StaffEdit.as_view(), name="staff_edit"),
     path("staff_list/", views.staff_list, name="staff_list"),
     path("company_create/", views.CompanyCreate.as_view(), name="company_create"),
     path("company_edit/<int:pk>/", views.CompanyEdit.as_view(), name="company_edit"),
     path("company_list/", views.company_list, name="company_list"),
     path("companyworker_create/", views.CompanyWorkerCreate.as_view(),
          name="companyworker_create"),
     path("companyworker_edit/<int:pk>/", views.CompanyWorkerEdit.as_view(),
          name="companyworker_edit"),
     path("companyworker_list/", views.companyworker_list,
          name="companyworker_list"),
     path("ue_company_create/", views.UeCompanyCreate.as_view(),
          name="ue_company_create"),
     path("ue_company_edit/<int:pk>/", views.UeCompanyEdit.as_view(),
          name="ue_company_edit"),
     path("ue_company_list", views.uecompany_list, name="ue_company_list"),
     path("ue_user_create/", views.UeUserCreate.as_view(),
          name="ue_user_create"),
     path("ue_user_edit/<int:pk>/", views.UeUserEdit.as_view(),
          name="ue_user_edit"),
     path("ue_user_list", views.ueuser_list, name="ue_user_list"),
     path("unit_create/", views.UnitCreate.as_view(), 
          name="unit_create"),
     path("unit_edit/<int:pk>/", views.UnitEdit.as_view(),
          name="unit_edit"),
     path("unit_list/", views.unit_list, name="unit_list"),
     path("car_type_create/", views.CarTypeCreate.as_view(),
          name="car_type_create"),
     path("car_type_edit/<int:pk>/", views.CarTypeEdit.as_view(),
          name="car_type_edit"),
     path("car_type_list/", views.car_type_list, name="car_type_list"),
     path("car_create", views.CarCreate.as_view(),
          name="car_create"),
     path("car_edit/<int:pk>/", views.CarEdit.as_view(),
          name="car_edit"),
     path("car_list/", views.car_list, name="car_list"),


     # TEST PATHS
    
]

