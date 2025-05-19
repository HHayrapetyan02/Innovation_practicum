import numpy as np
import matplotlib.pyplot as plt

from time_optimal_trajectory import TOFrequencyCalculator

@staticmethod
def plot_all_dependencies():
    """Строит все три графика на одной фигуре"""
    fig, axes = plt.subplots(3, 1, figsize=(10, 15))
    
    # Фиксированные параметры для всех случаев
    alpha = 0.1
    fixed_params = [
        {'beta': 0.5, 'tau_bar': 0.2},  # Для зависимости от tau
        {'tau': 1.0, 'tau_bar': 0.2},    # Для зависимости от beta
        {'beta': 0.5, 'tau': 1.0}        # Для зависимости от tau_bar
    ]
    
    # Параметры для каждого субграфика
    settings = [
        {
            'var_name': 'tau',
            'var_values': np.linspace(0.1, 2.0, 20),
            'fixed_str': "beta=0.5, tau_bar=0.2",
            'color': 'blue'
        },
        {
            'var_name': 'beta',
            'var_values': np.linspace(0.1, 1.0, 20),
            'fixed_str': "tau=1.0, tau_bar=0.2",
            'color': 'red'
        },
        {
            'var_name': 'tau_bar',
            'var_values': np.linspace(0.1, 0.8, 20),
            'fixed_str': "beta=0.5, tau=1.0",
            'color': 'green'
        }
    ]
    
    for ax, setting, fixed in zip(axes, settings, fixed_params):
        omega_to_values = []
        for var_value in setting['var_values']:
            params = {
                'alpha': alpha,
                setting['var_name']: var_value,
                **fixed
            }
            calculator = TOFrequencyCalculator(**params)
            omega_to_values.append(calculator.calculate_omega_to())
        
        ax.plot(setting['var_values'], omega_to_values, 
                marker='o', linestyle='-', 
                color=setting['color'])
        ax.set_xlabel(setting['var_name'], fontsize=12)
        ax.set_ylabel("ω(TO)", fontsize=12)
        ax.set_title(
            f"Зависимость ω(TO) от {setting['var_name']} ({setting['fixed_str']})", 
            fontsize=12
        )
        ax.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_all_dependencies()
    
