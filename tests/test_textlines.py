from . import BaseTestCase

import textlines


class TestTextLines(BaseTestCase):

    def test_textlines_docs(self):
        expected_text = (
            '36 words, 3 paragraphs, '
            '0.36 % of a short story, 0.06 % of a novel'
        )
        self.assertEquals(
            expected_text,
            textlines.text_lines(textlines.__doc__)
        )
