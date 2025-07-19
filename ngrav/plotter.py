import matplotlib.pyplot as plt
import numpy as np

def simple_plot(trajectory, plot_params, filename):
    """
    Simple 2D plot of the bodies and orbits

    Args:
        trajectory (np.ndarray): (# steps, # bodies, 2 dimensions),
        plot_params (np.array): [names, colors, radii, linewidth],
        filename (str): "results/output.png"

    Returns:
        saves to file no output
    """

    names = plot_params[0]
    colors = plot_params[1]
    radii = plot_params[2]
    linewidth = plot_params[3]
    
    num_bodies = len(trajectory.keys())

    for i in range(num_bodies):
        traj_temp = np.array(trajectory[i])
        plt.plot(traj_temp[:, 0], traj_temp[:, 1], color=colors[i], \
                markersize=linewidth[i], linewidth=linewidth[i])
        circle = plt.Circle((traj_temp[-1, 0], traj_temp[-1, 1]), \
                        radii[i], label=names[i], color=colors[i])
        plt.gca().add_patch(circle)
    plt.gca().set_aspect('equal')
    plt.savefig(filename)


    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.gca().set_aspect('equal')
    plt.savefig(filename, bbox_inches='tight')

    