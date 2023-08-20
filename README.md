# Mosaic Benchmark: Synthetic Modular link streams for testing dynamic community detection algorithms

Temporal networks offer valuable insights into dynamic complex systems, capturing the evolving nature of social, biological, and technological interactions. Community structure is a critical feature of real networks, revealing the internal organization of nodes. Dynamic community detection algorithms uncover strongly connected node groups, unveiling hidden temporal patterns and community dynamics in temporal networks. 

However, evaluating the performance of these algorithms remains a challenge. A well-established method is to use tests that rely on synthetic graphs. Yet, this approach does not suit temporal networks with instantaneous edges and continuous time domains, known as link streams. To address this gap, we propose a novel benchmark comprising predefined communities that simulate synthetic modular link streams. 


``Mosaic`` is a meta-library for creating modular link streams for testing dynamic community detection algorithms in complex temporal networks: it creates communities, visualises them and exports the network to csv files.


================ =================== ==================  ==========  ===============
   **Date**      **Python Versions**   **Main Author**   **GitHub**      **pypl**
|date|                 3.8-3.9       `Yasaman Asgari`_  `Source`_   `Distribution`_
================ =================== ==================  ==========  ===============

^^^^^^^^^^^^^^
CDlib Dev Team
^^^^^^^^^^^^^^

======================= ============================
**Name**                **Contribution**
`Giulio Rossetti`_      Library Design/Documentation
`Letizia Milli`_        Community Models Integration
`Rémy Cazabet`_         Visualization
`Salvatore Citraro`_    Community Models Integration
======================= ============================


.. toctree::
   :maxdepth: 1
   :hidden:

   overview.rst
   installing.rst
   tutorial.rst
   reference/reference.rst
   bibliography.rst


.. _`Giulio Rossetti`: http://www.about.giuliorossetti.net
.. _`Letizia Milli`: https://github.com/letiziam
.. _`Salvatore Citraro`: https://github.com/dsalvaz
.. _`Rémy Cazabet`: http://cazabetremy.fr
.. _`Source`: https://github.com/GiulioRossetti/CDlib
.. _`Distribution`: https://pypi.python.org/pypi/CDlib
.. _`SoBigData++`: https://sobigdata.d4science.org/group/sobigdata-gateway/explore?siteId=20371853
## Citation
If you use our algorithm, please cite the following works:

> Yasaman Asgari
> Paper
## Installation

To install the package download (or clone) the current project and copy the demon folder in the root of your application.

Alternatively, use pip:
```bash
sudo pip install mosaic
```

# Execution

The algorithm can be used as a standalone program as well as integrated into Python scripts.

**Link stream parameters**

Name  |  Type | Description | Default 
-------------  | ------------- |------------- | -------------
number_of_nodes  | Integer | Number of nodes | -
starting_time |Float | Starting time for link stream's time domain| 0
ending_time | Float |Ending time for link stream's time domain | -


**Optional arguments**

Flag | Extended Name  |  Type | Description | Default 
-------------  | ------------- |------------- | ------------- | -------------
-d | --avg_degree | Integer | Average node degree | 15
-s | --sigma | Float | Percentage of node's edges within a community | .7
-l | --lbd | Float | Lambda community size distribution | 1
-a | --alpha | Float |Alpha degree distribution | 3
-p | --prob_action | Float |Probability of node action | 1
-r | --prob_renewal | Float |Probability of edge renewal | .8
-q | --quality_threshold | Float | Conductance quality threshold | .3
-n | --new_nodes | Float |Probability of node appearance | 0
-j | --delete_nodes | Float |Probability of node vanishing | 0
-e | --max_events | Integer |Max number of community events for stable iteration | 1

All parameters have a default value.
In order to generate a dynamic graph of 1000 nodes for 1000 iterations applying the simplified version of the algorithm just use:

```bash
python rdyn 1000 1000 True
```

## As python library

RDyn can be also executed within a python program.
In order to generate a dynamic network with the default parameter values just use the following snippet

```python
from rdyn import RDyn
rdb = RDyn()
rdb.execute(simplified=True)
```

To custumize the execution specify the usual parameters during object instantiation.

# Output

RDyn generates a folder named ``results`` and, for each specific model configuration a subfolder having the following naming convention:
 - ``nodes_iterations_avgDegree_sigma_renewal_qualityThreshold_maxEvts`` 
 - Example (default parameters): ``results/1000_1000_15_0.7_0.8_0.3_1``

Within such folder the following files are generated:
 - ``graph-*.txt``: Edgelist representation of the generated graph. One file for stable iteration.
 - ``communities-*.txt``: community description. One file for stable iteration.
 - ``events.txt``: summary of merge\split action per stable iteration.
 - ``interaction.txt``: dynamic graph description as edge stream.
 
The syntax of each class of output files is the following:

**Communities**

A community per line descibed as:
```bash
community_id	[node1, node2, node3, ..., nodeN]
```

**Events**

An block of events per stable iteration descibed as:

```bash
iteration_id:
 	Event1
 	Event2
 	...
 	EventN
```

Where the available events are:
 - ``START``, used for the first stable iteration
 - ``SPLIT id_origina_community [id_new_com1, id_new_com2]``
 - ``MERGE [id_old_com1, id_old_com2]`` the new com will inherit ``id_old_com_1``
 
**Interactions**
 
One interaction per line with the syntax:

``iteration_id	interaction_seq	operation	node1	node2``

Where:
 - ``iteration_id`` identify the iteration in which the interaction occurs
 - ``interaction_seq`` describe an absolute ordering among all the interactions
 - ``operation`` define if the interaction produces a new edge ``+`` or destroy an existing one ``-``
 - ``node1`` and ``node2`` are interaction endpoints
  
Example:
```bash
123	5361	+	385	390
123	5362	-	385	379
```

# Dependencies

RDyn is written in Python and requires the following package to run:
- python>=2.7.11
- networkx==1.11
- numpy==1.11.1
- tqdm
- six
- future
