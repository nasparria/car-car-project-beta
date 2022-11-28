from django.db import models
# from django.contrib.auth.models import User


class AutomobileVO(models.Model):
    vin = models.CharField(max_length=17, unique=True)


class Technician(models.Model):
    name = models.TextField()
    employee_number = models.SmallIntegerField(unique=True)


class ServiceAppointment(models.Model):
    vin = models.CharField(max_length=17, null=True, unique=False)
    owner_name = models.CharField(max_length=66)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    technician = models.ForeignKey(
        Technician,
        related_name="technician",
        on_delete=models.CASCADE,
    )
    reason = models.CharField(max_length=50)
    finished = models.BooleanField(default=False, null=True, blank=True)
    vip = models.BooleanField(default=False, null=True)


# class State(models.Model):
#     name = models.CharField(max_length=40)
#     id1 = models.IntegerField(primary_key=True)
#     abbreviation = models.CharField(max_length=2, unique=True)

#     def __str__(self):
#         return f"{self.name}, {self.abbreviation}"

#     class Meta:
#         ordering = ("id1",)  # Default ordering for State

# TIPO_REQUIRIMIENTO = (
#     ('tecnologia','TECNOLOGIA'),
#     ('marketing digital', 'MKT'),
#     ('analytics','ANALYTICIS'),
# )

class FormularioCliente(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # <--- added
    empresa = models.CharField(max_length=21, null=True, unique=True) # nombre de la empresa
    titulo = models.CharField(max_length=66) # titulo del requirimiento
    descripcion = models.CharField(max_length=66) # descripcion del requirimiento
    enlace = models.URLField(null=True)
    # File = models.FileField(null=True)
    # state = models.ForeignKey(
    #     State, related_name="+", on_delete=models.PROTECT)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    # technician = models.ForeignKey(
    #     Technician,
    #     related_name="technician",
    #     on_delete=models.CASCADE,
    # )
    # reason = models.CharField(max_length=50)
    # finished = models.BooleanField(default=False, null=True, blank=True)
    # vip = models.BooleanField(default=False, null=True)

# class Requerimiento(models.Model):
#     empresa = models.CharField(max_length=21, null=True, unique=True) # nombre de la empresa
#     titulo = models.CharField(max_length=66) # titulo del requirimiento
#     descripcion = models.TextField() # descripcion del requirimiento
#     enlace = models.URLField()
#     File = models.FileField()
#     Tipo = models.CharField(max_length=17, choices=TIPO_REQUIRIMIENTO, default="tecnologia")
#     date = models.DateField(null=True)
#     time = models.TimeField(null=True)
#     # technician = models.ForeignKey(
#     #     Technician,
#     #     related_name="technician",
#     #     on_delete=models.CASCADE,
#     # )
#     # reason = models.CharField(max_length=50)
#     # finished = models.BooleanField(default=False, null=True, blank=True)
#     # vip = models.BooleanField(default=False, null=True)