
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import itertools
import json

doc = 'Cuestionarios para capturar la preferencia intertemporal'


class Constants(BaseConstants):
    """
    Description:
        Inherits oTree Class BaseConstants. Defines constants for
        the experiment these will remain unchanged
    """

    players_per_group = None
    num_rounds = 1
    timer = 20
    payment_per_answer = c(0.2)


    instructions_template = 'Biases/InstruccionesB.html'
    instructions_button = "Biases/Instructions_Button.html"
    contact_template = "Biases/Contactenos.html"

    name_in_url = 'Cigarettes_experiment_3'  # name in webbrowser

class Subsession(BaseSubsession):

    def creating_session(self):

        from .pages import initial_page_sequence
        ini = [i.__name__ for i in initial_page_sequence]
        for p in self.get_players():
            pb = ini.copy()
       #     random.shuffle(pb)
            p.page_sequence = json.dumps(pb)

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    # Para el pay-off del sistema
    def set_payoffs(self):
        p.payoff = self.player.quiz_earnings

    # Test de Ida (2014)

    s1_1 = models.FloatField(
        label='¿Cuál sería el valor de "T" que usted elegiría? Ingrese el valor de "T" (es posible incluir decimales)',
        min=0.000001, max=10)

    s1_2 = models.FloatField(
        label='¿Cuál sería el valor de "S" que usted elegiría? Ingrese el valor de "S" (es posible incluir decimales)',
        min=0.000001, max=10)

    # Test de Wang et al. (2016)

    s2_1 = models.FloatField(
        label='En la pregunta 1, ¿Cuál sería el valor mínimo de "X" (en S/.) para que sea indiferente entre ambas opciones?',
        min=100, max=500)

    s2_2 = models.FloatField(
        label='En la pregunta 2, ¿Cuál sería el valor mínimo de "X" (en S/.) para que sea indiferente entre ambas opciones?',
        min=100, max=1000)

    # Test de Andreoni & Sprenger - Prueba (2012)

    s3example_1 = models.IntegerField(
        label='En la fila uno (1), ¿cuántos soles asignaría a la inversión A',
        min=0, max=100)

    s3example_2 = models.IntegerField(
        label='En la fila dos (2), ¿cuántos soles asignaría a la inversión A',
        min=0, max=100)

    # Test de Andreoni & Sprenger (2012)

    s3_1 = models.IntegerField(
        label='En la fila uno (1), ¿cuántos soles asignaría a la inversión A',
        min = 0, max = 100)

    s3_2 = models.IntegerField(
        label='En la fila dos (2), ¿cuántos soles asignaría a la inversión A',
        min=0, max=100)

    s3_3 = models.IntegerField(
        label='En la fila tres (3), ¿cuántos soles asignaría a la inversión A',
        min=0, max=100)

    s3_4 = models.IntegerField(
        label='En la fila cuatro (4), ¿cuántos soles asignaría a la inversión A',
        min=0, max=100)

    s3_5 = models.IntegerField(
        label='En la fila cinco (5), ¿cuántos soles asignaría a la inversión A',
        min=0, max=100)

    s3_6 = models.IntegerField(
        label='En la fila seis (6), ¿cuántos soles asignaría a la inversión A',
        min=0, max=100)

    s3_7 = models.IntegerField(
        label='En la fila uno (1), ¿cuántos soles asignaría a la inversión A',
        min=0, max=100)

    s3_8 = models.IntegerField(
        label='En la fila dos (2), ¿cuántos soles asignaría a la inversión A',
        min=0, max=100)

    s3_9 = models.IntegerField(
        label='En la fila tres (3), ¿cuántos soles asignaría a la inversión A',
        min=0, max=100)

    s3_10 = models.IntegerField(
        label='En la fila cuatro (4), ¿cuántos soles asignaría a la inversión A',
        min=0, max=100)

    s3_11 = models.IntegerField(
        label='En la fila cinco (5), ¿cuántos soles asignaría a la inversión A',
        min=0, max=100)

    s3_12 = models.IntegerField(
        label='En la fila seis (6), ¿cuántos soles asignaría a la inversión A',
        min=0, max=100)

    # Para la secuencia de páginas
    page_sequence = models.StringField()

