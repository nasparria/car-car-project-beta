from common.json import ModelEncoder

from .models import Technician, ServiceAppointment, AutomobileVO, FormularioCliente, Tipo


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
        "descripcion",
        "enlace",
        # "tipo",
        # "File",
        # "tipo",
        "date",
        "time"
    ]

    def get_extra_data(self, o):
        return {"tipo": o.tipo.abbreviation}

class TipoEncoder(ModelEncoder):
    model = Tipo
    properties = [
        "name",
        "abbreviation",
        "id",
    ]
    encoders = {"formulariocliente": FormularioClienteEncoder()}