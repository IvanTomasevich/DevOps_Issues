from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ticket
# Create your tests here.


class TicketModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='Piky')
        Ticket.objects.create(
            title='Título de ejemplo',
            sub_title='Subtítulo de ejemplo',
            body='Contenido de ejemplo',
            tipe='IN',
            level='Mid',
            author=user
        )

    def test_title_field(self):
        ticket = Ticket.objects.get(id=1)
        max_length = ticket._meta.get_field('title').max_length
        self.assertEqual(ticket.title, 'Título de ejemplo')
        self.assertEqual(max_length, 48)

    def test_sub_title_field(self):
        ticket = Ticket.objects.get(id=1)
        max_length = ticket._meta.get_field('sub_title').max_length
        self.assertEqual(ticket.sub_title, 'Subtítulo de ejemplo')
        self.assertEqual(max_length, 96)

    def test_body_field(self):
        ticket = Ticket.objects.get(id=1)
        self.assertEqual(ticket.body, 'Contenido de ejemplo')

    def test_tipe_field_choices(self):
        ticket = Ticket.objects.get(id=1)
        choices = dict(ticket._meta.get_field('tipe').choices)
        self.assertEqual(choices, {'IN': 'Incident', 'RQ': 'Request'})

    def test_level_field_choices(self):
        ticket = Ticket.objects.get(id=1)
        choices = dict(ticket._meta.get_field('level').choices)
        self.assertEqual(choices, {'Low': 'Bajo', 'Mid': 'Medio', 'Hi': 'Alta', 'VHI': 'Critico'})

    def test_level_field_default(self):
        ticket = Ticket.objects.get(id=1)
        self.assertEqual(ticket.level, 'Mid')

    def test_author_field(self):
        ticket = Ticket.objects.get(id=1)
        self.assertEqual(ticket.author.username, 'Piky')
