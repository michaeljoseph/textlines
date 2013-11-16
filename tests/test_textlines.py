from . import BaseTestCase

import textlines


class TestTextLines(BaseTestCase):

    def test_textlines_docs(self):
        expected_text = (
            '27 :abc: 2 :page_with_curl: '
            '0.27 % of a :notebook: 0.04 % of a :books: '
            '0m16s :speech_balloon: '
            '0m5s :eyes::book:'
        )
        self.assertEquals(
            expected_text,
            textlines.text_lines(textlines.__doc__)
        )
