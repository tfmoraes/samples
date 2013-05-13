import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from itertools import product, combinations, cycle, izip

from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

# taken from http://stackoverflow.com/a/11156353
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

def plot_vectors2D(*vectors):
    ax = plt.gca()
    minx, maxx = 0, -9999999
    miny, maxy = 0, -9999999
    colors = cycle(('r', 'g', 'b', 'y', 'k', 'c'))
    for v, c in izip(vectors, colors):
        minx = min(v[0], minx)
        maxx = max(v[0], maxx)
        miny = min(v[1], miny)
        maxy = max(v[1], maxy)
        if len(v) == 4:
            print v
            arr = plt.Arrow(v[0], v[1], v[2], v[3], color=c)
        else:        
            arr = plt.Arrow(0, 0, v[0], v[1], color=c)
        ax.add_patch(arr)
    
    print minx, maxx
    print miny, maxy
    ax.set_xlim([minx, maxx])
    ax.set_ylim([miny, maxy])
    plt.show()


# taken from http://stackoverflow.com/a/11156353
def plot_vectors3D(*vectors):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")

    colors = cycle(('r', 'g', 'b', 'y', 'k', 'c'))
    for v, c in izip(vectors, colors):
        if len(v) == 6:
            a = Arrow3D([v[0], v[3]],[v[1], v[4]],[v[2], v[5]], mutation_scale=20, lw=1, arrowstyle="-|>", color=c)
        else:
            a = Arrow3D([0,v[0]],[0,v[1]],[0,v[2]], mutation_scale=20, lw=1, arrowstyle="-|>", color=c)
        ax.add_artist(a)
    plt.show()

def projection(v, w):
    return v.dot(w) * (w / (np.linalg.norm(w)**2))

