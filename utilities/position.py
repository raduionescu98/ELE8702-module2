from math import sqrt

"""Position utility module

This module contains position related functions

"""

def equidistant_coords(n:int, map_size:int) -> list:
    """Génère des coordonnées equidistantes sur une surface carrée

    Place des points equidistant où placer des antennes de manière à 
    obtenir un couverture sur totale sur un surface carrée.

    Args:
        n (int): Nombre de coodonnées à générer
        map_size (int): Aire de la surface à couvrir en km^2

    Return:
        list(tuple(float,float)): liste de coordonnées (x,y)
    """
    n_by_side = int(sqrt(n))
    map_length = sqrt(map_size)*1000
    equi_dist = map_length/n_by_side
    points = []
    for x_point in range(n_by_side):
        for y_point in range(n_by_side):
            points.append(((0.5+x_point)*equi_dist,
                           (0.5+y_point)*equi_dist))
    return points

def random_coord(n:int, map_size:int) -> list:
    """Génère des coordonnées aléatoire sur une surface carrée

    Génère des coordonnées sur une surface carré en utilisant une 
    distribution uniforme. 

    Args:
        n (int): Nombre de coordonnées à générer
        map_size (int): Aire de la surface à couvrir en km^2

    Return:
        list(tuple(float,float)): liste de coordonnées (x,y)
    """
    #TODO

def get_distance(coord1:tuple, coord2:tuple):
    """Cacule la distance L2 entre 2 points

    Args:
        cood1 (tuple(float,float)): Premier point (x,y)
        cood2 (tuple(float,float)): Deuxième point (x,y)

    Return:
        float: Distance L2
    """
    #TODO


