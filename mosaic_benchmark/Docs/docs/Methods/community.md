#Mosaic Community

To extend the definition of communities for temporal networks, we define a mosaic as a community which contains nodes interacting in the time frame.

Name  |  Type | Description 
-------------  | ------------- |-------------
number_of_nodes  | Integer |A list containing nodes that belong to the mosaic.
t_start |Float | Starting time  of the mosaic.
t_end | Float |Ending time of the mosaic.

##Example
```python
from mosaic_benchmark import ModularLinkStream
M=ModularLinkStream(number_of_nodes=100, t_start=0,t_end=100)

#Creating some communities
M.snap_shot_scenario(number_of_slices=2)

print('Communities', M.communities)

mos1=M.communities['c1']

print(f'Nodes={mos1.nodes}---Time:({mos1.t_start},{mos1.t_end})')

```

