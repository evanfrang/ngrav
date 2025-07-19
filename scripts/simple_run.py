from ngrav.system import System
from ngrav.forces import Gravity
from ngrav.integrators import RK4Integrator
import numpy as np
from ngrav.body import Body
from ngrav.plotter import simple_plot
import json


def main():

    ###### CONFIG LOADING ######
    config_path = "configs/three_body.json"
    with open(config_path, 'r') as f:
        config = json.load(f)

    mass_config = config["bodies"]["masses"]
    position_config = config["bodies"]["positions"]
    velocity_config = config["bodies"]["velocities"]
    G_param = config["G"]
    T = config["sim_params"]["time"]
    dt = config["sim_params"]["dt"]
    plot_config = config["plot_params"]
    plot_params = [plot_config["names"], plot_config["colors"], \
                plot_config["radii"], plot_config["linewidth"]]
    filename = "results/" + config["filename"]

    bodies = [
        Body(id = i, mass=mass_config[i], position=position_config[i], \
            velocity=velocity_config[i]) for i in range(len(mass_config))
    ]

    # Instantiate system and components
    system = System(bodies)
    forces = Gravity(G=G_param)
    integrator = RK4Integrator(forces.compute)
    system.integrator = integrator
    system.run(T, dt)

    trajectory = system.get_trajectories()

    simple_plot(trajectory, plot_params, filename)

if __name__ == "__main__":
    main()