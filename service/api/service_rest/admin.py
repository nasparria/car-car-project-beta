from django.contrib import admin
from .models import AutomobileVO, Technician, ServiceAppointment ,FormularioCliente


class AutomobileVOAdmin(admin.ModelAdmin):
    pass


class TechnicianAdmin(admin.ModelAdmin):
    pass


class ServiceAppointmentAdmin(admin.ModelAdmin):
    pass

class FormularioClienteAdmin(admin.ModelAdmin):
    pass


admin.site.register(AutomobileVO, AutomobileVOAdmin)
admin.site.register(Technician, TechnicianAdmin)
admin.site.register(ServiceAppointment, ServiceAppointmentAdmin)
admin.site.register(FormularioCliente, FormularioClienteAdmin)