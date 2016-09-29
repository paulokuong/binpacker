| |Build Status|

Knapsack01
--------------

Generic 0-1 Knapsack Problem Solver.

    | Given a set of items, each with a weight and a value, Knapsack01
    | determine the number of each item to include in a collection so
      that the
    | total weight is less than or equal to a given limit and the total
      value is
    | as large as possible.

Requirements
------------

-  Python 3.4 (tested)

Goal
----

| The ultimate goal of this library is to provide a generic interface
| for solving the Knapsack problem for variety of applications.

Code sample
-----------

| Lets say, given the capacity (10) of a team and a list of Jira tickets
  with
| story points and priorities, I would like to know what tickets I want
| to do in the next sprint. Note that you can put multiple parameters
  for
| evaluating the importance of each ticket.

.. code:: python

    from knapsack01.knapsack import Item
    from knapsack01.knapsack import Knapsack

    tickets = [
        Item('A', 1, [1, 4, 8, 23, 6]),
        Item('B', 3, [4]),
        Item('C', 4, [5]),
        Item('E', 5, [7])
    ]
    k = Knapsack(10)
    k.items = tickets
    jira_tickets_next_sprint = k.pick_items()

Contributors
------------

-  Paulo Kuong (`@pkuong`_)

.. _@pkuong: https://github.com/paulokuong

.. |Build Status| image:: https://travis-ci.org/paulokuong/knapsack01.svg?branch=master
   :target: https://travis-ci.org/paulokuong/knapsack01
