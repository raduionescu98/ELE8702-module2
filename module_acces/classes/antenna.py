from .ue import UE

"""Antenna module

Module defining the antenna class. gNodeB functionnalities are also 
implemented in antennas.

"""

class Antenna:
    """Antenna class

    Class implementing antennas and gNodeB functionnalities.


    """
    def __init__(self):
    
        self.id = Antenna.id_counter
        Antenna.id_counter += 1


    @classmethod
    def init_antenna_class(cls):
        cls.id_counter = 0

    #To complete with module 1 implementation
   

    ################ Module 2 ################

    def update(self, time_ms:int):
        """Update the antenna to the current time

        Manage antennas time related functionnalities. 
        To be called each millisecond. Considers antenna 
        objects have a ues attribute which is a dict of 
        UEs mapped by ID.

        Args:
            time_ms (int): Time since the start of the simulation in 
                milliseconds.

        """
        ra_attempts = {}
        colliding_ues = []
        for ue in self.ues.values():
            new_packet = ue.update(time_ms)
            if new_packet:
                ue.results.pk_generated += 1
            #Detect collision

        #Manage collisions

        