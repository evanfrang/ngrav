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
        vel[i] = [-vel_init*radius * np.sin(theta_i), \
                  vel_init*radius * np.cos(theta_i)]
    return pos, vel

def main():

    ### Inits ###
    num_bodies = 10
    small_mass = 0.01
    large_mass = 1.0
    rad_init = 1.0
    vel_init = 1.1
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
    system.a_thresh = 1000.
    system.dist_thresh = 10.
    system.collision_tolerance = 0.001
    system.integrator = integrator
    print("Starting Simulation ... ")
    system.run(T, dt)

    trajectory, velo_log = system.get_trajectories()

    ring_plot(trajectory, "results/ring.png")
    animate_ring(trajectory, "results/ring_ani.mp4")

    for i in range(len(bodies)):
        bodies[i].position = np.array(trajectory[i])[-1]
        bodies[i].velocity = -np.array(velo_log[i])[-1]

    system = System(bodies)
    forces = Gravity(G=G_param)
    integrator = RK4Integrator(forces.compute)
    system.a_thresh = 2000.
    system.dist_thresh = 20.
    system.collision_tolerance = 0.001
    system.integrator = integrator
    print("Starting Simulation Reverse ... ")
    T = 100.0
    system.run(T, dt)

    trajectory, velo_log = system.get_trajectories()

    ring_plot(trajectory, "results/ring_reverse.png")
    animate_ring(trajectory, "results/ring_ani_reverse.mp4")

if __name__ == '__main__':
    main()

