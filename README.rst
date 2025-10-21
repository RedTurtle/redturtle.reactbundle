.. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on PyPI or github. It is a comment.

.. image:: https://img.shields.io/pypi/v/redturtle.reactbundle.svg
    :target: https://pypi.python.org/pypi/redturtle.reactbundle/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/redturtle.reactbundle.svg
    :target: https://pypi.python.org/pypi/redturtle.reactbundle
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/l/redturtle.reactbundle.svg
    :target: https://pypi.python.org/pypi/redturtle.reactbundle/
    :alt: License


======================
RedTurtle React Bundle
======================

Addon that add React into Classic UI

Features
--------

- Install it and have React and ReactDOM available in your Plone Classic UI as bundle.


React version
--------------

- React 19.2.0

Development
-----------

If you need to update React version, just run::

    > npm install react@latest react-dom@latest
    > npm run build

Installation
------------

Install redturtle.reactbundle by adding it to your buildout::

    [buildout]

    ...

    eggs =
        redturtle.reactbundle


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/RedTurtle/redturtle.reactbundle/issues
- Source Code: https://github.com/RedTurtle/redturtle.reactbundle


Authors
-------

This product was developed by RedTurtle Technology team.

.. image:: https://avatars1.githubusercontent.com/u/1087171?s=100&v=4
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/


License
-------

The project is licensed under the GPLv2.
