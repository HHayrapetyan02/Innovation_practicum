from scipy.optimize import root
from Optimization_task.main_functions import GramianCalculator

class ParameterSolver:
    def __init__(self, target_norm_x, target_scalar_xy, target_norm_y, alpha):
        self.target_norm_x = target_norm_x
        self.target_scalar_xy = target_scalar_xy
        self.target_norm_y = target_norm_y
        self.alpha = alpha
        self.solution = None
        
    def _equations(self, params):
        """Система уравнений для решения"""
        beta, tau, tau_bar = params
        calculator = GramianCalculator(
            alpha = self.alpha,
            tau = tau,
            beta = beta, 
            tau_bar = tau_bar
        )
        return [
            calculator.norm_x_squared() - self.target_norm_x,
            calculator.scalar_product_xy() - self.target_scalar_xy,
            calculator.norm_y_squared() - self.target_norm_y
        ]
    
    def _solve_system(self, initial_guess):
        """Метод Левенберга-Марквардта для решения системы"""
        result = root(
            self._equations,
            initial_guess,
            method = 'lm'
        )
        if not result.success:
            raise ValueError(f"Решение не найдено: {result.message}")
        return result.x
    
    def solve(self, initial_guess=[0.5, 1.0, 0.2]):
        """Основной метод решения"""
        self.solution = self._solve_system(initial_guess)
        return self.solution
    
    @property
    def beta(self):
        if self.solution is None:
            raise ValueError("Сначала вызовите метод solve()")
        return self.solution[0]
    
    @property
    def tau(self):
        if self.solution is None:
            raise ValueError("Сначала вызовите метод solve()")
        return self.solution[1]
    
    @property
    def tau_bar(self):
        if self.solution is None:
            raise ValueError("Сначала вызовите метод solve()")
        return self.solution[2]

    def test_rev_functions():
        # Пример использования
        solver_1 = ParameterSolver(
            target_norm_x = 0.527256368946863,
            target_scalar_xy = 0.32640384048514937,
            target_norm_y = 0.398892037414181,
            alpha = 1.0
        )

        solver_2 = ParameterSolver(
            target_norm_x = 0.21514819967870435,
            target_scalar_xy = 0.18035275498303144,
            target_norm_y = 0.3104028963427644,
            alpha = 0.1
        )

        # Получение параметров через свойства
        solution = solver_1.solve(initial_guess=[0.5, 1.0, 0.2])
        print(f"beta: {solver_1.beta:.10f}")
        print(f"tau: {solver_1.tau:.10f}")
        print(f"tau_bar: {solver_1.tau_bar:.10f}")
