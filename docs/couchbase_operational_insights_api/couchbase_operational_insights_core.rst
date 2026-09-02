===========================
Core API
===========================

.. contents::
    :local:

Cluster
==============

.. module:: couchbase_operational_insights.cluster
.. autoclass:: Cluster

    .. important::
        See :ref:`Cluster Overloads<cluster-overloads-ref>` for details on overloaded methods.

    .. automethod:: create_instance
    .. automethod:: database

    .. important::
        See :ref:`Cluster Overloads<cluster-overloads-ref>` for details on overloaded methods.

    .. automethod:: execute_query

    .. important::
        See :ref:`Cluster Overloads<cluster-overloads-ref>` for details on overloaded methods.

    .. automethod:: start_query
    .. automethod:: shutdown


Database
==============

.. module:: couchbase_operational_insights.database
.. autoclass:: Database

    .. autoproperty:: name
    .. automethod:: scope

Scope
==============

.. module:: couchbase_operational_insights.scope
.. autoclass:: Scope

    .. autoproperty:: name

    .. important::
        See :ref:`Scope Overloads<scope-overloads-ref>` for details on overloaded methods.

    .. automethod:: execute_query

    .. important::
        See :ref:`Scope Overloads<scope-overloads-ref>` for details on overloaded methods.

    .. automethod:: start_query
