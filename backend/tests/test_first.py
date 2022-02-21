from lib2to3.pgen2.literals import simple_escapes
from telnetlib import TELNET_PORT
from django import setup
from django.test import SimpleTestCase

class TestBackendSetUp(SimpleTestCase):

    def setUp(self) -> None:
        return super().setUp()
    

class TestBackend(TestBackendSetUp):

    def test_me(self):
        a = 4
        b = 4

        self.assertEqual(a,b)

