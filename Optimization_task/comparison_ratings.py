import numpy as np
import matplotlib.pyplot as plt

from time_optimal_trajectory import TOFrequencyCalculator

class CalculatorGraphics:
    @staticmethod
    def plot_all_dependencies_comparison():
        """Строит три графика с двумя линиями каждый"""
        fig, axes = plt.subplots(3, 1, figsize=(12, 18))
        
        configs = [
            {  # График 1: Зависимость от τ
                'var_name': 'tau',
                'var_range': np.linspace(0.1, 2.0, 20),
                'variations': [
                    {'beta': 0.5, 'tau_bar': 0.2, 'label': 'beta=0.5, tau_bar=0.2'},
                    {'beta': 0.6, 'tau_bar': 0.25, 'label': 'beta=0.6, tau_bar=0.25'}
                ],
                'fixed': {'alpha': 0.1}
            },
            {  # График 2: Зависимость от beta
                'var_name': 'beta',
                'var_range': np.linspace(0.2, 1.0, 20),
                'variations': [
                    {'tau': 1.0, 'tau_bar': 0.2, 'label': 'tau=1.0, tau_bar=0.2'},
                    {'tau': 1.2, 'tau_bar': 0.3, 'label': 'tau=1.2, tau_bar=0.3'}
                ],
                'fixed': {'alpha': 0.1}
            },
            {  # График 3: Зависимость от tau_bar
                'var_name': 'tau_bar',
                'var_range': np.linspace(0.15, 0.7, 20),
                'variations': [
                    {'beta': 0.5, 'tau': 1.0, 'label': 'beta=0.5, tau=1.0'},
                    {'beta': 0.6, 'tau': 0.9, 'label': 'beta=0.6, tau=0.9'}
                ],
                'fixed': {'alpha': 0.1}
            }
        ]

        colors = ['blue', 'orange']
        line_styles = ['-', '--']

        for ax, config in zip(axes, configs):
            for i, variation in enumerate(config['variations']):
                omega_values = []
                calc_params = {k: v for k, v in variation.items() if k != 'label'}
                
                for var_value in config['var_range']:
                    params = {
                        **config['fixed'],
                        **calc_params,  # Используем очищенные параметры
                        config['var_name']: var_value
                    }
                    calculator = TOFrequencyCalculator(**params)
                    omega_values.append(calculator.calculate_omega_to())
                
                ax.plot(config['var_range'], omega_values,
                        color=colors[i],
                        linestyle=line_styles[i],
                        linewidth=1.5,
                        marker='' if i == 0 else '^',
                        markersize=4,
                        label=variation['label'])  # label остается только для легенды

            ax.set_xlabel(config['var_name'], fontsize=12)
            ax.set_ylabel("ω(TO)", fontsize=12)
            ax.set_title(f"Зависимость ω(TO) от {config['var_name']}", fontsize=14)
            ax.grid(True, alpha=0.3)
            ax.legend(fontsize=10)

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    CalculatorGraphics.plot_all_dependencies_comparison()
