looter
======

To install, just run

.. code:: bash

    $ pip install looter

features
--------

-  super-light-weight crawler
-  automatically generate spider with template
-  blazing fast speed with concurrent.futures
-  provides shell to debug your crawler

example
-------

Here's a very simple image crawler: First, open it with shell

.. code:: bash

    $ looter shell konachan.net/post

Then, extract with css and grab images you want!

.. code:: python

    >>> imgs = tree.cssselect('a.directlink')
    >>> save_imgs(imgs)

Or, just in a more crude way :d

.. code:: python

    >>> save_imgs(links(res, search='jpg'))

And of course, there are more functions for you to discover.

usage
-----

.. code:: bash

    Usage:
      looter genspider <name> <tmpl> [--async]
      looter shell [<url>]
      looter (-h | --help | --version)

    Options:
      -h --help        Show this screen.
      --version        Show version.
      --async          Use async instead of concurrent.

Templates available: data, image. You can also view
`examples <https://github.com/alphardex/looter/tree/master/looter/examples>`__.

tutorial
--------

以下是中文教程：\ `猛戳这里 <http://nameless.wang/2018/03/07/looter%E2%80%94%E2%80%94%E8%B6%85%E8%BD%BB%E9%87%8F%E7%BA%A7%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6/>`__
