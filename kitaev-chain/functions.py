import numpy as np # type: ignore
from tqdm import tqdm # type: ignore
from qiskit.opflow import Suzuki # type: ignore

# Time evolution operator for a Hamiltonian H and time time_param
def compute_U(H, t):
    U = (H * t).exp_i()
    return U

def exact_time_evolution(H,observable, initial_state, times, num_sites):
    evo_matrix = np.zeros((len(times), num_sites))
    var_matrix = np.zeros(len(times))

    for i, time in enumerate(tqdm(times)):
        for j, oi in enumerate(observable):
            # Compute the time evolution operator U(time) at time time
            U = compute_U(H, time)
            # Compute the evolution of the initial state
            final_state = U @ initial_state
            # Compute the expectation value n_i
            evo_matrix[i, j] = np.abs((final_state.adjoint() @ oi @ final_state).eval())
        var_matrix[i] = (
            np.abs((final_state.adjoint() @ (sum(observable) @ sum(observable)) @ final_state).eval())
            - np.abs((final_state.adjoint() @ sum(observable) @ final_state).eval()) ** 2
        )
    return evo_matrix, var_matrix

def exact_time_evolution_energy(H, initial_state, times, num_sites):
    evo_matrix = np.zeros((len(times)))
    var_matrix = np.zeros(len(times))
    
    for i, time in enumerate(tqdm(times)):
        # Compute the time evolution operator U(time) at time time
        U = compute_U(H, time)
        # Compute the evolution of the initial state
        final_state = U @ initial_state
        # Compute the expectation value n_i
        evo_matrix[i] = np.abs((final_state.adjoint() @ H @ final_state).eval())
    
    return evo_matrix, var_matrix

def exact_time_evolution_density(H, initial_state, times, num_sites):
    evo_matrix = np.zeros((len(times)))
    var_matrix = np.zeros(len(times))
    
    for i, time in enumerate(tqdm(times)):
        # Compute the time evolution operator U(time) at time time
        U = compute_U(H, time)
        # Compute the evolution of the initial state
        final_state = U @ initial_state
        # Compute the expectation value n_i
        evo_matrix[i] = (final_state @ final_state.adjoint()).eval()
    
    return evo_matrix, var_matrix

def compute_U_trot(H, time, trotter_steps, order=1):
    U_trot = Suzuki(trotter_steps, order=order).convert(time * H)
    return U_trot

def trotter_evolution(H, observable, initial_state, times, num_sites, trotter_steps):
    evo_matrix_trot = np.zeros((len(times), num_sites))
    for i, time in enumerate(tqdm(times)):
        for j, oi in enumerate(observable):
            U = compute_U_trot(H, time, trotter_steps)
            final_state = U @ initial_state
            evo_matrix_trot[i, j] = np.abs(
                (final_state.adjoint() @ oi @ final_state).eval()
            )
    return evo_matrix_trot