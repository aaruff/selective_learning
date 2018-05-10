import random

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SelectProblemPage(Page):
    form_model = 'player'
    form_fields = ['problem']


class ChooseToSolvePage(Page):
    def vars_for_template(self):
        pid = self.player.problem
        return {'problems': self.player.participant.vars['problems'][pid]}


page_sequence = [
    SelectProblemPage,
    ChooseToSolvePage,
]
