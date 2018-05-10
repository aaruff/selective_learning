import random

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'experiment'
    players_per_group = None
    num_rounds = 1
    num_expressions_per_cell = 10
    num_problems = 4


class Subsession(BaseSubsession):
    def easy_int(self):
        return random.randint(1, 10)

    def hard_int(self):
        return random.randint(10, 1000)

    def creating_session(self):
        problem_types = [True, True, False, False]
        for player in self.get_players():
            problems = []
            for pid in range(Constants.num_problems):
                expressions = []
                for eid in range(Constants.num_expressions_per_cell):
                    op = random.choice([' + ', ' - ', ' * '])
                    if problem_types[pid]:
                        operand1 = self.hard_int()
                        operand2 = self.hard_int()
                    else:
                        operand1 = self.easy_int()
                        operand2 = self.easy_int()

                    expressions.append("{} {} {}".format(operand1, op, operand2))
                problems.append(expressions)
            player.participant.vars['problems'] = problems


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    problem = models.IntegerField(min=0, max=4)
