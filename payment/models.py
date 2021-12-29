from django.db import models
from agreement.models import  *
years = ( 
    ("2022", "2022"), 
    ("2023", "2023"), 
    ("2024", "2024"), 
    ("2025", "2025"),
) 

months = ( 
    ("January", "January"), 
    ("February", "February"), 
    ("March", "March"), 
    ("April", "April"), 
    ("May", "May"), 
    ("June", "June"), 
    ("Jule", "Jule"), 
    ("August", "August"), 
    ("September", "September"), 
    ("October", "October"), 
    ("November", "November"), 
    ("December", "December"),  
) 

class payment(models.Model): 
    agreement = models.ForeignKey(agreement, on_delete=models.SET_NULL, null=True) 
    teacher = models.ForeignKey(teacher, on_delete=models.SET_NULL, null=True) 
    course = models.ForeignKey(course, on_delete=models.SET_NULL, null=True) 
    student = models.ForeignKey(student, on_delete=models.SET_NULL, null=True)  
    # Payment year and payment month is a date of course in which year or month pupil is studying and payment date is the date whne pupil is pays.
    payment_year = models.CharField(max_length=50, choices=years) 
    payment_month = models.CharField(max_length=100, choices=months)
    discount_status = models.CharField(max_length=15, default="Passive", choices=(("Active", "Active"), ("Passive", "Passive"))) 
    discount_reason = models.CharField(max_length=100,default="No") 
    discount_size = models.PositiveIntegerField(default=0)
    payment_date = models.DateField() 
    must_pay = models.PositiveIntegerField(default=0)
    cashier = models.CharField(max_length=100) 
    in_hand = models.PositiveIntegerField(default=0)
    bank = models.PositiveIntegerField(default=0)
    card  = models.PositiveIntegerField(default=0)  
    payed = models.PositiveIntegerField(default=0)   
    rest_money = models.PositiveIntegerField(default=0)
