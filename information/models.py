from django.db import models
# from djmoney.models.fields import MoneyField
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

# SECTION 1: GENERAL INFORMATION - 
class Unit(models.Model):
    """
    This is the main connection to the project.
    Units are connected to scaffolds, workers,
    companies, economy, cars, staff etc.
    """
    unit = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.unit
    

class Company(models.Model):
    """
    Model for companies that store information about it.
    """
    company_name = models.CharField(max_length=100,
                                    verbose_name="Företagsnamn nisse")
    company_invoice_address = models.CharField(max_length=300,
                                    verbose_name="Fakturaadress")
    company_org_nr = models.CharField(max_length=100,
                                      verbose_name="Organisations nummer")
    company_phone_number = models.CharField(max_length=100,
                                            verbose_name="Telefonnummer")
    company_postal_number = models.CharField(max_length=20,
                                             verbose_name="Postkod")
    company_city = models.CharField(max_length=100,
                                    verbose_name="Stad")

    def __str__(self):
        return self.company_name
    
class CompanyWorker(models.Model):
    """
    Model for the worker associated with the company.
    This person can be at more than one unit.
    """
    worker_firstname = models.CharField(max_length=100,
                                        verbose_name="Beställare Förnamn")
    worker_lastname = models.CharField(max_length=100,
                                       verbose_name="Beställare Efternamn")
    worker_company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                       verbose_name="Beställare Företag")
    worker_email = models.EmailField(null=True,
                                     verbose_name="Beställare mail")
    unit = models.ManyToManyField(Unit, default=None,
                                  verbose_name="Enheter")

    def __str__(self):
        return f"{self.worker_firstname} {self.worker_lastname}"
    
# SECTION 2: SCAFFOLDING INFORMATION - 
    
# CHOICES FOR TYPES OF WORK DONE ON SCAFFOLD
WORK_CHOICES = WORK_TYPE_CHOICES = (
    ('montering', 'Montering'),
    ('deldemontering', 'Deldemontering'),
    ('ändring', 'Ändring'),
    ('slutdemontering', 'Slutdemontering'),
    ('komplettering', 'Komplettering'),
    ('ombesiktning', 'Ombesiktning'),
)

class WorkPerformed(models.Model):
    """
    Generate options from the list work_choices
    """
    work_performed = models.CharField(max_length=100, choices=WORK_CHOICES)


class ScaffoldType(models.Model):
    """
    Model to set the scaffold type. Default is False (which means
    the scaffold is not a price job.)
    """
    is_price = models.BooleanField(default=False)
    # work_price = MoneyField(max_digits=19, decimal_places=4, 
    #                         default_currency='SEK')
    # work_rent = MoneyField(max_digits=19, decimal_places=4,
    #                        default_currency='SEK')
    work_comment = models.CharField(max_length=300, default=None)

def validate_positive_or_zero(value):
    """Validate so you can't add negative number to cubic/stair m"""
    if value < 0:
        raise ValidationError("Ställnings kubik kan inte vara negativt")
    
class Scaffold(models.Model):
    """
    Model for scaffolding information and connections to above.
    Scaffolding numbers are unique within a unit, but can have the same
    number when not in the same unit.
    """
    scaffold_number = models.IntegerField(verbose_name="Ställnings nummer")
    scaffold_location = models.CharField(max_length=200,
                                         verbose_name="Plats")
    scaffold_for = models.CharField(max_length=200,
                                    verbose_name="Ställning för")
    scaffold_marking = models.CharField(max_length=200, blank=True,
                                        verbose_name="Märkning")
    scaffold_po = models.CharField(max_length=200, blank=True,
                                   verbose_name="Inköpsordernummer")
    scaffold_cubic = models.IntegerField(default=0, blank=True,
                                         validators=[validate_positive_or_zero],
                                         verbose_name="Kubik")
    scaffold_stair = models.IntegerField(default=0, blank=True,
                                         validators=[validate_positive_or_zero],
                                         verbose_name="Trappmeter")
    scaffold_material = models.BooleanField(default=False,
                                            verbose_name="Ställnings material")
    day_created = models.DateTimeField(auto_now_add=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE,
                             verbose_name="Enhet")
    # FIX SCAFFOLDTYPE CONNECTION - 
    class Meta:
        """Ensures uniqueness with scaffold numbers connected to
        a Unit."""
        unique_together = ('unit', 'scaffold_number')

    def __str__(self):
        return str(self.scaffold_number)



# SECTION 3 - OWN WORKERS (BOTH EMPLOYEES, AND SUBCONTRACTORS/SUBCOMPANY)
    
class Staff(models.Model):
    """
    Model for Highcon's own employees and information.
    """
    staff_firstname = models.CharField(max_length=50, verbose_name='Förnamn')
    staff_lastname = models.CharField(max_length=50,
                                      verbose_name='Efternamn')
    staff_email = models.EmailField(max_length=100, null=True,
                                    verbose_name='Email')
    staff_phonenumber = models.CharField(max_length=100, 
                                         verbose_name='Telefon')
    staff_id06 = models.CharField(max_length=100, null=True, blank=True,
                                  verbose_name='ID06')
    # staff_certificate = models.CharField ??
    # staff_authoraziation ?? 
    unit = models.ManyToManyField(Unit, blank=True, verbose_name='Enhet')

    def __str__(self):
        return f"{self.staff_firstname} {self.staff_lastname}"
    
class SubcontractorCompany(models.Model):
    """
    Model for Subcontractor Companies
    """
    sub_company = models.CharField(max_length=100, unique=True,
                                   verbose_name="UE Företagsnamn")
    sub_email = models.EmailField(max_length=200, unique=True,
                                  verbose_name="UE Företagsmail")
    sub_org_nr = models.CharField(max_length=100, unique=True,
                                  verbose_name="UE Org Nummer")
    sub_address = models.CharField(max_length=100,
                                   verbose_name="UE Address")
    sub_city = models.CharField(max_length=100,
                                verbose_name="UE Stad")

    def __str__(self):
        return self.sub_company


class Subcontractor(models.Model):
    """
    Model for Subcontractors
    """
    sub_firstname = models.CharField(max_length=50,
                                     verbose_name="UE Förnamn")
    sub_lastname = models.CharField(max_length=50,
                                    verbose_name="UE Efternamn")
    sub_email = models.EmailField(max_length=200, blank=True,
                                  verbose_name="UE Mail")
    sub_id06 = models.CharField(max_length=100,
                                verbose_name="UE ID06")
    sub_company = models.ForeignKey(SubcontractorCompany,
                                     on_delete=models.CASCADE,
                                     verbose_name="UE Företag")
    unit = models.ManyToManyField(Unit, blank=True,
                                  verbose_name="Enheter")

    def __str__(self):
        return f"{self.sub_firstname} {self.sub_lastname}" 

# SECTION 4 - CARS

class CarType(models.Model):
    """
    Model to define what Car types are available
    """
    car_type_name = models.CharField(max_length=100, unique=True,
                                     verbose_name="Fordonstyp")

    def __str__(self):
        return self.car_type_name
    
class Car(models.Model):
    """
    Car register with all cars.
    """
    car_regnr = models.CharField(max_length=50, unique=True,
                                 verbose_name="Reg Nr")
    car_name = models.CharField(max_length=100,
                                verbose_name="Bil namn")
    car_type_name = models.ForeignKey(CarType, on_delete=models.CASCADE,
                                      verbose_name="Bil typ")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE,
                             verbose_name="Enhet")
    car_active = models.BooleanField(default=True,
                                     verbose_name="Bil aktiv")
    day_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_regnr



# SECTION 5 - 



