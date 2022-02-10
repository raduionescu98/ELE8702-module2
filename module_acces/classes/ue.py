
from enum import Enum, auto
from random import randint

"""UE module

Module defining the UE class, which represent a user device.

"""

class UE:
    """User Device class

    Class containing user information and functionnalities.

    """
    def __init__(self) -> None:

        self.id = UE.id_counter
        UE.id_counter += 1

    @classmethod
    def init_ue_class(cls):
        cls.id_counter = 0

    #To complete with module 1 implementation

    ################ Module 2 ################
    
    @classmethod
    def add_access_info(cls, access_info):
        cls.inactivity_timer = access_info['inactivity_timer']
        cls.scs = access_info['scs']
        cls.ra_parameters = access_info['ra_parameters']
        cls.backoff_time = access_info['backoff_time']
        cls.number_of_preambles = access_info['number_of_preambles']
        cls.max_inactive_ues = access_info['max_inactive_ues']
        cls.rach_structure = access_info['rach_structure']
        

    def add_packet_list(self, packet_list):
        self.packet_info = packet_list
        if packet_list:
            self._next_packet = packet_list.pop(0)
        else:
            self._next_packet = (float('inf'),0)

    def _compute_connection_time(self, ra_parameters: dict) -> int:
        """Connection time computation method.

        This method returns the time that a UE needs in order to go
        from RRC_IDLE to RRC_CONNECTED. 

        Args:
            ra_parameters (dict): Dictionaty containings input 
                parameters

        Returns:
            int: 
                Time to connect (ms).
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
        


    def _select_preamble(self) -> int:
        """Select a valid preamble (Boutin Aug 2019)

        Selects a preamble format from the set of available preamble
        of the application and reselects a preamble if it lands on
        a reserved signature (N/A).
        
        INCOMPLETE!!!!

        """
        #preamble_index = randint(0, number_of_possible_preamble)
        #time_index = randint(0,number_of_possible_time_modulation)
        return (preamble_index, time_index)


    def update(self, time_ms:int):
        """Update the UE to the current time

        Manage UEs time related functionnalities. 
        To be called each millisecond. Mainly manages UE 
        states.

        Args:
            time_ms (int): Time since the start of the simulation in 
                milliseconds.

        """
        # If the UE is connected, it either sends a packet or resumes to IDLE.
        if self.status == UEStatus.RRC_CONNECTED: pass
            # The packet is inactive for too long -> set to IDLE mode.

            # A packet is waiting to be sent -> send the packet.

            
        # The UE is in IDLE or INACTIVE state but needs to connect to the 
        # network.
        if self.status in (UEStatus.RRC_IDLE, UEStatus.RRC_INACTIVE): pass

        # If the UE is connecting, it can complete or repeat an RA attempt.
        if self.status == UEStatus.CONNECTING: pass
            # Collision: Wait an additional backoff time.

            # No collision: connect.


class UEStatus(Enum):
    #Possible status for user equipments.
    RRC_CONNECTED = auto()  # can send a packet at any time
    CONNECTING = auto()     # currently performing a RACH attempt
    RRC_IDLE = auto()       # disconnected; cannot sent a packet
    RRC_INACTIVE = auto()       # Idle, but with faster reconnection (5G)
