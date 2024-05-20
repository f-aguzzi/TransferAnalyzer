"""
Frequency response module.
"""
import numpy as np
import matplotlib.pyplot as plt

def __db(x):
    """
    Convert a linear amplitude to decibels (dB).

    Parameters:
    x (float or array-like): The linear amplitude(s) to be converted.

    Returns:
    float or array-like: The amplitude(s) in decibels.
    """
    return 20 * np.log10(x)

def plot_frequency_response(transfer_function, start_range=10e-2, end_range=10e2):
    """
    Plot the frequency response (both magnitude and phase) of a given transfer function.

    Parameters:
    G (function): The transfer function G(s), where s is a complex frequency.
    start_range (float, optional): The starting frequency for the plot (in rad/s). Default is 0.1.
    end_range (float, optional): The ending frequency for the plot (in rad/s). Default is 1000.0.

    Returns:
    None
    """
    omega = np.arange(0, end_range, start_range)

    module = [__db(abs(transfer_function(1j * x))) for x in omega]
    phase = [np.angle(transfer_function(1j * x), deg=True) for x in omega]

    omega_c_pos = np.min(np.abs(module))
    omega_c = omega[((np.where(np.abs(module) == omega_c_pos))[0])[0]]
    phi_c = phase[(((np.where(np.abs(module) == omega_c_pos))[0])[0])]

    # Module Diagram
    plt.figure()
    plt.grid(True, which="both")
    plt.semilogx(omega, module)
    plt.ylim([-80, 80])
    plt.xlim([start_range / 10, end_range])
    plt.scatter(omega_c, 0, color='orange', label=f'ω_c = {omega_c}')
    plt.legend()
    plt.title('Frequency response: module')
    plt.xlabel('ω (rad/s)')
    plt.ylabel('Module (dB)')
    plt.show()

    # Phase Diagram
    plt.figure()
    plt.grid(True, which="both")
    plt.semilogx(omega, phase)
    plt.ylim([-180, 180])
    plt.xlim([start_range / 10, end_range])
    plt.scatter(omega_c, phi_c, color='orange', label=f'ϕ_c = {phi_c}')
    plt.legend()
    plt.title('Frequency response: phase')
    plt.xlabel('ω (rad/s)')
    plt.ylabel('Phase (degrees)')
    plt.show()

