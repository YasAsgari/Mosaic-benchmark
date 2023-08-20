from matplotlib.patches import Rectangle
from matplotlib import pyplot as plt

def plot_rectangles_simple(rectangles,ax , colors):
  for rect in rectangles.keys():
      P_Start,P_End,V_Start,V_End=rectangles[rect]
      w, h = P_End-P_Start, V_End-V_Start
      ax.add_patch(Rectangle((P_Start, V_Start), w, h, fill=True,facecolor=colors[rect],edgecolor='#000000',lw=1))
  ax.plot([0,0], [1,1])
  ax.invert_yaxis()
  ax.set_aspect('equal')
  ax.axis('off')