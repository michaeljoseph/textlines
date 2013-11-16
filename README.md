# textlines

[![Build Status](https://secure.travis-ci.org/michaeljoseph/textlines.png)](http://travis-ci.org/michaeljoseph/textlines)
[![Stories in Ready](https://badge.waffle.io/michaeljoseph/textlines.png?label=ready)](https://waffle.io/michaeljoseph/textlines) [![pypi version](https://badge.fury.io/py/textlines.png)](http://badge.fury.io/py/textlines)
[![# of downloads](https://pypip.in/d/textlines/badge.png)](https://crate.io/packages/textlines?version=latest)
[![code coverage](https://coveralls.io/repos/michaeljoseph/textlines/badge.png?branch=master)](https://coveralls.io/r/michaeljoseph/textlines?branch=master)

## Features

Emoji sparklines for text.
`textlines` counts your words, paragraphs, pages and emits a short, emoji summary.

1338 :abc: 61 :page_with_curl: 13.38 % of a :notebook: 2.23 % of a :books: 13m802s :speech_balloon: 4m267s :eyes::book:

## Usage

Install `textlines`:

    pip install textlines

Run the cli:

```
textlines.

Usage:
  textlines [options] <source>

  textlines -h | --help

Options:
  --debug               Debug.
  -h --help             Show this screen.
```

```python
$ textlines a-brief-history-of-the-word/talk/abstract.md 
1338 :abc: 61 :page_with_curl: 13.38 % of a :notebook: 2.23 % of a :books: 13m802s :speech_balloon: 4m267s :eyes::book:
```

## Documentation

[API Documentation](http://textlines.rtfd.org)

## Testing

Install development requirements:

    pip install -r requirements.txt

Tests can then be run with:

    nosetests

Lint the project with:

    flake8 textlines tests

## API documentation

Generate the documentation with:

    cd docs && PYTHONPATH=.. make singlehtml

To monitor changes to Python files and execute flake8 and nosetests
automatically, execute the following from the root project directory:

    stir