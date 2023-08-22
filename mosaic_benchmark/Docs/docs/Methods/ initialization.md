#Initialization

For unifying all the function we have created a Python class named ``ModularLinkStream`` which is very easy to access. 

The parameters for initializing is: 

Name  |  Type | Description 
-------------  | ------------- |-------------
number_of_nodes  | Integer |Total number of nodes in the network.
t_start |Float | Starting time of the link stream.
t_end | Float |Ending time of the link stream.


##Example
```python
from mosaic_benchmark import ModularLinkStream
M=ModularLinkStream(number_of_nodes=100, t_start=0,t_end=100)
print('Starting time', M.t_start)
print('Ending time', M.t_end)
print('Number of nodes', M.number_of_nodes)
print('Nodes' , M.nodes)

#Creating some communities
M.snap_shot_scenario(number_of_slices=2)

print('Communities', M.communities)
print('Number of communities', M.number_of_communities)

#Generate edges
M.generate_edges(1,1,1,1)

#Access to edges:
M.temporal_edges
```

