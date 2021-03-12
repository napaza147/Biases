
from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Player, Group

import json


class Introduction_Part4(Page):

    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)
    pass

class Biases1(Page):

    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True

    form_model = 'player'
    form_fields = ['s1_1', 's1_2']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

  #  def is_displayed(self):
   #     if self.participant.vars['MobilePhones'] is False:
    #        return True
     #   else:
      #      return False

class Biases2(Page):

    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True

    form_model = 'player'
    form_fields = ['s2_1', 's2_2']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

   # def is_displayed(self):
    #    if self.participant.vars['MobilePhones'] is False:
     #       return True
      #  else:
       #     return False

class Biases3_examp(Page):

    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True

    form_model = 'player'
    form_fields = ['s3example_1', 's3example_2']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

  #  def is_displayed(self):
   #     if self.participant.vars['MobilePhones'] is False:
    #        return True
     #   else:
      #      return False

class Biases3(Page):

    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True

    form_model = 'player'
    form_fields = ['s3_1', 's3_2', 's3_3','s3_4', 's3_5', 's3_6']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

  #  def is_displayed(self):
   #     if self.participant.vars['MobilePhones'] is False:
    #        return True
     #   else:
      #      return False

class Biases4(Page):

    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True

    form_model = 'player'
    form_fields = ['s3_7', 's3_8', 's3_9','s3_10', 's3_11', 's3_12']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)


class Payment(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True

    def vars_for_template(self):
        return {'participant_id': self.participant.label,
                'quiz_earnings': self.participant.vars['quiz_earnings'],
                'numero': self.participant.vars['quiz_questions_correct'],
                'ea1': self.participant.vars['ea1'],
                'ea2': self.participant.vars['ea2'],
                'ea3': self.participant.vars['ea3'],
                'ea4': self.participant.vars['ea4'],
                'pago_final': self.participant.vars['quiz_earnings'] / 25  + 5
                }

#Una secuencia definida inicialmente (que luego se aleatorizará)
initial_page_sequence = [
    Introduction_Part4,
    Biases1,
    Biases2,
    Biases3_examp,
    Biases3,
    Biases4,
    Payment,
]

page_sequence = [

]

class Biases0(Page):

    def inner_dispatch(self):
        page_seq = int(self.__class__.__name__.split('_')[1])
        page_to_show = json.loads(self.player.page_sequence)[page_seq]
        self._is_frozen = False
        self.__class__ = globals()[page_to_show]
        return super(globals()[page_to_show], self).inner_dispatch()


for i, _ in enumerate(initial_page_sequence):
    NewClassName = "Page_{}".format(i)
    A = type(NewClassName, (Biases0,), {})
    locals()[NewClassName] = A
    page_sequence.append(locals()[NewClassName])

class Eleccion0(Page):
    def is_displayed(self):
            return False