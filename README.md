# Rituals

Common tasks for [Invoke](http://www.pyinvoke.org/) that are needed again and again.

![GINOSAJI](https://raw.githubusercontent.com/jhermann/rituals/master/static/img/symbol-200.png) … and again and again.

 [![Groups](https://img.shields.io/badge/Google_groups-rituals--dev-orange.svg)](https://groups.google.com/forum/#!forum/rituals-dev)
 [![Travis CI](https://api.travis-ci.org/jhermann/rituals.svg)](https://travis-ci.org/jhermann/rituals)
 [![Coveralls](https://img.shields.io/coveralls/jhermann/rituals.svg)](https://coveralls.io/r/jhermann/rituals)
 [![GitHub Issues](https://img.shields.io/github/issues/jhermann/rituals.svg)](https://github.com/jhermann/rituals/issues)
 [![License](https://img.shields.io/pypi/l/rituals.svg)](https://github.com/jhermann/rituals/blob/master/LICENSE)
 [![Development Status](https://pypip.in/status/rituals/badge.svg)](https://pypi.python.org/pypi/rituals/)
 [![Latest Version](https://img.shields.io/pypi/v/rituals.svg)](https://pypi.python.org/pypi/rituals/)
 [![Download format](https://pypip.in/format/rituals/badge.svg)](https://pypi.python.org/pypi/rituals/)
 [![Downloads](https://img.shields.io/pypi/dw/rituals.svg)](https://pypi.python.org/pypi/rituals/)

## Overview

The following lists the common task implementations that the ``invoke_tasks`` module contains.
See the next section on how to integrate them into your `tasks.py`.

* ``help`` –    Default task, when invoked with no task names.
* ``clean`` –   Perform house-cleaning.
* ``build`` –   Build the project.
* ``test`` –    Perform standard unittests.
* ``check`` –   Perform source code checks.
* ``bump`` –    Bump a development version.
* ``dist`` –    Distribute the project.
* ``release.prep`` – Prepare for a release (perform QA checks, and switch to non-dev versioning).
* … and *many* more, see `inv -l` for a complete list.

The guiding principle for these tasks is to strictly separate
low-level tasks for building and installing (via ``setup.py``)
from high-level convenience tasks a developer uses (via ``invoke``).
Invoke tasks can use Setuptools ones as building blocks,
but never the other way 'round
– this avoids any bootstrapping headaches during package installations.

Use ``inv -h ‹task›`` as usual to get details on the options of these tasks.
Look at the [invoke_tasks](https://github.com/jhermann/rituals/blob/master/src/rituals/invoke_tasks.py) source
if you want to know what these tasks do exactly.

:bulb: | The easiest way to get a working project using `rituals` is the [py-generic-project](https://github.com/Springerle/py-generic-project) cookiecutter archetype. That way you have a working project skeleton within minutes that is fully equipped, with all aspects of building, testing, quality checks, continuous integration, documentation, and releasing covered.
---- | :----


## Some Practical Examples

In projects that include *Rituals* in their `tasks.py` (e.g. this one), the following commands can be used.

Command | Description
----: | :----
`inv test.tox --clean -e py34` | Run `tox` for Python 3.4 with a clean status, i.e. an empty `.tox` directory.
`inv bump` | Set the `tag_build` value in `setup.cfg` to something like `0.3.0.dev117+0.2.0.g993edd3.20150408t1747`, uniquely identifying dev builds, even in dirty working directories.


## Usage

### Add common tasks to your project's `task.py`

Add `rituals` to your `dev-requirements.txt` or a similar file,
or add it to `setup_requires` in your `setup.py`.
Then at the start of your `tasks.py`, use the following statement to define _all_ tasks that are considered standard:

```py
from rituals.easy import *
```

Note that this defines Invoke's ``Collection`` and ``task`` identifiers,
the root ``namespace``with Ritual's default tasks, and some common helpers
(see the documentation for details).
Of course, you can also do more selective imports,
or build your own Invoke namespaces with the specific tasks you need.

:warning: | These tasks expect an importable `setup.py` that defines a `project` dict with the setup parameters, see [javaprops](https://github.com/Feed-The-Web/javaprops) and [py-generic-project](https://github.com/Springerle/py-generic-project) for examples.
---- | :----

To refer to the current GitHub ``master`` branch, use a ``pip`` requirement like this:

```
-e git+https://github.com/jhermann/rituals.git#egg=rituals
```


### Change default project layout

By default, sources are expected in `src/‹packagename›` and tests in `src/tests`.

You can change this by calling one of the following functions, directly after the import from `rituals.invoke_tasks`.

* `config.set_maven_layout()` – Changes locations to `src/main/python/‹packagename›` and `src/test/python`.
* `config.set_flat_layout()` – Changes locations to `‹packagename›` and `tests`.


### Change default project configuration

**TODO**


## Contributing

To create a working directory for this project, call these commands:

```sh
git clone "https://github.com/jhermann/rituals.git"
cd rituals
. .env --yes --develop
invoke build --docs
```

To use the source in this working directory within another project,
change your current directory to _this_ project,
then call `bin/pip` from *that* project's virtualenv like so:

    …/.venv/…/bin/pip install -e .

See [CONTRIBUTING](https://github.com/jhermann/rituals/blob/master/CONTRIBUTING.md) for more.

[![Throughput Graph](https://graphs.waffle.io/jhermann/rituals/throughput.svg)](https://waffle.io/jhermann/rituals/metrics)


## Releasing

This is the process of releasing  ``rituals`` itself,
projects that use it will have an identical to very similar sequence of commands.

```sh
inv release.prep
inv dist --devpi # local release + tox testing

git push && git push --tags # … and wait for Travis CI to do its thing

twine upload -r pypi dist/*
```

If you have any pending changes, staged or unstaged, you'll get an error like this:

![uncommitted changes](https://raw.githubusercontent.com/jhermann/rituals/master/docs/_static/img/invoke-release-prep-changes.png)


## Related Projects

* [Springerle/py-generic-project](https://github.com/Springerle/py-generic-project)
* [pyinvoke/invoke](https://github.com/pyinvoke/invoke)
* [pyinvoke/invocations](https://github.com/pyinvoke/invocations) – A collection of reusable Invoke tasks and task modules.


## Acknowledgements

* Logo elements from [clker.com Free Clipart](http://www.clker.com/).
* In case you wonder about the logo, [watch this](http://youtu.be/9VDvgL58h_Y).
