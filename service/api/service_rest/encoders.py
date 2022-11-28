from common.json import ModelEncoder

from .models import Technician, ServiceAppointment, AutomobileVO, FormularioCliente # State


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
        # "state",
        # "File",
        # "tipo",
        "date",
        "time"
    ]

    # def get_extra_data(self, o):
    #     return {"state": o.state.abbreviation}

# class StateEncoder(ModelEncoder):
#     model = State
#     properties = [
#         "name",
#         "abbreviation",
#         "id",
#     ]
#     encoders = {"formulariocliente": FormularioClienteEncoder()}