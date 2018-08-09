from mainApp.models import Action
from articlesApp.models import Article
from django.db import models


class Loan(Action):
    VIGENTE = 'V'
    CADUCADO = 'C'
    PERDIDO = 'L'
    STATES = (
        (VIGENTE, 'Vigente'),
        (CADUCADO, 'Caducado'),
        (PERDIDO, 'Perdido')
    )
    state = models.CharField(
        'Estado',
        choices=STATES,
        max_length=1,
        default=VIGENTE
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )
