#Generating edges

This library generate edges in a modular structure based on the paper ... .
##Procedure

It follows a two step process:

1. Generating edges inside communities

2. Generating edges between communities

Each of these steps, also follow two subsequent processes:

1. Creating backbone connectivity network for contributing nodes

2. Add a temporal dimension to this static network using poisson point process.

For the first step, the parameters are explained as below:

**Backbone connectivity network parameters**

Name  |  Type | Description 
-------------  | ------------- |-------------
alpha | Float | [0.5,1): defines the internal density coefficient 
beta |Float | [0,1]: related to community identifialbility  

For the second step, the arguments are discussed below:

**Poisson point process parameters**

Name  |  Type | Description 
-------------  | ------------- |-------------
lambda_in | Float | Rate of poisson process for generating temporal edges inside communities
lambda_out |Float | Rate of poisson process for generating temporal edges betweek communities

##Rewiring noise
Inorder to add imperfections to our linkstream, we introduced a rewiring noise which can be used after the edge generation procedure.

It has only one paramter: 

Name  |  Type | Description 
-------------  | ------------- |-------------
eta|Float|[0,1]: rewiring noise probability

##Example

``` python
from mosaic_benchmark import ModularLinkStream
M=ModularLinkStream(number_of_nodes=10, t_start=0,t_end=4)
M.add_community([0,1,2,3,4],0,4)
M.add_community([5,6,7,8,9],0,4)

#Full clique inside, No edges outside in backbone connectivity network
M.generate_edges(1,0,1,0)

#Full clique inside and outside in backbone connectivity network (equal rates)
M.clear_edges()
M.generate_edges(1,1,1,1)


#Full clique inside and outside in backbone connectivity network (dissimilar rates)
M.clear_edges()
M.generate_edges(1,1,1,0.01)


# Signifact inside and rare outside in backbone connectivity network (similar rates)
M.clear_edges()
M.generate_edges(0.8,0.1,1,1)

```

**Becarefull that the function gets the attribute with this order:**

```generate_edges(alpha, beta, lambda_in, lambda_out)```