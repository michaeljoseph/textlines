from . import BaseTestCase

from textlines import textlines


class TestTextlines(BaseTestCase):

    def test_something(self):
        self.assertEquals(
            'Hello World!',
            textlines(),
        )
