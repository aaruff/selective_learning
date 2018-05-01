from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SelectProblemPage(Page):
    form_model = 'player'
    form_fields = ['problem']


class ChooseToSolvePage(Page):
    pass


page_sequence = [
    SelectProblemPage,
    ChooseToSolvePage,
]
