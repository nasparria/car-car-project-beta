from common.json import ModelEncoder

from .models import Technician, ServiceAppointment, AutomobileVO, FormularioCliente


class AutomobileVOEncoder(ModelEncoder):
    model = AutomobileVO
    properties = [
        "vin",
    ]


class TechnicianEncoder(ModelEncoder):
    model = Technician
    properties = [
        "name",
        "employee_number",
        "id"
    ]


class ServiceAppointmentEncoder(ModelEncoder):
    model = ServiceAppointment
    properties = [
        "vin",
        "owner_name",
        "date",
        "time",
        "technician",
        "reason",
        "finished",
        "vip",
        "id"
    ]
    encoders = {
        "technician": TechnicianEncoder(),
    }

class FormularioClienteEncoder(ModelEncoder):
    model = FormularioCliente
    properties = [
        "empresa",
        "titulo",
        "descripcion"
        # # "enlace",
        # # "File",
        # "Tipo",
        # "date",
        # "time"
    ]