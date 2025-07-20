import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def simple_plot(trajectory, plot_params, filename):
    """
    Simple 2D plot of the bodies and orbits

    Args:
        trajectory (dict): (key is body_id, x, y in N steps),
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


def animate_plot(trajectory, plot_params, filename, fps=20):
    """
    Animate orbits over time.

    Args:
        trajectory (dict): (key is body_id, x, y in N steps),
        plot_params (np.array): [names, colors, radii, linewidth],
        filename (str): "results/output.png"
        fps (int): frames of animation

    Returns:
        saves to file no output
    """

    names = plot_params[0]
    colors = plot_params[1]
    radii = plot_params[2]
    linewidth = plot_params[3]
    trail_length = 50
    
    num_bodies = len(trajectory.keys())
    Nt = len(trajectory[0])

    fig, ax = plt.subplots()
    lines = []
    lines = [ax.plot([], [], 'o', color=colors[i])[0] for i in range(num_bodies)]
    
    all_positions = np.concatenate([np.array(trajectory[i]) for i in range(num_bodies)])
    xmin, ymin = np.min(all_positions, axis=0)
    xmax, ymax = np.max(all_positions, axis=0)
    ax.set_xlim(xmin - 1, xmax + 1)
    ax.set_ylim(ymin - 1, ymax + 1)

    def update(frame):
        start_frame = max(0, frame - trail_length)
        for i, line in enumerate(lines):
            trail_positions = np.array(trajectory[i])[start_frame : frame + 1]
            x_data = trail_positions[:, 0]
            y_data = trail_positions[:, 1]
            line.set_data(x_data, y_data)
        return lines

    stride = 20
    frames = range(0, Nt, stride)
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
    ani.save('results/orbits.mp4', fps=fps, dpi=150)

    