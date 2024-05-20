import numpy as np
import matplotlib.pyplot as plt
from mpmath import invertlaplace

def plot_impulse_response(transfer_function, end_range=30, precision=250, inversion_method='cohen'):
    """
    Plot the impulse response of a given transfer function.

    Parameters:
    G (function): The transfer function G(s), where s is a complex frequency.
    end_range (float, optional): The time span for the plot (in seconds). Default is 30.
    precision (int, optional): The number of samples. Default is 250.
    inversion_method (str, optional): The inversion method to use. Default is 'cohen'.

    Returns:
    None
    """
    x = np.arange(0.01, end_range, end_range / precision)
    f_inv = [invertlaplace(transfer_function, t, method=inversion_method) for t in x]

    plt.grid(True, which="both", axis="both")
    plt.plot(x, f_inv)
    plt.title('Impulse response')
    plt.xlabel('Time (s)')
    plt.ylabel('Output amplitude')
    plt.show()

def plot_step_response(transfer_function, step_amplitude=1, end_range=30, precision=250, inversion_method='cohen'):
    """
    Plot the step response of a given transfer function.

    Parameters:
    G (function): The transfer function G(s), where s is a complex frequency.
    step_amplitude (float, optional): The amplitude of the step input. Default is 1.
    end_range (float, optional): The time span for the plot (in seconds). Default is 30.
    precision (int, optional): The number of samples. Default is 250.
    inversion_method (str, optional): The inversion method to use. Default is 'cohen'.

    Returns:
    None
    """
    def step(s):
        return step_amplitude * transfer_function(s) / s

    x = np.arange(0.01, end_range, end_range / precision)
    f_inv = [invertlaplace(step, t, method=inversion_method) for t in x]

    plt.grid(True, which="both", axis="both")
    plt.plot(x, f_inv)
    plt.title('Step response')
    plt.xlabel('Time (s)')
    plt.ylabel('Output amplitude')
    plt.show()
