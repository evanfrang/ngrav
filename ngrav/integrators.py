class RK4Integrator:
    def __init__(self, compute_acceleration_fn):
        self.acceleration = compute_acceleration_fn

    def step(self, state, masses, dt):
        x, v = state['positions'], state['velocities']

        def deriv(pos, vel):
            return vel, self.acceleration({'positions': pos, 'velocities': vel}, masses)

        k1_v, k1_a = deriv(x, v)
        k2_v, k2_a = deriv(x + 0.5*dt*k1_v, v + 0.5*dt*k1_a)
        k3_v, k3_a = deriv(x + 0.5*dt*k2_v, v + 0.5*dt*k2_a)
        k4_v, k4_a = deriv(x + dt*k3_v, v + dt*k3_a)

        x_new = x + dt/6.0 * (k1_v + 2*k2_v + 2*k3_v + k4_v)
        v_new = v + dt/6.0 * (k1_a + 2*k2_a + 2*k3_a + k4_a)

        return {'positions': x_new, 'velocities': v_new}, k4_a

