Mosaic Benchmark: Synthetic Modular link streams for testing dynamic community detection algorithms
===================================================================================================

Temporal networks offer valuable insights into dynamic complex systems,
capturing the evolving nature of social, biological, and technological
interactions. Community structure is a critical feature of real
networks, revealing the internal organization of nodes. Dynamic
community detection algorithms uncover strongly connected node groups,
unveiling hidden temporal patterns and community dynamics in temporal
networks.

However, evaluating the performance of these algorithms remains a
challenge. A well-established method is to use tests that rely on
synthetic graphs. Yet, this approach does not suit temporal networks
with instantaneous edges and continuous time domains, known as link
streams. To address this gap, we propose a novel benchmark comprising
predefined communities that simulate synthetic modular link streams.

``Mosaic`` is a meta-library for creating modular link streams for
testing dynamic community detection algorithms in complex temporal
networks: it creates communities, visualises them and exports the
network to csv files.

Citation
--------

If you use our algorithm, please cite the following works:

   Yasaman Asgari Paper ## Installation

To install the package, download (or clone) the current project and copy
the demon folder in the root of your application.

Alternatively, use pip:

.. code:: bash

   sudo pip install mosaic

Execution
=========

The algorithm can be used as a standalone program and integrated into
Python scripts.

**Link stream parameters**

=============== ======= ===========================================
Name            Type    Description
=============== ======= ===========================================
number_of_nodes Integer Number of nodes
starting_time   Float   Starting time for link stream’s time domain
ending_time     Float   Ending time for link stream’s time domain
=============== ======= ===========================================

**Community parameters**

============= ===== ==========================================
Name          Type  Description
============= ===== ==========================================
nodes         List  list of Integer indices inside a community
starting_time Float Starting time for community
ending_time   Float Ending time for community
============= ===== ==========================================

**Scenario parameters**

============== ===== =================================================
Name           Type  Description
============== ===== =================================================
:math:`\alpha` Float [0.5,1): defines the internal density coefficient
:math:`\beta`  Float [0,1]: related to community identifialbility
:math:`\eta`   Float [0,1]: rewiring noise probability
============== ===== =================================================

Output
======

Mosaic Benchmark can export two different types of files. -
``graph-*.csv``: Edgelist representation of the generated graph. One
line for each edge in link stream. - ``communities-*.txt``: community
description. One file for stable iteration.

The syntax of each class of output files is the following:

**Communities**

A community per line descibed as:

.. code:: bash

   community_id    [node1, node2, node3, ..., nodeN] stating_time  ending_time

**Interactions**

One edge per line with the syntax:

``time    node1   node2``

Where: - ``time`` identify the time in which the interaction occurs -
``node1`` and ``node2`` are interaction endpoints

Example:

.. code:: bash

   1.5 2   4
   3   4   8

Dependencies
============

Mosaic is written in Python and requires the following package to run: -
python>=3.8 - Pandas - tqdm - Numpy - Matplotlib - itertools

Tutorial
========

Check out the official tutorial to get started!
