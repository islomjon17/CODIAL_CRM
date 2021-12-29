from django.db import models
from agreement.models import  *
# Create your models here.


class payment(models.Model):
    oylar =  (
        ("Yanvar", "Yanvar"),
        ("Fevral", "Fevral"),
        ("Mart", "Mart"),
        ("Aprel", "Aprel"),
        ("Iyun", "Iyun"),
        ("Iyul", "Iyul"),
        ("Avgust", "Avgust"),
        ("Sentabr", "Sentabr"),
        ("Okatabr", "Okatabr"),
        ("Noyabr", "Noyabr"),
        ("Dekabr", "Dekabr"),
    )
    shartnoma_raqammi = models.IntegerField()
    teacher = models.ForeignKey(teacher, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(course,  on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(student,  on_delete=models.SET_NULL, null=True)
    year = models.IntegerField()
    tolov_oyi = models.ChoiceField(max_length=10, choices=oylar)
    chegirma_statur = models.CharField(max_lenght=15, default="yo'q")
    ch_sababi =  models.CharField(max_lenght=15)
    ch_sababi = models.PositiveIntegerField()
    t_sanasi = models.DateField()
    kassir = models.CharField(max_lenght=30)
    naqd = models.PositiveIntegerField()
    plastik = models.PositiveIntegerField()
    bank = models.PositiveIntegerField()
    click = models.PositiveIntegerField()
    jami_tolondi = models.PositiveIntegerField()
    jami_qoldi = models.models.PositiveIntegerField()
    def __str__(self):
        f"{self.student.ism}, {self.student.familya}, {self.student.agreement}"
