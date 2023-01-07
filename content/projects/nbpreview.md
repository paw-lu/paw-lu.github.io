Title: nbpreview
Subtitle: View your jupyter notebooks on the command line
Tags: Python, Open source, Jupyter
Date: 2021-8-31
Hero: /images/composition-notebook.jpg
hero_name: Paul Thek
hero_source: https://www.wikiart.org/en/paul-thek/untitled-penmate-composition-notebook-detail-1976
project: https://nbpreview.readthedocs.io/en/latest/

[Jupyter notebooks] are the de-facto editor for data science work.
The file format—`ipynb`—is
tricky to work with.
It's a JSONy format,
which makes it hard to use with traditional developer tools.
This is why [Jupyter notebooks] need custom tools
to work nicely with version control.[^1]

Another area that notebooks work poorly with is the terminal.
Typically when you are navigating via the command line,
you use the [`cat`](https://man7.org/linux/man-pages/man1/cat.1.html) command
to view the contents of files.
If you try this with an `ipynb` file,
it's unintelligble chaos:

```console
$ cat notebook.ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "671faf81-f06a-4d0a-a066-2f040df733fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Text(0.5, 0, ''), Text(0, 0.5, ''), [], []]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABGoAAAGKCAYAAABUy6cjAAAAOXRF
      WHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMiwgaHR0cHM6Ly9tYXRwbG
      90bGliLm9yZy8rg+JYAAAACXBIWXMAAAsTAAALEwEAmpwYAACCsElEQVR4nOzdd3iV
      5fkH8O+7zspOSNiEEfYeYe+l4MatdVTrqNaqrVprq3ZptT/bqq3aOmtdVFRwgSB7T9
...
```

So if you have a directory full of `ipynb` files,
you essentially have to launch Jupyter Lab to preview your files.
If the files are on a remote machine that you're connected to over ssh
you need to download the files,
or launch a remote Jupyter server to connect to.
It'a a lot of work if you just needed to take a quick peak at the contents
of a notebook.

Similar to the tooling that has been developed
to make version control play nicer with Jupyter notebooks,[^1]
I wanted to contribute to improving compatability
between [Jupyter notebooks] and the terminal.

![nbpreview logo light]({static}/images/nbpreview_logo_light.svg)

[nbpreview](https://nbpreview.readthedocs.io/en/latest/) is a terminal viewer
for [Jupyter notebooks].
It parses the JSON structure of an `ipynb` file
and then presents the data in a terminal-compatable way.
So now,
insead of running `cat notebook.ipynb` in your terminal,
if you run `nbpreview notebook.ipynb`,
you get something like this:

![nbpreview notebook render]({static}/images/nbpreview_notebook_render.webp)

There is a _lot_ of content Jupyter notebooks can render—images,
$\LaTeX$,
inteactive charts,
warnings,
markdown—and
I try to get most of it looking right on the command line.
I go over a full list of the different types of content we render
[in the documentation](https://nbpreview.readthedocs.io/en/latest/features.html#features).

[^1]:
    [Jupytext](https://github.com/mwouts/jupytext),
    [nbdime](https://nbdime.readthedocs.io/en/latest/),
    and [ReviewNB](https://www.reviewnb.com/)
    are some solutions for increasing compatability
    between Jupyter notebooks and version control.

[jupyter notebooks]: https://jupyter.org/
