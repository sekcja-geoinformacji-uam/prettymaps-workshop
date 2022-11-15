import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from prettymaps import plot
# pip install osmnx==1.2.1

# zdefiniowanie przestrzeni mapy
fig, ax = plt.subplots(figsize = (10, 10), constrained_layout = True)
# MAPA
layers = plot(
    # Adres:
    #'Plac Grunwaldzki, Szczecin, Polska',
    # współrzędne geograficzne
    (53.428433469351, 14.54659327488271),
    # promień okręgu/kwadratu w którym tworzymy mapę
    radius = 1000,
    # Matplotlib axis
    ax = ax,
    # wybór warstw OpenStreetMap
    layers = {
            # obrys kształtu mapy
            'perimeter': {},
            # ulice i ich szerokości
            'streets': {
                'width': {
                    'motorway': 5,
                    'trunk': 5,
                    'primary': 4.5,
                    'secondary': 4,
                    'tertiary': 3.5,
                    'residential': 3,
                    'service': 2,
                    'unclassified': 2,
                    'pedestrian': 1,
                    'footway': .5,
                }
            },
            # Inne warstwy:
            # {'tags': {KEY_OSM: VALUE_OSM}}
            'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False},
            'water': {'tags': {'natural': ['water', 'bay']}},
            'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
            'forest': {'tags': {'landuse': 'forest'}},
            'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}}
        },
        # parametry stylizacyjne dla każdej warstwy:
        # wpisz nazwę jednej z warstw którą wcześniej zdefiniowałeś, a nastepnie nadaj jej styl
        # fc - facecolor (kolor wypełnienia), ec - edgecolor (kolor obrysu), lw - linewidth (grubość obrysu)
        # alpha - przezroczystość (0-1), zorder - kolejność wyświetlania warstw
        # palette - lista kolorów, które będą losowo przyporządkowane do obiektów z danej warstwy
        drawing_kwargs = {
            'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'zorder': -1},
            'perimeter': {'fill': False, 'ec': '#373732', 'lw': 5, 'zorder': 5},
            'green': {'fc': '#15ad38', 'ec': '#2f3737', 'lw': 1, 'zorder': 1},
            'forest': {'fc': '#1d8009', 'ec': '#2f3737', 'lw': 1, 'zorder': 1},
            'water': {'fc': '#39a5d7', 'ec': '#2F3737', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
            'parking': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
            'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
            'building': {'palette': ['#4d2f26', '#75483b', '#9c6656'], 'ec': '#2F3737', 'lw': .5, 'zorder': 4}
        },
        # atrybucja OpenStreetMap
        osm_credit = {'x': 0.84, 'y': 0.97, 'color': '#2F3737', 'fontsize': 0.5}
)

plt.savefig('img/basic.png')
plt.show()