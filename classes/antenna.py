from .ue import UE


from math import sqrt, log10, pi, pow

from utilities.position import get_distance

"""Module d'antenne

Module définissant la classe antenne. Les fonctionnalité du gNodeB 
sont aussi implémenté dans cette classe.

"""

class Antenna:
    """Classe d'antenne

    Classe implémentant les fonctionnalité d'antenne et de gNodeB.

    Args:
        coord (tuple(float,float)): Coordonées des UEs (x,y)
        scenario (str): 'UMi' ou 'RMa'
        frequency (float): Fréquence centrale de transmission
        height (float): Hauteur de l'antenne

    Other attributes:
        id (int): Identifiant de l'antenne
        ues(dict(int:UE)): Dict associant les UEs de l'antenne à leur identifiant
        inactive_ues(list)

    """
    def __init__(self, coord:tuple, scenario:str, frequency:float, height:float):
        self.coord = coord
        self.scenario = scenario
        self.frequency = frequency
        self.height = height
        self.distances = {}
        self.number_ues = 0
        self.id = Antenna.id_counter
        Antenna.id_counter += 1
        self.ues = {}

    @classmethod
    def init_antenna_class(cls):
        Antenna.id_counter = 0

    def add_ue(self, ue:UE) -> None:
        self.ues[ue.id]=ue
        self.distances[ue.id] = get_distance(ue.coord,self.coord)
        self.number_ues += 1

    def calculate_pathloss(self, ue:UE, d_2D:float) -> None:
        """Calcul le pathloss par rapport à un UE

        Utilise la formule approprié de calcul de pathloss en fonction 
        du scénation du 3GPP utilisé et si le UE est en LOS ou NLOS.

        Args:
            ue (UE): UE de référence pour le calcul
            d_2D (float): Distance 2D entre l'antenne et le UE
        """
        #TODO: À remplir avec l'implémentation du module 1

        """Calcul le pathloss pour tous les UEs associés à l'antenne

        Utilise la formule approprié de calcul de pathloss en fonction
        du scénation du 3GPP utilisé et si le UE est en LOS ou NLOS.

        Args:
            ue (UE): UE de référence pour le calcul
            d_2D (float): Distance 2D entre l'antenne et le UE
        """
        # TODO
        c: float = pow(3.0 * 10.0, 8)

        hBS = 35.0

        hUT = 1.5

        hE = 1.0

        d3d = sqrt((self.height - ue.get_height()) ** 2 + d_2D ** 2)

        dBP = 2 * pi * hBS * hUT * self.frequency * 10**9/ c

        hBS_prime = hBS - hE

        hUT_prime = hUT - hE

        dBP_prime = 4 * hBS_prime * hUT_prime * self.frequency * 10**9 / c

        h = 5.0  # average building height

        W = 20

        if self.scenario == 'UMi':

            if ue.is_LOS:

                if  d_2D <= dBP_prime:

                    pl1 = 28.0 + 22 * log10(d3d) + 20 * log10(self.frequency)

                    pathloss = pl1

                    ue.set_pathloss(pathloss)

                elif dBP_prime <= d_2D <= 5000:

                    pl2 = 28.0 + 40 * log10(d3d) + 20 * log10(self.frequency) - 9 * log10(
                        dBP_prime ** 2 + (hBS - hUT) ** 2)

                    pathloss = pl2

                    ue.set_pathloss(pathloss)

                else:
                    pass

            else:

                if  d_2D <= 5000 :

                    if  d_2D <= dBP_prime:

                        pl1 = 28.0 + 22 * log10(d3d) + 20 * log10(self.frequency)

                        pathloss_LOS = pl1

                    else:

                        pl2 = 28.0 + 40 * log10(d3d) + 20 * log10(self.frequency) - 9 * log10(
                            dBP_prime ** 2 + (hBS - hUT) ** 2)

                        pathloss_LOS = pl2

                    pathloss_NLOS = 13.54 + 39.08 * log10(d3d) + 20 * log10(self.frequency) - 0.6 * (hUT - 1.5)

                    if pathloss_NLOS > 1000 :
                        pathloss_NLOS = 0

                    pathloss = max(pathloss_LOS,pathloss_NLOS)

                    ue.set_pathloss(pathloss)

                else :
                    pass

        else: ##RMa

            if ue.is_LOS:

                pl1 = 20.0 * log10(40.0 * pi * d3d * self.frequency / 3.0) + min(0.03 * pow(h, 1.72), 10) * log10(
                    d3d) - min(0.044 * pow(h, 1.72), 14.77) + 0.002 * log10(h) * d3d

                if  d_2D <= dBP:

                    pathloss = pl1

                    ue.set_pathloss(pathloss)

                elif dBP <= d_2D <= 10000:

                    pl2 = pl1 + 40 * log10(d3d / dBP)

                    pathloss = pl2

                    ue.set_pathloss(pathloss)

                else:
                    pass

            else:

                ### EN NLOS

                if  d_2D <= 5000:

                    pl1 = 20.0 * log10(40.0 * pi * d3d * self.frequency / 3.0) + min(0.03 * pow(h, 1.72), 10) * log10(
                        d3d) - min(0.044 * pow(h, 1.72), 14.77) + 0.002 * log10(h) * d3d

                    if  d_2D <= dBP:

                        pathloss_LOS = pl1

                    else :

                        pl2 = pl1 + 40 * log10(d3d / dBP)

                        pathloss_LOS = pl2

                    pathloss_NLOS = 161.04 - 7.1 * log10(W) + 7.5 * log10(h)  - (24.37 - 3.7 * pow(h/hBS,2))*log10(hBS) + (43.42 - 3.1 * log10(hBS))*(log10(d3d)-3) + 20 * log10(self.frequency) - 3.2 * pow(log10(11.75*hUT),2) - 4.97

                    if pathloss_NLOS > 1000:
                        pathloss_NLOS = 0

                    pathloss = max(pathloss_LOS,pathloss_NLOS)

                    ue.set_pathloss(pathloss)

                else:

                    pass

    def get_coord(self):
        return self.coord

    def get_user_distance(self, id):
        return self.distances[id]

    def get_ues(self):
        return list(self.ues.values())

    def get_id(self):
        return self.id
    ################ Module 2 ################

    def update(self, time_ms:int):
        """Met à jour l'antenne

        Gère les fonctions d'antennes liées au temps.
        À appeler à chque milliseconde. Cette méthode 
        appelle une méthode du même nom pour chaque UE
        associé à l'antenne.

        Args:
            time_ms (int): Temps simulé depuis le début de la 
                simulation (ms)
        """
        ra_attempts = {} #Contient les information des préambule et des UEs de manière à détecter une colision
        colliding_ues = [] #Permet d'identifier les UEs en colisions
        for ue in self.ues.values():
            new_packet = ue.update(time_ms)
            if new_packet:
                ue.results.pk_generated += 1
            #TODO: Détection de colision
            ##Détermine quels UE nécessite de se connecter
            ##Relève les ressources utilisées
            ##Si les même ressources sont utilisées, il y a colision


        for colliding_ue in colliding_ues:
            colliding_ue.connection_failed = True

        