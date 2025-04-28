import unittest

from Optimization_task.main_functions import GramianCalculator as Calc
from Optimization_task.reverse_functions import ParameterSolver as Solver

class TestGramianCalculations(unittest.TestCase):
    def setUp(self):
        # Тестовые параметры
        self.alpha = 1.0
        self.tau = 1.0
        self.beta = 0.5
        self.tau_bar = 0.2
        self.tolerance = 1e-4  # Допустимая погрешность

        # Инициализация калькулятора
        self.calculator = Calc(
            alpha = self.alpha,
            tau = self.tau,
            beta = self.beta,
            tau_bar = self.tau_bar
        )

    def test_forward_calculations(self):
        """Проверка прямых вычислений"""
        norm_x = self.calculator.norm_x_squared()
        scalar_xy = self.calculator.scalar_product_xy()
        norm_y = self.calculator.norm_y_squared()

    def test_inverse_calculations(self):
        """Проверка обратных вычислений"""
        target_norm_x = self.calculator.norm_x_squared()
        target_scalar_xy = self.calculator.scalar_product_xy()
        target_norm_y = self.calculator.norm_y_squared()

        # Решаем обратную задачу
        solver = Solver(
            target_norm_x=target_norm_x,
            target_scalar_xy=target_scalar_xy,
            target_norm_y=target_norm_y,
            alpha=self.alpha
        )
        
        # Вычисляем параметры
        try:
            solver.solve(initial_guess=[self.beta, self.tau, self.tau_bar])
        except ValueError as e:
            self.fail(f"Решение не найдено: {e}")

        # Проверяем точность восстановления параметров
        self.assertAlmostEqual(solver.beta, self.beta, delta = self.tolerance)
        self.assertAlmostEqual(solver.tau, self.tau, delta = self.tolerance)
        self.assertAlmostEqual(solver.tau_bar, self.tau_bar, delta = self.tolerance)

    def test_numerical_stability(self):
        """Проверка численной устойчивости"""
        # Разные начальные приближения
        initial_guesses = [
            [0.7, 1.2, 0.4],
            [0.4, 0.9, 0.25],
            [0.6, 0.8, 0.3]
        ]
        
        for guess in initial_guesses:
            with self.subTest(f"Initial guess {guess}"):
                solver = Solver(
                    target_norm_x = self.calculator.norm_x_squared(),
                    target_scalar_xy = self.calculator.scalar_product_xy(),
                    target_norm_y = self.calculator.norm_y_squared(),
                    alpha = self.alpha
                )
                solver.solve(initial_guess=guess)
                self.assertAlmostEqual(solver.beta, self.beta, delta=0.1)
                self.assertAlmostEqual(solver.tau, self.tau, delta=0.1)

if __name__ == '__main__':
    unittest.main()
