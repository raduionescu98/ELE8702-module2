from classes.antenna import Antenna
from classes.ue import UE, UEStatus
from input import INPUT_DICT1 as INPUT_DICT
from utilities.file_io import read_csv_index_table
from utilities.results import AppResults
from utilities.stochastic import gen_packets

import numpy as np
from scipy.stats import uniform

"""Main module

"""
if __name__ == '__main__':
    ################ Module 1 ################

    #Ajouter le main du module 1 en exclant les graphs

    ################ Module 2 ################
    # Il n'y a pas de modifications nécessaire à effectuer 
    # dans le main. Les modifications à effectuer sont dans 
    # antennes et ue.

    #Read PRACH Tables
    rach_table = read_csv_index_table(INPUT_DICT['rach_table_path'])

    #Fetch access_info
    access_info = {name:INPUT_DICT[name] for name in (
        'inactivity_timer',
        'scs',
        'ra_parameters',
        'backoff_time',
        'number_of_preambles',
        'max_inactive_ues')
        } 

    access_info['rach_structure'] = rach_table[
        INPUT_DICT['prach_config_index']]

    UE.add_access_info(access_info)

    #Create results per app
    app_results = {}
    for app_name in INPUT_DICT['apps']:
        app_results[app_name] = AppResults(app_name)

    #Generate random number for fraction decision
    rand_num = uniform.rvs(size=len(ues))
    for i, ue in enumerate(ues):
        #Generate packets
        ue.add_packet_list(gen_packets(INPUT_DICT['simulation_time']*1000,
            INPUT_DICT['apps'][ue.app_name]['gen_distribution'],
            INPUT_DICT['apps'][ue.app_name]['len_distribution']))
        #Manage initial connection
        if rand_num[i] <= INPUT_DICT['apps'][ue.app_name][
            'fraction_connected']:
            ue.status = UEStatus.RRC_CONNECTED
        else:
            ue.status = UEStatus.RRC_IDLE
        #Assign results objects
        ue.results = app_results[ue.app_name]

    #Update loop
    for time_ms in range(INPUT_DICT['simulation_time']*1000):
        #Go through all antennas to update
        for antenna in antennas.values():
            antenna.update(time_ms)
    tot_results = AppResults('all')
    for results in app_results.values():
        tot_results = tot_results + results
        results.print_results()
    tot_results.print_results()


    print('mehdi')

