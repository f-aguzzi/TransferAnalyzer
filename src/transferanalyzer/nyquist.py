"""
Nyquist module. Plot the Nyquist diagram of a given transfer function.
"""
import numpy as np
import matplotlib.pyplot as plt

def plot_nyquist_diagram(transfer_function, omega_range=(-500, 500), omega_step=0.009):
    """
    Plot the Nyquist diagram of a given transfer function.

    Parameters:
    G (function): The transfer function G(s), where s is a complex frequency.
    omega_range (tuple, optional): The range of frequency values for the plot (in rad/s). Default is (-500, 500).
    omega_step (float, optional): The step size for the frequency values. Default is 0.009.

    Returns:
    None
    """
    omega = np.arange(omega_range[0], omega_range[1], omega_step)
    complex_values = [transfer_function(1j * x) for x in omega]
    
    plt.plot(np.real(complex_values), np.imag(complex_values), color='blue')
    plt.plot(np.real(complex_values), -np.imag(complex_values), color='blue')
    plt.scatter(np.real(complex_values)[0], np.imag(complex_values)[0], color='orange', label='Start point')
    plt.scatter(-1, 0, color='red', label='(-1,0)')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.title('Nyquist Diagram')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.5)  # Add a horizontal dashed line at y=0
    plt.axvline(0, color='black', linestyle='--', linewidth=0.5)  # Add a vertical dashed line at x=0
    plt.legend()
    plt.grid(True)
    plt.show()
