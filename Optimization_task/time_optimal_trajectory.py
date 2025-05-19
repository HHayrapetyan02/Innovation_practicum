import math

class TOFrequencyCalculator:
    def __init__(self, alpha, beta, tau, tau_bar):
        self.alpha = alpha
        self.beta = beta
        self.tau = tau
        self.tau_bar = tau_bar
        
    def calculate_omega_to(self):
        """Вычисляет ω(TO) по восстановленной формуле"""
        tau = self.tau
        beta = self.beta
        tau_bar = self.tau_bar

        # Основные компоненты выражения
        term1 = - (tau**5) / 40
        term2 = - (1/6) * ( (71/36)*beta**2 + beta**2 * math.atanh(tau_bar)**2 + 1 ) * tau**3
        term3 = (1/4) * (beta**2 * math.atanh(tau_bar) + tau_bar) * tau**2
        term4 = - (1/72) * (9*beta**4 * math.atanh(tau_bar)**2 + 27*beta**2 + 56*beta**4 - 18*beta**2*tau_bar*math.atanh(tau_bar) + 9) * tau
        term5 = (1/2160) * ( (1024*beta**4 - 163*beta**2 + 54)*tau_bar - 675*beta**4*math.atanh(tau_bar) )
        term6 = (1/18) * (3*beta**2*tau_bar - 5*beta**4*math.atanh(tau_bar)) * math.sqrt(tau**2 + beta**2)
        term7 = (11 * beta**2 / 16) * tau * math.sqrt(tau**2 + beta**2)
        term8 = - (1/36) * (13*beta**2*math.atanh(tau_bar) + 3*tau_bar) * tau**2 * math.sqrt(tau**2 + beta**2)
        term9 = (1/8) * tau**3 * math.sqrt(tau**2 + beta**2)
        term10 = (5 * beta**4 / 16) * math.asinh(tau / beta)
        term11 = (beta**2 / 4) * (beta**2 * math.atanh(tau_bar) - tau_bar) * tau * math.asinh(tau / beta)
        term12 = - (beta**2 / 4) * tau**2 * math.asinh(tau / beta)
        term13 = (beta**2 / 3) * tau**3 * math.atanh(tau_bar) * math.asinh(tau / beta)
        term14 = (5 * beta**4 / 18) * math.sqrt(tau**2 + beta**2) * math.asinh(tau / beta)
        term15 = (13 * beta**2 / 36) * tau**2 * math.sqrt(tau**2 + beta**2) * math.asinh(tau / beta)
        term16 = - (beta**4 / 8) * tau * (math.asinh(tau / beta))**2
        term17 = - (beta**2 / 6) * tau**3 * (math.asinh(tau / beta))**2

        # Суммируем все члены
        result = (
            term1 + term2 + term3 + term4 + term5 + term6 + term7 + term8 + term9 +
            term10 + term11 + term12 + term13 + term14 + term15 + term16 + term17
        )
        return -result
    
    def test_optimal_trajectory():
        calculator = TOFrequencyCalculator(
            alpha=0.1,
            beta = 0.5,
            tau = 1.0,
            tau_bar = 0.2
        )

        print(calculator.calculate_omega_to())



if __name__ == "__main__":
    TOFrequencyCalculator.test_optimal_trajectory()        
