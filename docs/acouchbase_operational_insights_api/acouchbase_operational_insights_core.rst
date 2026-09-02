======================================
Core API
======================================


.. contents::
    :local:

AsyncCluster
==============

.. module:: acouchbase_operational_insights.cluster
.. autoclass:: AsyncCluster

    .. important::
        See :ref:`AsyncCluster Overloads<async-cluster-overloads-ref>` for details on overloaded methods.

    .. automethod:: create_instance
    .. automethod:: database

    .. important::
        See :ref:`AsyncCluster Overloads<async-cluster-overloads-ref>` for details on overloaded methods.

    .. automethod:: execute_query

    .. important::
        See :ref:`AsyncCluster Overloads<async-cluster-overloads-ref>` for details on overloaded methods.

    .. automethod:: start_query

    .. automethod:: shutdown


AsyncDatabase
==============

.. module:: acouchbase_operational_insights.database
.. autoclass:: AsyncDatabase

    .. autoproperty:: name
    .. automethod:: scope


AsyncScope
==============

.. module:: acouchbase_operational_insights.scope
.. autoclass:: AsyncScope

    .. autoproperty:: name

    .. important::
        See :ref:`AsyncScope Overloads<async-scope-overloads-ref>` for details on overloaded methods.

    .. automethod:: execute_query

    .. important::
        See :ref:`AsyncScope Overloads<async-scope-overloads-ref>` for details on overloaded methods.

    .. automethod:: start_query
