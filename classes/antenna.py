from .ue import UE

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
    
        self.id = Antenna.id_counter
        Antenna.id_counter += 1
        self.ues = {}

    @classmethod
    def init_antenna_class(cls):
        Antenna.id_counter = 0

    def add_ue(self, ue:UE) -> None:
        self.ues[ue.id]=ue

    def calculate_pathloss(self, ue:UE, d_2D:float) -> None:
        """Calcul le pathloss par rapport à un UE

        Utilise la formule approprié de calcul de pathloss en fonction 
        du scénation du 3GPP utilisé et si le UE est en LOS ou NLOS.

        Args:
            ue (UE): UE de référence pour le calcul
            d_2D (float): Distance 2D entre l'antenne et le UE
        """
        #TODO: À remplir avec l'implémentation du module 1
   

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

        