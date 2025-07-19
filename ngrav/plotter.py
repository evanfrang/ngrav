import matplotlib.pyplot as plt

def simple_plot(trajectory, plot_params, filename):
    """
    Simple 2D plot of the bodies and orbits

    Args:
        trajectory (np.ndarray): (# steps, # bodies, 2 dimensions),
        plot_params (np.array): [names, colors, radii, trails],
        filename (str): "results/output.png"

    Returns:
        saves to file no output
    """
    num_bodies = trajectory.shape[1]
    if not plot_params:
        for i in range(num_bodies):
            plt.plot(trajectory[:, i, 0], trajectory[:, i, 1])
        plt.gca().set_aspect('equal')
        plt.savefig(filename)
        return

    names = plot_params[0]
    colors = plot_params[1]
    radii = plot_params[2]
    trails = plot_params[3]

    for i in range(num_bodies):
        plt.plot(trajectory[:, i, 0], trajectory[:, i, 1], color=colors[i], \
                 label=names[i], markersize=radii[i], linewidth=radii[i])
    plt.legend()
    plt.gca().set_aspect('equal')
    plt.savefig(filename)

    