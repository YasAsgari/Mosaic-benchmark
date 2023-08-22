#Scenario description
As explained in the paper, we have implemented three different methods for generating the communities in this library.

##Methods
1. Ad-hoc scenario: The experimenter designs the communities based on their research questions.

2. Snapshots: It helps us to have snapshots (with fixed or varying windowsize) so that the edges inside have a continuous time occurence.

3. Random: A function that generates approximately a number of communities, different in size of nodes and time domains.


### Ad-hoc scenario example
``` python
from mosaic_benchmark import ModularLinkStream
M=ModularLinkStream(number_of_nodes=10, t_start=0,t_end=4)
M.add_community([0,1,2,3,4],0,4)
M.add_community([5,6,7,8,9],0,4)
M.communities
```

The parameters are:

Name  |  Type | Description 
-------------  | ------------- |------------- 
nodes | List | list of Integer indices inside a community 
t_start |Float | Starting time for community
t_end | Float |Ending time for community 

### Snapshot scenario example

``` python
from mosaic_benchmark import ModularLinkStream
M=ModularLinkStream(number_of_nodes=10, t_start=0,t_end=4)
#Varying windowsizes
M.snap_shot_scenario(3, fixed=False)
print('varying',M.communities)


#Fixed windowsizes
M.clear_communities()
M.snap_shot_scenario(3, fixed=True)
print('fixed',M.communities)

```
The parameters are:

Name  |  Type | Description 
-------------  | ------------- |------------- 
number_of_slices | int | The number of time intervals to divide the scenario into.
fixed |bool, optional | If True, evenly divides time intervals; if False, varies interval length. Default is True.

### Random scenario example
``` python
from mosaic_benchmark import ModularLinkStream
M=ModularLinkStream(number_of_nodes=10, t_start=0,t_end=4)
M.random_scenario(3)
M.communities
```

The parameters are:

Name  |  Type | Description 
-------------  | ------------- |------------- 
approx_order_of_communities:| int |  it gives an approximate number of communities 


**Note that the algorithm filters communities with less 2 nodes.**

##Emptying Mosaic
As described in the paper, we can empty the mosaics randomly based on our need to create a more realistic scenario.

To do so, we can use the method named ``empty_mosaics`` which has only one parameter which is the probability of emptying which is called ``gamma``.

### Random scenario example
``` python
from mosaic_benchmark import ModularLinkStream
M=ModularLinkStream(number_of_nodes=10, t_start=0,t_end=100)
M.random_scenario(40)
print('before', len(M.communities))
#Emptying
M.empty_mosaics(gamma=0.5)
print('after', len(M.communities))

```