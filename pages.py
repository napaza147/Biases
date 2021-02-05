
from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Player, Group

import json

class Biases0(Page):

    pass

class Biases1(Page):

    form_model = 'player'
    form_fields = ['s1_1', 's1_2']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

  #  def is_displayed(self):
   #     if self.participant.vars['MobilePhones'] is False:
    #        return True
     #   else:
      #      return False

    timeout_seconds = 180

class Biases2(Page):

    form_model = 'player'
    form_fields = ['s2_1', 's2_2']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

   # def is_displayed(self):
    #    if self.participant.vars['MobilePhones'] is False:
     #       return True
      #  else:
       #     return False

    timeout_seconds = 180

class Biases3(Page):

    form_model = 'player'
    form_fields = ['s3_1', 's3_2', 's3_3','s3_4', 's3_5', 's3_6']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

  #  def is_displayed(self):
   #     if self.participant.vars['MobilePhones'] is False:
    #        return True
     #   else:
      #      return False

    timeout_seconds = 300

#Una secuencia definida inicialmente (que luego se aleatorizará)
initial_page_sequence = [
    Biases0,
    Biases1,
    Biases2,
    Biases3,
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