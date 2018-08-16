from mainApp.models import Action
from spacesApp.models import Space
from django.db import models


class Reservation(Action):
    ACEPTADO = 'A'
    RECHAZADO = 'R'
    PENDIENTE = 'P'
    STATES = (
        (ACEPTADO, 'Aceptado'),
        (RECHAZADO, 'Rechazado'),
        (PENDIENTE, 'Pendiente')
    )
    state = models.CharField(
        'Estado',
        choices=STATES,
        max_length=1,
        default=PENDIENTE
    )
    space = models.ForeignKey(
        Space,
        on_delete=models.CASCADE
    )
