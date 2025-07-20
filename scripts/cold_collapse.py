import numpy as np
from ngrav.system import System
from ngrav.forces import Gravity
from ngrav.integrators import RK4Integrator
from ngrav.body import Body
from ngrav.plotter import ring_plot, animate_ring

def ring_init(N, radius=1.0, vel_init=1.0):
    """
    return x,y and vx,vy for N bodies around a ring
    """
    pos = [[0.,0.]] * N
    vel = [[0.,0.]] * N
    for i in range(N):
        theta_i = i * 2 * np.pi / N
        pos[i] = [radius * np.cos(theta_i), radius * np.sin(theta_i)]
        #vel[i] = [-vel_init*radius * np.sin(theta_i), \
        #          vel_init*radius * np.cos(theta_i)]
        vel[i] = [vel_init*radius * np.cos(theta_i), \
                  vel_init*radius * np.sin(theta_i)]
    return pos, vel

def main():

    ### Inits ###
    num_bodies = 100
    small_mass = 0.01
    large_mass = 2.0
    rad_init = 10.0
    vel_init = 0.05
    ring_pos, ring_vel = ring_init(num_bodies, rad_init, vel_init)
    G_param = 1.0
    T = 100.0
    dt = 0.01

    bodies = [Body(id = 0, mass=large_mass, position=[0.0,0.0], 
                   velocity=[0.0,0.0])]
    for i in range(num_bodies):
        bodies.append(Body(id = i+1, mass=small_mass, position=ring_pos[i], 
                           velocity=ring_vel[i]))
        
    system = System(bodies)
    forces = Gravity(G=G_param)
    integrator = RK4Integrator(forces.compute)
    system.a_thresh = np.inf
    system.dist_thresh = 50.
    system.collision_tolerance = 0.0
    system.integrator = integrator
    print("Starting Simulation ... ")
    system.run(T, dt)

    trajectory, velo_log = system.get_trajectories()

    ring_plot(trajectory, "results/ring_collapse.png")
    animate_ring(trajectory, "results/ring_collapse_ani.mp4")

if __name__ == '__main__':
    main()

