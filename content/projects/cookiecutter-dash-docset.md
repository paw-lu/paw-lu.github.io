Title: Cookiecutter Dash docset
Subtitle: Automating the generation of documentation for scientific Python libraries
Tags: Python, Open source, Jupyter
Date: 2022-11-25
Hero: /images/still-life-with-cookies.jpg
Project: https://paw-lu.github.io/cookiecutter-dash-docset/
hero_name: Still Life with Cookies by John Stuart Ingle
hero_source: https://www.wikiart.org/en/john-stuart-ingle/still-life-with-cookies

[Dash] is an app[^1] that lets you instantly search through documentation sets offline.
[Hynek Schlawack has a great writeup on the benefits of using Dash.](https://hynek.me/articles/productive-fruit-fly-programmer/)
If you find yourself
with dozen of documentation tabs open
or repeatedly searching for the same APIs,
[Dash] might be useful for you.

![Demo of Dash searching docs]({static}/images/dash_demo.gif)

[Dash] comes with a few documentation sets,
but if a library isn't included
[you can always generate your own](https://kapeli.com/docsets).[^2]
You can contribute your documentation sets to [Kapeli/Dash-User-Contributions]
to make them available to others.

However,
if you want to keep things up to date,
each time new version of a library releases
you need to:

1. Clone the library
2. Reinstall the dependencies
3. Rebuild the docs
4. Convert the docs to a Dash-compatible documentation set
5. Create a pull request for [Kapeli/Dash-User-Contributions]

I personally have contributed and maintain over 6 different docsets,
so going through all of these steps
each time a library makes a new release is tedious.
As a result,
many documentation sets don't keep up with their libraries
and go stale.

[Cookiecutter Dash docset](https://paw-lu.github.io/cookiecutter-dash-docset/)
generates a repository that automates this process.
After generating the project
[and modifying the template in a couple of key areas](https://paw-lu.github.io/cookiecutter-dash-docset/modifying_the_project/),
you should have a repository that specifies the entire docset building process
and automatically re-runs it on [GitHub Actions] with a new release of the library.

Upon detecting a new project release,
this project should automatically:

1. Build a new Dash documentation set
2. Contribute the docset to [Kapeli/Dash-User-Contributions]

See more information
about this project's features
in the [documentation](https://paw-lu.github.io/cookiecutter-dash-docset/how_it_works/).

Using this,
I've currently automated the docsets of six different Python libraries:

- [Arviz](https://github.com/paw-lu/arviz-dash-docset/commit/58e0b9d47328290ef31fb6446bee8a48004670af)
- [Invoke](https://github.com/paw-lu/invoke-dash-docset/commit/6117c119c3f18f1d946110d53f14758fb619735e)
- [Nox](https://github.com/paw-lu/nox-dash-docset/commit/fb1d3cbfb9c4c6b7cdeda53939d171f7ca65952d)
- [Polars](https://github.com/paw-lu/polars-dash-docset/commit/19031411a8eb295eb5fd78d08ffbff1d60b42a13)
- [PyMC](https://github.com/paw-lu/pymc-dash-docset/commit/10969a24d57a2f236cf76f27ba3d8ac02dc001d8)
- [Seaborn](https://github.com/paw-lu/seaborn-dash-docset)

These repositories [automatically generate pull requests against](https://github.com/Kapeli/Dash-User-Contributions/pulls?q=is%3Apr+author%3A%40me+is%3Aclosed) against [Kapeli/Dash-User-Contributions]
every time any of these libraries has a new release—keeping
docsets up to date for me and other [Dash] users.

[^1]:
    There are multiple alternatives as well—like
    [Zeal](https://zealdocs.org/),
    [Velocity](https://velocity.silverlakesoftware.com/),
    [Helm Dash](https://github.com/dash-docs-el/helm-dash),
    and [dasht](https://github.com/sunaku/dasht)

[^2]: Tools like [doc2dash] help automate some of the generation.

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[dash]: https://kapeli.com/dash
[doc2dash]: https://doc2dash.readthedocs.io/en/stable
[github actions]: https://github.com/features/actions
[kapeli/dash-user-contributions]: https://github.com/Kapeli/Dash-User-Contributions
