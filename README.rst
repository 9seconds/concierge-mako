concierge-mako
==============

|PyPI| |Build Status| |Code Coverage|

``concierge-mako`` provides support of Mako_ templates for concierge_.

To interpret your ``~/.conciergerc`` as Mako template, just use ``-u`` flag:

.. code-block:: shell

    $ concierge -u mako -o ~/.ssh/config

or

.. code-block:: shell

    $ concierge-check -u mako -o ~/.ssh/config

.. _Mako: http://makotemplates.org
.. _concierge: https://github.com/9seconds/concierge

.. |PyPI| image:: https://img.shields.io/pypi/v/concierge-mako.svg
    :target: https://pypi.python.org/pypi/concierge-mako

.. |Build Status| image:: https://travis-ci.org/9seconds/concierge-mako.svg?branch=master
    :target: https://travis-ci.org/9seconds/concierge-mako

.. |Code Coverage| image:: https://codecov.io/github/9seconds/concierge-mako/coverage.svg?branch=master
    :target: https://codecov.io/github/9seconds/concierge-mako?branch=master
