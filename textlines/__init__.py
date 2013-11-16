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
PAGE = 450
WPM = 100
RPM = 300

EMOJI = {
    'word': ':abc:',
    'paragraph': ':page_with_curl:',
    'page': ':page_facing_up:',
    'short_story': ':notebook:',
    'novel': ':books:',
    'talking_time': ':speech_balloon:',
    'reading_time': ':eyes::book:',
}


def human_duration(minutes):
    return '%dm%ds' % (minutes, minutes * 60)


def reading_time(num_words):
    return human_duration(
        (num_words * 1.0) / RPM
    )


def talking_time(num_words):
    return human_duration(
        (num_words * 1.0) / WPM
    )


def work_percentage(words, length):
    percentage = (len(words) * 1.0 / length) * 100
    return '%.2f %%' % percentage


def text_lines(words):
    paragraphs = words.split('\n\n')
    words = words.split(' ')

    output = [
        '%d %s' % (len(words), EMOJI['word']),
        '%d %s' % (len(paragraphs), EMOJI['paragraph']),
        '%s of a %s' % (
            work_percentage(words, SHORT_STORY),
            EMOJI['short_story'],
        ),
        '%s of a %s' % (
            work_percentage(words, NOVEL),
            EMOJI['novel'],
        ),
        '%s %s' % (talking_time(len(words)), EMOJI['talking_time']),
        '%s %s' % (reading_time(len(words)), EMOJI['reading_time']),
    ]

    return ' '.join(output)
