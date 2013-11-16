"""
Sparklines for text. text_lines counts your words, paragraphs, pages
and emits a short summary.

The text doesn't need to be here, but I'm trying to write a new paragraph.
"""
__author__ = 'Michael Joseph'
__email__ = 'michaeljoseph@gmail.com'
__url__ = 'https://github.com/michaeljoseph/textlines'
__version__ = '0.0.1'

SHORT_STORY = 10000
NOVEL = 60000
WPM = 130


def talking_time(num_words):
    return num_words / WPM


def work_percentage(words, length):
    return (
        len(words) * 1.0 /
        length
    ) * 100


def text_lines(words):
    paragraphs = words.split('\n\n')
    words = words.split(' ')

    output = [
        '%d words' % len(words),
        '%d paragraphs' % len(paragraphs),
        '%.2f %% of a short story' % work_percentage(words, SHORT_STORY),
        '%.2f %% of a novel' % work_percentage(words, NOVEL),
        u'',
    ]

    return ', '.join(output)
