
"""Result module

Utilities to manage results, including an AppResults class

"""

class AppResults():
    """Application results container

    Class used to record results for each application

    Attributes:
        app_name (str): Name of the application
        n_ra_attempt (int): Number of rach attempt
        n_collision (int): Number of collision (1 collision per UE in 
            collision)
        pk_generated (int): Number of generated packets. A packet is 
            considered generates when it is ready to be sent.
        cummul_ra_time (int): Cummulative time, in ms UEs of the app spent in 
            ra_attempt in ms (consideres backoff time and multiple 
            attempt if collision)
        n_ra_time (int): Number of completed ra_attempt.
        

    """
    def __init__(self, app_name):
        self.app_name = app_name
        self.n_rach_attempt = 0
        self.n_collision = 0
        self.pk_generated = 0
        self.cummul_ra_time = 0
        self.n_ra_time = 0

    def __add__(self,results):
        new_results = AppResults(self.app_name)
        new_results.n_rach_attempt = self.n_rach_attempt \
                                   + results.n_rach_attempt
        new_results.n_collision = self.n_collision \
                                + results.n_collision
        new_results.pk_generated = self.pk_generated \
                                 + results.pk_generated
        new_results.cummul_ra_time = self.cummul_ra_time \
                                 + results.cummul_ra_time
        new_results.n_ra_time = self.n_ra_time \
                                 + results.n_ra_time
        return(new_results)
        
    def add_RA_time(self, ra_time:int):
        """Records random access procedure time
        """
        self.cummul_ra_time += ra_time
        self.n_ra_time += 1


    def print_results(self):
        """Print results

        """
        print('**********Results**********')
        print('App: {}'.format(self.app_name))
        print('Number of RACH attempt: {}'.format(self.n_rach_attempt))
        print('Number of collision: {}'.format(self.n_collision))
        print('Number of packet generated: {}'.format(self.pk_generated))
        print('Average RACH time: {}'.format(self.cummul_ra_time/self.n_ra_time))
        print('***************************')
