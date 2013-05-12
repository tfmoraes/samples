import itertools
import matplotlib.pyplot as plt

def plot_vectors(*vectors):
    ax = plt.gca()
    minx, maxx = 0, -9999999
    miny, maxy = 0, -9999999
    colors = itertools.cycle(('r', 'g', 'b', 'y', 'k', 'c'))
    for v, c in itertools.izip(vectors, colors):
        minx = min(v[0], minx)
        maxx = max(v[0], maxx)
        miny = min(v[1], miny)
        maxy = max(v[1], maxy)
        arr = plt.Arrow(0, 0, v[0], v[1], color=c)
        ax.add_patch(arr)
    
    print minx, maxx
    print miny, maxy
    ax.set_xlim([minx, maxx])
    ax.set_ylim([miny, maxy])
    plt.show()
