Title: Dress up
Subtitle: Turning your words to 𝔴𝔬𝔯𝔡𝔰, 🆆🅾🆁🅳🆂, and 𝔀𝓸𝓻𝓭𝓼
Hero: /images/the_reluctant_bride.webp
Tags: Python, Open source
Date: 2010-12-12
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
to bring some 🅴🅼🅿🅷🅰🆂🅸🆂 ᴛᴏ 𝔂𝓸𝓾𝓻 𝖜𝖔𝖗𝖉𝖘.

![Dressup logo]({static}/images/dressup_logo.webp)

But, these Unicode characters are a pain to access.
I wanted an easy way to programmatically use some of these unique characters to spell words in Unicode characters.
[Dress up] is a command-line interface and Python library
that allows you to convert normal characters into special Unicode versions.
It maps the characters you know into their Unicode counterparts.
For example, `Lorep ipsum` can become:

| Style                 | Conversion            |
| --------------------- | --------------------- |
| Circle                | Ⓛⓞⓡⓔⓟ ⓘⓟⓢⓤⓜ           |
| Negative circle       | 🅛🅞🅡🅔🅟 🅘🅟🅢🅤🅜           |
| Monospace             | Ｌｏｒｅｐ ｉｐｓｕｍ |
| Math bold             | 𝐋𝐨𝐫𝐞𝐩 𝐢𝐩𝐬𝐮𝐦           |
| Math bold fraktur     | 𝕷𝖔𝖗𝖊𝖕 𝖎𝖕𝖘𝖚𝖒           |
| Math bold italic      | 𝑳𝒐𝒓𝒆𝒑 𝒊𝒑𝒔𝒖𝒎           |
| Math bold script      | 𝓛𝓸𝓻𝓮𝓹 𝓲𝓹𝓼𝓾𝓶           |
| Math double struck    | 𝕃𝕠𝕣𝕖𝕡 𝕚𝕡𝕤𝕦𝕞           |
| Math monospace        | 𝙻𝚘𝚛𝚎𝚙 𝚒𝚙𝚜𝚞𝚖           |
| Math sans             | 𝖫𝗈𝗋𝖾𝗉 𝗂𝗉𝗌𝗎𝗆           |
| Math sans bold        | 𝗟𝗼𝗿𝗲𝗽 𝗶𝗽𝘀𝘂𝗺           |
| Math sans bold italic | 𝙇𝙤𝙧𝙚𝙥 𝙞𝙥𝙨𝙪𝙢           |
| Math sans italic      | 𝘓𝘰𝘳𝘦𝘱 𝘪𝘱𝘴𝘶𝘮           |
| Parenthesized         | ⒧⒪⒭⒠⒫ ⒤⒫⒮⒰⒨           |
| Square                | 🄻🄾🅁🄴🄿 🄸🄿🅂🅄🄼           |
| Negative square       | 🅻🅾🆁🅴🅿 🅸🅿🆂🆄🅼           |
| Cute                  | Ĺőŕéṕ íṕśúḿ           |
| Math fraktur          | 𝔏𝔬𝔯𝔢𝔭 𝔦𝔭𝔰𝔲𝔪           |
| Rock dots             | Ḷöṛëṗ ïṗṡüṁ           |
| Small caps            | ʟᴏʀᴇᴩ ɪᴩꜱᴜᴍ           |
| Stroked               | Łøɍɇᵽ ɨᵽsᵾm           |
| Subscript             | ₗₒᵣₑₚ ᵢₚₛᵤₘ           |
| Superscript           | ᴸᵒʳᵉᵖ ⁱᵖˢᵘᵐ           |
| Inverted              | ןoɹǝd ıdsnɯ           |
| Reversed              | ⅃oᴙɘq iqꙅum           |

For quick and convenient access,
these conversions can be accessed through a command line-interface.

![Animated Dress up]({static}/images/dressup_cli.svg)

For use in other applications,
there is also a Python API:

```pycon
>>> import dressup
>>> dressup.convert("Hello", unicode_type="negative circle")
'🅗🅔🅛🅛🅞'
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
