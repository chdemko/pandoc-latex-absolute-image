Installation
============

[![Python package](https://img.shields.io/github/actions/workflow/status/chdemko/pandoc-latex-absolute-image/python-package.yml?logo=github&branch=develop)](https://github.com/chdemko/pandoc-latex-absolute-image/actions/workflows/python-package.yml)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-absolute-image/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-latex-absolute-image?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-absolute-image.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-absolute-image/)
[![Code Climate](https://img.shields.io/codeclimate/maintainability/chdemko/pandoc-latex-absolute-image?logo=codeclimate&barnch=develop)](https://codeclimate.com/github/chdemko/pandoc-latex-absolute-image/)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/chdemko/pandoc-latex-absolute-image/develop.svg?logo=codefactor)](https://www.codefactor.io/repository/github/chdemko/pandoc-latex-absolute-image)
[![Codacy](https://img.shields.io/codacy/grade/de425638e13b4ceab3bfad1c4557aa6c.svg?logo=codacy&logoColor=white)](https://app.codacy.com/gh/chdemko/pandoc-latex-absolute-image/dashboard)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-absolute-image.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-absolute-image/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-absolute-image.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-absolute-image/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-absolute-image.svg?logo=pypi&logoColor=white)](https://raw.githubusercontent.com/chdemko/pandoc-latex-absolute-image/develop/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-absolute-image?logo=pypi&logoColor=white)](https://pepy.tech/project/pandoc-latex-absolute-image)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-absolute-image.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-absolute-image/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-absolute-image.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-latex-absolute-image/)
[![Pandoc version](https://img.shields.io/badge/pandoc-3.0%20..%203.6-blue.svg?logo=markdown)](https://pandoc.org/)
[![Latest release](https://img.shields.io/github/release-date/chdemko/pandoc-latex-absolute-image.svg?logo=github)](https://github.com/chdemko/pandoc-latex-absolute-image/releases)
[![Last commit](https://img.shields.io/github/last-commit/chdemko/pandoc-latex-absolute-image/develop?logo=github)](https://github.com/chdemko/pandoc-latex-absolute-image/commit/develop/)
[![Repo Size](https://img.shields.io/github/repo-size/chdemko/pandoc-latex-absolute-image.svg?logo=github)](http://pandoc-latex-absolute-image.readthedocs.io/en/latest/)
[![Code Size](https://img.shields.io/github/languages/code-size/chdemko/pandoc-latex-absolute-image.svg?logo=github)](http://pandoc-latex-absolute-image.readthedocs.io/en/latest/)
[![Source Rank](https://img.shields.io/librariesio/sourcerank/pypi/pandoc-latex-absolute-image.svg?logo=libraries.io&logoColor=white)](https://libraries.io/pypi/pandoc-latex-absolute-image)
[![Docs](https://img.shields.io/readthedocs/pandoc-latex-absolute-image.svg?logo=read-the-docs&logoColor=white)](http://pandoc-latex-absolute-image.readthedocs.io/en/latest/)

*pandoc-latex-absolute-image*,
is a [pandoc] filter for adding image at absolute position in the pages.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-latex-absolute-image* requires [python],
a programming language that comes pre-installed on linux and Mac OS X,
and which is easily installed [on Windows].

Install *pandoc-latex-absolute-image* using the bash command

~~~shell-session
$ pipx install pandoc-latex-absolute-image
~~~

To upgrade to the most recent release, use

~~~shell-session
$ pipx upgrade pandoc-latex-absolute-image
~~~

`pipx` is a script to install and run python applications in isolated
environments from the Python Package Index, [PyPI]. It can be installed
using instructions given [here](https://pipx.pypa.io/stable/).

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with pandoc-latex-absolute-image,
please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-absolute-image/issues

Contribute
==========

Instructions
------------

Install `hatch`, then run

~~~shell-session
$ hatch run pip install pre-commit
$ hatch run pre-commit install
~~~

to install `pre-commit` before working on your changes.

Tests
-----

When your changes are ready, run

~~~shell-session
$ hatch test
$ hatch fmt --check
$ hatch run lint:check
$ hatch run docs:build
$ hatch build -t wheel
~~~

for running the tests, checking the style, building the documentation
and building the wheel.
