import math
from scipy.optimize import root

class GramianCalculator:
    def __init__(self, alpha, beta, tau, tau_bar):
        self.alpha = alpha
        self.beta = beta
        self.tau = tau
        self.tau_bar = tau_bar
        self._validate_parameters()

    def _validate_parameters(self):
        if abs(self.tau_bar) >= 1:
            raise ValueError("tau_bar должен быть в диапазоне (-1, 1)")
        if self.beta <= 0:
            raise ValueError("beta должен быть положительным")

    def update_parameters(self, alpha=None, tau=None, beta=None, tau_bar=None):
        if alpha is not None: self.alpha = alpha
        if tau is not None: self.tau = tau
        if beta is not None: self.beta = beta
        if tau_bar is not None: self.tau_bar = tau_bar
        self._validate_parameters()

    def _common_calculations(self):
        self.sqrt_term = math.sqrt(self.tau**2 + self.beta**2)
        self.arsinh_tau_beta = math.asinh(self.tau / self.beta)
        self.atanh_tau_bar = math.atanh(self.tau_bar)

    def norm_x_squared(self):
        self._common_calculations()
        terms = [
            (1/4) * self.tau**4,
            (self.beta**2 * self.atanh_tau_bar**2 + (5*self.beta**2)/4 + 1) * self.tau**2,
            -(self.beta**2 * self.atanh_tau_bar + self.tau_bar) * self.tau,
            (1/4) * (4*self.beta**4 + 3*self.beta**2 + 1 + self.beta**4 * self.atanh_tau_bar**2 - 2*self.beta**2 * self.tau_bar * self.atanh_tau_bar),
            -self.tau**2 * self.sqrt_term,
            (1/2) * (3*self.beta**2 * self.atanh_tau_bar + self.tau_bar) * self.tau * self.sqrt_term,
            -2 * self.beta**2 * self.sqrt_term,
            -2 * self.beta**2 * self.tau**2 * self.atanh_tau_bar * self.arsinh_tau_beta,
            self.beta**2 * self.tau * self.arsinh_tau_beta,
            -(self.beta**2 / 2) * (self.beta**2 * self.atanh_tau_bar - self.tau_bar) * self.arsinh_tau_beta,
            -(3 * self.beta**2 / 2) * self.tau * self.sqrt_term * self.arsinh_tau_beta,
            self.beta**2 * self.tau**2 * self.arsinh_tau_beta**2,
            (self.beta**4 / 4) * self.arsinh_tau_beta**2
        ]
        return (self.alpha**(-4)) * sum(terms)

    def scalar_product_xy(self):
        self._common_calculations()
        terms = [
            (1/2) * self.tau**3,
            (self.beta**2 * self.atanh_tau_bar**2 + self.beta**2/2 + 1) * self.tau,
            -(self.beta**2 / 2) * self.sqrt_term * self.arsinh_tau_beta,
            (1/2) * (self.beta**2 * self.atanh_tau_bar + self.tau_bar) * self.sqrt_term,
            -(3/2) * self.tau * self.sqrt_term,
            (self.beta**2 / 2) * self.arsinh_tau_beta,
            -(1/2) * (self.beta**2 * self.atanh_tau_bar + self.tau_bar),
            self.beta**2 * self.tau * self.arsinh_tau_beta**2,
            -2 * self.beta**2 * self.tau * self.atanh_tau_bar * self.arsinh_tau_beta
        ]
        return (self.alpha**(-3)) * sum(terms)

    def norm_y_squared(self):
        self._common_calculations()
        terms = [
            self.tau**2,
            -2 * self.sqrt_term,
            self.beta**2 * self.arsinh_tau_beta**2,
            -2 * self.beta**2 * self.atanh_tau_bar * self.arsinh_tau_beta,
            self.beta**2 * self.atanh_tau_bar**2 + self.beta**2 + 1
        ]
        return (self.alpha**(-2)) * sum(terms)

    def test_main_functions():        
        calculator_1 = GramianCalculator(
            alpha = 1.0,
            beta = 0.5,
            tau = 1.0,
            tau_bar = 0.2
        )

        calculator_2 = GramianCalculator(
            alpha = 1.0,
            beta = 0.7,
            tau = 1.0,
            tau_bar = 0.4
        )

        print("||x||² =", calculator_1.norm_x_squared())
        print("⟨x,y⟩ =", calculator_1.scalar_product_xy())
        print("||y||² =", calculator_1.norm_y_squared())
