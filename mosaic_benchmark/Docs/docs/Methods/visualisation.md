#Visualisation

Inorder to visualize the communities, we have provided a function that shows different communities.

> for better visualisations regarding the linkstreams, use the [tnetwork](https://tnetwork.readthedocs.io/en/latest/notebooks/demo_visu.html)!

##Example
```python
from mosaic_benchmark import ModularLinkStream
M=ModularLinkStream(number_of_nodes=20, t_start=0,t_end=10)
M.snap_shot_scenario(number_of_slices=4, fixed=False)

#Visualize
M.plot()
```

