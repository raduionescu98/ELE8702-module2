
from enum import Enum, auto
from random import randint

"""Module de UE

Module définissant la classe UE, qui représente l'appareil d'un usager.

"""

class UE:
    """Classe UE

    Classe définissant les information et les fonctionnalité
    d'un UE.

    Args:
        app_name (str): Nom de l'application
        coord (tuple(float,float)): Coordoner du UE (x,y)
        height (float): Hauteur du UE
        is_LOS (bool): Indique si la ligne de vu (LOS) du UE est obstrué 
            (par rapport à l'antenne)
        pathloss (float): Pathloss en dB entre l'antenne et le UE
        recv_power (float): Puissance reçue en dBm

    """
    def __init__(self, 
                 app_name:str, 
                 coord:tuple, 
                 height:float) -> None:
        self.app_name = app_name
        self.coord = coord
        self.height = height

        self.is_LOS = True
        self.pathloss = float('inf')
        self.recv_power = -float('inf')
        self.id = UE.id_counter
        UE.id_counter += 1

    def __repr__(self):
        return 'App:{};Coord:{}'.format(self.app_name, self.coord)

    @classmethod
    def init_ue_class(cls):
        cls.id_counter = 0

    #To complete with module 1 implementation

    ################ Module 2 ################
    
    @classmethod
    def add_access_info(cls, access_info):
        """Initialise les attributs d'accès des UEs"""
        cls.inactivity_timer = access_info['inactivity_timer']
        cls.scs = access_info['scs']
        cls.ra_parameters = access_info['ra_parameters']
        cls.backoff_time = access_info['backoff_time']
        cls.number_of_preambles = access_info['number_of_preambles']
        cls.max_inactive_ues = access_info['max_inactive_ues']
        cls.rach_structure = access_info['rach_structure']

    def is_valid_preamble_subframe(self,
                                   rach_structure: list,
                                   subframe: int) -> bool:
        """Détermine la validité d'un subframe pour le RA

        Vérifie qu'un UE peut faire un RA en fonction de sa 
        sign
        """
        #TODO
        

    def add_packet_list(self, packet_list):
        """Ajoute une liste d'information permettant de générer des paquets

        Les informations de paquets sont un tuple indiquant le temps
        de génération et la longeur du paquet en bits. Le prochain 
        paquet à envoyé est enregistré dans _next_paquet, les autres 
        dans paquet_info.
        
        """
        self.packet_info = packet_list
        if packet_list:
            self._next_packet = packet_list.pop(0)
        else:
            self._next_packet = (float('inf'),0)

    def _compute_connection_time(self, ra_parameters: dict) -> int:
        """Méthode permettant de déterminer le temps de connexion

        Cette méthode retourne le temps qu'un UE nécessite afin de 
        passe du mode RRC_IDLE ou RRC_INACTIVE au mode RRC_CONNECTED 

        Args:
            ra_parameters (dict): dictionnaire des paramètre d'entré

        Returns:
            int: Temps de connexion (ms).
        """
        if self._previous_status == UEStatus.RRC_IDLE:
            connection_time = ra_parameters['RA_length_idle']
        elif self._previous_status == UEStatus.RRC_INACTIVE:
            connection_time = ra_parameters['RA_length_innactive']
        else:
            print('Previous state: {}'.format(self._previous_status))
            raise ValueError('Previous state should be either idle or '
                            + 'inactive')
        return connection_time
        
    def connect(self, time_ms):
        """Tentative de connexion à un UE idle
        
        Cette méthode sélectionnne un préabule and et regarde s'il peut
        être à time_ms. S'il peut être envoyé, il change à l'état 
        connecting et détermine le temps de fin du RA et et incrémente 
        le nombre de rach attempt dans les résultats.

        Args:
            time_ms (int): Temps simulé depuis le début de la 
                simulation (ms)
        
        """
        #TODO
        pass


    def _select_preamble(self, valid_slots) -> int:
        """Sélectionne un préambule valide

        Sélectionne un format de préambule aléatoirement parmis 
        l'ensemble de préambule possible.

        Args:
            valid_slots (list): List d'entier représentant les 
                slots de transmission valides.

        Return:
            (int,int,int): Trois index représentant respectivement 
                le préambule, la modulation temporel et le slot.

        """
        #TODO
        return (preamble_index, time_mod_index, slot_index)

    def _send_packet(self):
        """Transmet le prochain packet à l'antenne

        """
        packet = self._next_packet
        if self.packet_info:
            self._next_packet = self.packet_info.pop(0)
        else:
            self._next_packet = (float('inf'),0)
        return packet

    def set_disconnected(self) -> None:
        """Effectue la déconnexion d'un UE
        
        Permet au UE de passer du mode CONNECTED au mode 
        IDLE ou INACTIVE dépendemment du nombre du UE 
        inactive déjà connecté
        """
        #TODO


    def update(self, time_ms:int):
        """Met à jour le UE à time_ms

        Gère les fontionnaliés temporelle du UE. À appeler
        à chaque milliseconde. Gère principalement les états 
        du UE.

        Args:
            time_ms (int): Temps simulé depuis le début de la 
                simulation (ms)


        """

        # Si le UE est connecté, envoie un paquet ou revient enmode IDLE/INACTIVE
        if self.status == UEStatus.RRC_CONNECTED: pass
            # Si le paquet est inactive pendant trop longtemps -> déconnexion

            # S'il y a un paquet à transmettre -> transmet le paquet

            
        # Le UE est en mode IDLE ou INACTIVE mais nécessite une connection
        if self.status in (UEStatus.RRC_IDLE, UEStatus.RRC_INACTIVE): pass

        # Si le UE est en train de se connecter, vérifier s'il a terminé sa procédure de connexion
        if self.status == UEStatus.CONNECTING: pass
            # Collision -> Attend un temps de backoff avant de se reconnecter

            # Pas de collision -> se connecte


class UEStatus(Enum):
    #État de connexion possible pour les UEs
    RRC_CONNECTED = auto()  # Peut transmettre des paquets
    CONNECTING = auto()     # Est en train de performer un RACH attempt
    RRC_IDLE = auto()       # Déconnecté, ne peut pas transmettre de paquets
    RRC_INACTIVE = auto()       # Comme idle, mais se reconnecte plus rapidement