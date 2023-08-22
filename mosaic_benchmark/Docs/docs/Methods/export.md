#Export

Mosaic Benchmark can export two different types of files.

 - ``*-edges.csv``: Edgelist representation of the generated graph. One line for each edge in link stream.

 - ``*-communities.npy``: community description.

 
The syntax of each class of output files is the following:

**Communities**

A community is descibed as:
```bash
community_id	[node1, node2, node3, ..., nodeN] stating_time  ending_time
```

**Interactions**
 
One edge per line with the syntax:

``	time	node1	node2``

Where:

 - ``time`` identify the time in which the interaction occurs.

- ``node1`` and ``node2`` are interaction endpoints.

  
Example:
```bash
1.5	2	4
3	4	8
```
##Code
```python
def export(self, address: str):
```
Exports the link stream data to files.

    Parameters:
    - address: Address for exporting data.

##Example
```python
from mosaic_benchmark import ModularLinkStream
M=ModularLinkStream(number_of_nodes=10, t_start=0,t_end=4)
M.snap_shot_scenario(number_of_slices=2)
M.generate_edges(1,1,1,1)

#Exporting
M.export('Address://scenario1')
```

