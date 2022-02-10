import matplotlib.pyplot as plt

import seaborn as sns
#sns.set()

def plot_positions(ue_pos:dict, antenna_pos:list):
    """Plot position of antennas and UEs

    Args:
        ue_pos (dict{str:list(tuple)}): Dict of UEs coordinates lsit
            mapped by application.
        antenna_pos (list(tuple)): List of antenna coordinate

    """
    #Zip to format [[x],[y]]
    ues_xy = {}
    for app, values in ue_pos.items():
        ues_xy[app] = list(zip(*values))
    antenna_xy = list(zip(*antenna_pos))

    #Plot
    fig, ax = plt.subplots()
    ue_scatters = []
    apps = []
    for app, values in ues_xy.items():
        ue_scatters.append(ax.scatter(values[0], values[1],  marker = 'x'))
        apps.append(app)
    antenna_scatter = ax.scatter(antenna_xy[0], antenna_xy[1], marker='o')
    plt.legend((*ue_scatters,antenna_scatter),
           (*apps,'Antenna'))


    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_title('Location of UEs and antennas')

    plt.show()

def plot_pathloss(pathloss_values:list):
    f = plt.figure()
    sns.kdeplot(pathloss_values, shade = True)
    sns.distplot(pathloss_values)
    plt.xlabel('pathloss (dB)')
    plt.title('Histogram of pathloss')
    plt.show()