Title: Dress up
Subtitle: Turning your words to ๐ด๐ฌ๐ฏ๐ก๐ฐ, ๐๐พ๐๐ณ๐, and ๐๐ธ๐ป๐ญ๐ผ
Hero: /images/the_reluctant_bride.webp
Tags: Python, Open source
Date: 2020-4-26
Project: https://dressup.readthedocs.io/en/latest/
hero_name: The reluctant bride by Auguste Toulmouche
hero_source: https://www.wikiart.org/en/auguste-toulmouche/the-reluctant-bride-1866

There are a [bunch of interesting unicode charters](https://home.unicode.org/).
What's cool is that since most devices and applications support them,
you can use them to hack some extra expressivity in traditionally limited platforms.
A terminal is a great example of this.
Typically thought of as an environment where you only send and receive text,
groups like [Textual](https://www.textualize.io/)
and [Charm](https://charm.sh/) use unicode characters to build entire UIs in the terminal.
Projects like [viu](https://github.com/atanunq/viu) will even use characters
to draw images in your terminal.
It's also just fun to use them over limited chat apps like SMS
to bring some ๐ด๐ผ๐ฟ๐ท๐ฐ๐๐ธ๐ แดแด ๐๐ธ๐พ๐ป ๐๐๐๐๐.

![Dressup logo]({static}/images/dressup_logo.webp)

But, these Unicode characters are a pain to access.
I wanted an easy way to programmatically use some of these unique characters to spell words in Unicode characters.
[Dress up] is a command-line interface and Python library
that allows you to convert normal characters into special Unicode versions.
It maps the characters you know into their Unicode counterparts.
For example, `Lorep ipsum` can become:

| Style                 | Conversion            |
| --------------------- | --------------------- |
| Circle                | โโโกโโ โโโขโคโ           |
| Negative circle       | ๐๐๐ก๐๐ ๐๐๐ข๐ค๐           |
| Monospace             | ๏ผฌ๏ฝ๏ฝ๏ฝ๏ฝ ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ |
| Math bold             | ๐๐จ๐ซ๐๐ฉ ๐ข๐ฉ๐ฌ๐ฎ๐ฆ           |
| Math bold fraktur     | ๐ท๐๐๐๐ ๐๐๐๐๐           |
| Math bold italic      | ๐ณ๐๐๐๐ ๐๐๐๐๐           |
| Math bold script      | ๐๐ธ๐ป๐ฎ๐น ๐ฒ๐น๐ผ๐พ๐ถ           |
| Math double struck    | ๐๐?๐ฃ๐๐ก ๐๐ก๐ค๐ฆ๐           |
| Math monospace        | ๐ป๐๐๐๐ ๐๐๐๐๐           |
| Math sans             | ๐ซ๐๐๐พ๐ ๐๐๐๐๐           |
| Math sans bold        | ๐๐ผ๐ฟ๐ฒ๐ฝ ๐ถ๐ฝ๐๐๐บ           |
| Math sans bold italic | ๐๐ค๐ง๐๐ฅ ๐๐ฅ๐จ๐ช๐ข           |
| Math sans italic      | ๐๐ฐ๐ณ๐ฆ๐ฑ ๐ช๐ฑ๐ด๐ถ๐ฎ           |
| Parenthesized         | โงโชโญโ?โซ โคโซโฎโฐโจ           |
| Square                | ๐ป๐พ๐๐ด๐ฟ ๐ธ๐ฟ๐๐๐ผ           |
| Negative square       | ๐ป๐พ๐๐ด๐ฟ ๐ธ๐ฟ๐๐๐ผ           |
| Cute                  | ฤนลลรฉแน รญแนลรบแธฟ           |
| Math fraktur          | ๐๐ฌ๐ฏ๐ข๐ญ ๐ฆ๐ญ๐ฐ๐ฒ๐ช           |
| Rock dots             | แธถรถแนรซแน รฏแนแนกรผแน           |
| Small caps            | สแดสแดแดฉ ษชแดฉ๊ฑแดแด           |
| Stroked               | ลรธษษแตฝ ษจแตฝsแตพm           |
| Subscript             | โโแตฃโโ แตขโโแตคโ           |
| Superscript           | แดธแตสณแตแต โฑแตหขแตแต           |
| Inverted              | ืoษนวd ฤฑdsnษฏ           |
| Reversed              | โoแดษq iq๊um           |

For quick and convenient access,
these conversions can be accessed through a command line-interface.

![Animated Dress up]({static}/images/dressup_cli.svg)

For use in other applications,
there is also a Python API:

```pycon
>>> import dressup
>>> dressup.convert("Hello", unicode_type="negative circle")
'๐๐๐๐๐'
```

[Dress up] also serves as a demonstration of what I think are the
current best practices in Python development.
It features strong linting via
[flake8](https://github.com/paw-lu/dressup/actions/workflows/pre-commit.yml) and select plugins
high test coverage [pytest](https://github.com/paw-lu/dressup/actions/workflows/tests.yml)
generated documentation via [Sphinx](https://dressup.readthedocs.io/en/latest/),
and type hinting.
All ran through a CI/CD framework powered by [Nox](https://github.com/theacodes/nox)
and [GitHub Actions](https://github.com/paw-lu/dressup/actions).

[dress up]: https://dressup.readthedocs.io/en/latest/
