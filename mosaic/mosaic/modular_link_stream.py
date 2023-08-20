import itertools
import pandas as pd
from mosaic.mosaic_community import Mosaic
from mosaic.edge_generator import outside_temporal_edges,inside_temporal_edges
#from mosaic.scenario_description_helper import random_scenario, snapshot_scenario
class Modular_linkstream:
    def __init__(self, number_of_nodes:int, t_start: float, t_end: float, sceneraio_description: str=None) :
        assert t_start>=0,'Starting time should be non-negative'
        assert t_end> t_start, 'Ending time should be greater than starting time'
        self.t_end=t_end
        self.t_start=t_start
        self.number_of_nodes=number_of_nodes
        self.number_of_communities=0
        self.communities={}


    def add_community(self,nodes: list, t_start: float, t_end: float):
        self.number_of_communities+=1
        self.communities[f'c{self.number_of_communities}']=Mosaic(nodes, t_start, t_end)

    def remove_community(self, label:str):
        if label in self.communities:
            self.number_of_communities-=1
            self.communities.pop(label, None)
            return
        raise AssertionError('Label is not present')
    
    def generate_edges(self, alpha:float, beta:float, lmbda_in:float, lmbda_out:float):
        stream=[]
        for mosaic1 , mosaic2 in itertools.combinations(self.communities.values(),2):
            stream.extend(outside_temporal_edges(mosaic1,mosaic2, lmbda_out,alpha, beta))
        for mosaic in self.communities.values():
            stream.extend(inside_temporal_edges(mosaic,alpha, lmbda_in))
        return pd.DataFrame(stream, columns=['node1', 'node2','time'])

    def export(self, address:str):
        pass