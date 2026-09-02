=========================
Server Async Request API
=========================

.. contents::
    :local:

.. module:: acouchbase_operational_insights.query_handle

AsyncQueryHandle
+++++++++++++++++++

.. py:class:: AsyncQueryHandle

    .. automethod:: fetch_status
    .. automethod:: cancel

AsyncQueryResultHandle
++++++++++++++++++++++++

.. py:class:: AsyncQueryResultHandle

    .. automethod:: fetch_results
    .. automethod:: discard_results

AsyncQueryStatus
+++++++++++++++++++

.. py:class:: AsyncQueryStatus

    .. automethod:: results_ready
    .. automethod:: result_handle
