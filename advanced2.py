import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from prettymaps import plot

# zdefiniowanie przestrzeni mapy
fig, ax = plt.subplots(figsize = (10, 10), constrained_layout = True)
# MAPA
layers = plot(
    # Adres:
    'Stad van de Zon, Heerhugowaard, Netherlands',
    # promień okręgu/kwadratu w którym tworzymy mapę
    radius = 1100,
    # Matplotlib axis
    ax = ax,
    # wybór warstw OpenStreetMap
    layers = {
            'perimeter': { 'circle': False, 'dilate': 100},
            'streets': {
                'width': {
                    'motorway': 5,
                    'trunk': 5,
                    'primary': 4.5,
                    'secondary': 4,
                    'tertiary': 3.5,
                    'cycleway': 3.5,
                    'residential': 3,
                    'service': 2,
                    'unclassified': 2,
                    'pedestrian': 2,
                    'footway': 1,
                },
                'circle': False, 'dilate': 100
            },
            'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': True, 'circle': False, 'dilate': 100},
            'water': {'tags': {'natural': ['water', 'bay']}, 'circle': False, 'dilate': 100},
            'forest': {'tags': {'landuse': 'forest'}, 'circle': False, 'dilate': 100},
            'green': {'tags': {'landuse': ['grass', 'orchard'], 'natural': ['island', 'wood'], 'leisure': 'park'}, 'circle': False, 'dilate': 100},
            'beach': {'tags': {'natural': 'beach'}, 'circle': False, 'dilate': 100},
            'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}, 'circle': False}
        },
        drawing_kwargs = {
            'perimeter': {'fill': False, 'lw': 0, 'zorder': 0},
            'background': {'fc': '#F2F4CB', 'zorder': -1},
            'green': {'fc': '#8BB174', 'ec': '#2F3737', 'hatch_c': '#A7C497', 'hatch': 'ooo...', 'lw': 1, 'zorder': 1},
            'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 2},
            'water': {'fc': '#a8e1e6', 'ec': '#2F3737', 'hatch_c': '#9bc3d4', 'hatch': 'ooo...', 'lw': 1, 'zorder': 3},
            'beach': {'fc': '#FCE19C', 'ec': '#2F3737', 'hatch_c': '#d4d196', 'hatch': 'ooo...', 'lw': 1, 'zorder': 3},
            'parking': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
            'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 4},
            'building': {'palette': ['#433633', '#FF5E5B'], 'ec': '#2F3737', 'lw': .5, 'zorder': 5},
            
        },
        osm_credit = {'x': .405, 'y': .68, 'color': '#2F3737', 'fontsize': 0.5}
)

xmin, ymin, xmax, ymax = layers['perimeter'].bounds
dx, dy = xmax-xmin, ymax-ymin
a = .2
ax.set_xlim(xmin+a*dx, xmax-a*dx)
ax.set_ylim(ymin+a*dy, ymax-a*dy)

ax.text(
    xmin+.39*dx, ymin+.305*dy,
    ' '*3 + 'Stad van de Zon,\nHeerhugowaard, Netherlands',
    color = '#2F3737',
    zorder = 6, rotation = +1.75,
    fontproperties = fm.FontProperties(fname = 'PermanentMarker-Regular.ttf', size = 24)
)

plt.savefig('img/advanced2.png')
plt.show()