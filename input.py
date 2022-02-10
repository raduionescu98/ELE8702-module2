"""Input file

Inputs are format as dict.

"""

INPUT_DICT1={
    'nb_antennas':16, #must be a square of an int
    'antenna_height':10,
    'apps':{
        'app1': {
            'nb_ues':100,
            #Access
            'gen_distribution': {
                'type': 'uniform', #interval [a,b]
                'a': 40, #ms
                'b':100 #ms
            },
            'len_distribution': {
                'type': 'uniform',
                'a': 50, #ms
                'b':100 #ms
            },
            'fraction_connected':0.5
        },
        'app2': {
            'nb_ues':200,
            #Access
            'gen_distribution': {
                'type': 'exponential',
                'scale': 100 #ms (scale = mean = 1/lambda)
            },
            'len_distribution': {
                'type': 'exponential',
                'scale': 100 #ms
            },
            'fraction_connected':0.5
        }
    },
    'ue_height': 1.5,
    'map_size': 5, #km^2
    'scenario': 'UMi',
    'frequency': 28, #GHz
    'antenna_gain': 35,
    #Access
    'rach_table_path': 'data/rachFrameStructure_FR2_TDD.csv',
    'simulation_time': 10, #in seconds
    'inactivity_timer': 50,
    'scs': 60, #kHz
    'ra_parameters': {
        'RA_length_idle':50, #ms
        'RA_length_innactive': 20 #ms
    },
    'max_inactive_ues': 10, #per antenna
    'backoff_time': 100,
    'prach_config_index': 5,
    'number_of_preambles': 54,

}

INPUT_DICT2={
    'nb_antennas':16, #must be a square of an int
    'antenna_height':35,
    'apps':{
        'app1': {
            'nb_ues':100,
            #Access
            'gen_distribution': {
                'type': 'uniform', #interval [a,b]
                'a': 40, #ms
                'b':100 #ms
            },
            'len_distribution': {
                'type': 'uniform',
                'a': 50, #ms
                'b':100 #ms
            },
            'fraction_connected':0.5
        },
        'app2': {
            'nb_ues':200,
            #Access
            'gen_distribution': {
                'type': 'exponential',
                'scale': 100 #ms (scale = mean = 1/lambda)
            },
            'len_distribution': {
                'type': 'exponential',
                'scale': 100 #ms
            },
            'fraction_connected':0.5
        }
    },
    'ue_height': 1.5,
    'map_size': 12, #km^2
    'scenario': 'RMa',
    'frequency': 0.9, #GHz
    'antenna_gain': 45,
    #Access
    'rach_table_path': 'data/rachFrameStructure_FR1_FDD.csv',
    'simulation_time': 10, #in seconds
    'inactivity_timer': 50,
    'scs': 15, #kHz
    'ra_parameters': {
        'RA_length_idle':50, #ms
        'RA_length_innactive': 20 #ms
    },
    'max_inactive_ues': 10, #per antenna
    'backoff_time': 100,
    'prach_config_index': 22,
    'number_of_preambles': 54,
}
