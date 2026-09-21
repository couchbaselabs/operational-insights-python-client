=========================================
Using the Python Operational Insights SDK
=========================================

The Operational Insights Python SDK library allows you to connect to a Couchbase Operational Insights cluster from Python.

Useful Links
=======================

* :operational_insights_sdk_github:`Source <>`
* :operational_insights_sdk_jira:`Bug Tracker <>`
* :operational_insights_sdk_docs:`Python docs on the Couchbase website <>`
* :operational_insights_sdk_release_notes:`Release Notes <>`
* :operational_insights_sdk_compatibility:`Compatibility Guide <>`
* :couchbase_dev_portal:`Couchbase Developer Portal <>`

How to Engage
=======================

* :couchbase_discord:`Join Discord and contribute <>`.
    The Couchbase Discord server is a place where you can collaborate about all things Couchbase.
    Connect with others from the community, learn tips and tricks, and ask questions.
* Ask and/or answer questions on the :operational_insights_sdk_forums:`Python SDK Forums <>`.


Installing the SDK
=======================

.. note::
    Best practice is to use a Python virtual environment such as venv or pyenv.
    Checkout:

        * Linux/MacOS: `pyenv <https://github.com/pyenv/>`_
        * Windows: `pyenv-win <https://github.com/pyenv-win/pyenv-win>`_


.. note::
    The Operational Insights Python SDK provides wheels for Windows, MacOS and Linux platforms for supported versions of Python.
    See :operational_insights_sdk_version_compat:`Operational Insights Python Version Compatibility <>` docs for details.

Prereqs
++++++++++

See :operational_insights_sdk_version_compat:`Operational Insights Python Version Compatibility <>` for details on supported Python versions.

We also recommend the following command to install/update ``pip``, ``setuptools`` and ``wheel``.

.. code-block:: console

    $ python3 -m pip install --upgrade pip setuptools wheel

Install
++++++++++

.. code-block:: console

    $ python3 -m pip install couchbase-operational-insights

Introduction
=======================

Connecting to an Operational Insights cluster is as simple as creating a new ``Cluster`` instance to represent the ``Cluster``
you are using. You are able to execute most operations immediately, and they will be queued until the connection is successfully established.

Here is a simple example of creating a ``Cluster`` instance and issuing a query.

.. code-block:: python

    from couchbase_operational_insights.cluster import Cluster
    from couchbase_operational_insights.credential import Credential
    from couchbase_operational_insights.options import (ClusterOptions,
                                             QueryOptions,
                                             SecurityOptions)


    # Update this to your cluster
    # IMPORTANT:  The appropriate port needs to be specified. The SDK's default ports are 80 (http) and 443 (https).
    #             If attempting to connect to Capella, the correct ports are most likely to be 8095 (http) and 18095 (https).
    #             Capella example: https://cb.2xg3vwszqgqcrsix.cloud.couchbase.com:18095
    endpoint = 'https://--your-instance--'
    username = 'username'
    pw = 'Password!123'
    # User Input ends here.

    cred = Credential.from_username_and_password(username, pw)
    cluster = Cluster.create_instance(endpoint, cred)

    # Execute a query and process rows as they arrive from server.
    statement = 'SELECT * FROM `travel-sample`.inventory.airline WHERE country="United States" LIMIT 10;'
    res = cluster.execute_query(statement)
    for row in res.rows():
        print(f'Found row: {row}')
    print(f'metadata={res.metadata()}')

Logging
=======================

The SDK logs through Python's standard :mod:`logging` module and does not configure the root logger.

The SDK's two APIs are peer top-level packages, so each one logs to a logger named after its package:

+-----------------------------------------+------------------------------------------+
| API                                     | Logger name                              |
+=========================================+==========================================+
| ``couchbase_operational_insights``      | ``couchbase_operational_insights``       |
+-----------------------------------------+------------------------------------------+
| ``acouchbase_operational_insights``     | ``acouchbase_operational_insights``      |
+-----------------------------------------+------------------------------------------+

Both names are available as ``LOGGER_NAME`` on the package you imported, so there is no need to hardcode
the string.

Integrating with your application's logging
--------------------------------------------

Attach your own handler to the SDK's logger and set the level you want. Nothing else is required.

.. code-block:: python

    import logging

    from couchbase_operational_insights import LOGGER_NAME

    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(my_handler)

If your application has already configured the root logger, SDK records propagate to it like those of any
other library, and you can filter them by the logger names above.

Quick debugging with an environment variable
---------------------------------------------

Set ``PYCBOI_LOG_LEVEL`` to turn SDK logging on without changing any code. Accepted values are ``trace``,
``debug``, ``info``, ``warning``, ``error``, ``critical`` and ``off``.

.. code-block:: console

    $ PYCBOI_LOG_LEVEL=debug python my_app.py

This sets the level on both SDK loggers. It attaches a handler *only* when neither the SDK logger nor the
root logger already has one. So, in an application that has configured logging, the records simply flow
into the handlers you installed. The root logger's own handlers and level are never modified.

Source Control
=======================

The source control is available  on :operational_insights_sdk_github:`Github <>`.
Once you have cloned the repository, you may contribute changes through Github.
For more details see :operational_insights_sdk_contribute:`CONTRIBUTING.md <>`.

License
=======================

The Operational Insights Python SDK is licensed under the Apache License 2.0.

See :operational_insights_sdk_license:`LICENSE <>` for further details.
