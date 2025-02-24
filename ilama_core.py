"""
ilama_core.py

Centrální modul ILamaLogic – řídicí jádro pro adaptivní syntetickou evoluci.
Podporuje dva režimy:
  - PNO: Prediktivní nelineární optimalizace se zpětnou vazbou
  - STAT: Statistická inference, Bayesovská aktualizace, Kalmanův filtr a adaptivní optimalizace

Tento modul slouží jako základní logická "krabička", kterou lze dále rozšiřovat o nové pluginy.
"""

import numpy as np
from scipy.optimize import minimize
from scipy.linalg import hessenberg

# ===== PNO moduly =====

class PNOValidationModule:
    """
    Validace vstupních dat na základě historických hodnot.
    Pokud vstup příliš vybočuje, provedeme korekci.
    """
    def __init__(self, history_data):
        self.history_data = history_data

    def validate(self, input_data):
        mean_value = np.mean(self.history_data)
        std_dev = np.std(self.history_data)
        if std_dev == 0:
            std_dev = 1e-6  # ochrana proti dělení nulou
        deviation = np.abs(input_data - mean_value)
        if deviation > 3 * std_dev:
            correction_factor = min(deviation / (5 * std_dev), 1)
            corrected_value = mean_value * (1 - correction_factor) + 80 * correction_factor
            return np.clip(corrected_value, 0, 100), True
        return np.clip(input_data, 0, 100), False

class PNOOptimizationModule:
    """
    Jednoduchá optimalizace vstupní hodnoty.
    """
    def optimize(self, input_data):
        return np.clip(input_data * 1.05, 0, 100)

class HeisenbergFilter:
    """
    Fyzikální omezení – omezuje hodnotu podle Heisenbergových principů.
    """
    def apply(self, input_data):
        return min(input_data, 95)

class FeedbackSystem:
    """
    Zpětná vazba – vyhlazuje výstup na základě předchozí hodnoty.
    """
    def adjust(self, input_data, previous_output):
        return (input_data + previous_output) / 2

class SynchronizationUnit:
    """
    Slučuje výstupy z validace, optimalizace a zpětné vazby.
    """
    def synchronize(self, validated, optimized, feedback):
        return np.clip(validated * 0.3 + optimized * 0.4 + feedback * 0.3, 0, 100)

class OutputUnit:
    """
    Zajišťuje, že konečný výstup je v platném rozsahu.
    """
    def generate_output(self, synced_value):
        return np.clip(synced_value, 0, 100)

# ===== STAT moduly =====

class StatValidationModule:
    """
    Statistická validace s učením z historie.
    """
    def __init__(self):
        self.history = []

    def validate(self, input_data):
        if len(self.history) < 5:
            self.history.append(input_data)
            return input_data, True
        mean_history = np.mean(self.history)
        std_dev = np.std(self.history)
        deviation = np.abs(input_data - mean_history)
        threshold = 2.5 * std_dev if std_dev > 0 else 5
        if deviation > threshold:
            corrected_value = np.clip(mean_history + np.random.normal(0, 7), 70, 90)
            self.history.append(corrected_value)
            return corrected_value, True
        self.history.append(input_data)
        return input_data, True

class BayesianInference:
    """
    Bayesovská inference pro adaptivní aktualizaci odhadu.
    """
    def __init__(self):
        self.prior_mean = 50
        self.prior_variance = 100

    def update(self, observed_value):
        likelihood_variance = 50
        posterior_mean = (self.prior_mean * likelihood_variance + observed_value * self.prior_variance) / (self.prior_variance + likelihood_variance)
        posterior_variance = 1 / (1 / self.prior_variance + 1 / likelihood_variance)
        self.prior_mean = posterior_mean
        self.prior_variance = posterior_variance
        return posterior_mean

class KalmanFilterModule:
    """
    Kalmanův filtr pro odstranění šumu a jemnější optimalizaci.
    """
    def __init__(self):
        self.x = 50
        self.P = 1
        self.Q = 0.1
        self.R = 1

    def update(self, measurement):
        K = self.P / (self.P + self.R)
        self.x = self.x + K * (measurement - self.x)
        self.P = (1 - K) * self.P
        return self.x

class AdaptiveOptimizer:
    """
    Adaptivní optimalizátor využívající historii pro optimalizaci.
    """
    def __init__(self):
        self.history = []

    def optimize(self, value):
        if len(self.history) > 10:
            mean_value = np.mean(self.history[-10:])
            optimized_value = (value + mean_value) / 2
        else:
            optimized_value = value
        self.history.append(optimized_value)
        return optimized_value

# ===== Doplňující funkce =====

def heisenberg_relation(position_uncertainty):
    """
    Výpočet neurčitosti hybnosti na základě neurčitosti polohy.
    """
    return 1.0 / (4 * np.pi * position_uncertainty)

def hessenberg_equation(matrix):
    """
    Vypočítá Hessenbergovu transformaci zadané matice a aplikuje HESSENBERG_CONSTANT.
    """
    H, _ = hessenberg(matrix, calc_q=True)
    return H * HESSENBERG_CONSTANT

def generate_report(history):
    """
    Vytvoří textový report z historie iterací optimalizace.
    """
    report = "\n\nHistorie výkonu algoritmu:\n"
    for i, entry in enumerate(history, 1):
        report += f"Iterace {i}: MSE = {entry['mse']:.6f}\n"
    return report

def objective_function(params, x, y_actual):
    """
    Nelineární cílová funkce optimalizace.
    """
    a, b, c = params
    y_pred = a * np.sin(b * x) + c
    mse = np.mean((y_actual - y_pred) ** 2)
    return mse

def predictive_nonlinear_optimization(x, y_actual, initial_params, max_iterations=100):
    """
    Prediktivní nelineární optimalizace s iterativní zpětnou vazbou.
    """
    history = []
    params = initial_params.copy()
    for iteration in range(max_iterations):
        result = minimize(objective_function, params, args=(x, y_actual), method='L-BFGS-B')
        params = result.x
        mse = result.fun
        history.append({"iteration": iteration + 1, "params": params, "mse": mse})
        y_pred = params[0] * np.sin(params[1] * x) + params[2]
        residuals = y_actual - y_pred
        y_actual = y_actual - 0.5 * residuals
        if mse < 1e-5:
            break
    return params, history

def logistic_map(r, x0, iterations):
    """
    Simulace logistické mapy jako modelu chaosu.
    """
    results = [x0]
    x = x0
    for _ in range(iterations):
        x = r * x * (1 - x)
        results.append(x)
    return results

# ===== Hlavní řídicí jednotka ILamaLogic =====

class ILamaLogic:
    """
    Hlavní logika ILama, která integruje základní moduly a adaptivní optimalizaci.
    Režim 'PNO' využívá prediktivní nelineární optimalizaci a fyzikální filtry,
    zatímco režim 'STAT' využívá statistickou validaci, Bayesovskou inferenci, Kalmanův filtr a adaptivní optimalizaci.
    """
    def __init__(self, mode='PNO', history_data=None):
        self.mode = mode.upper()
        if self.mode == 'PNO':
            if history_data is None:
                history_data = np.array([10, 12, 15, 14, 16, 18, 17])
            self.validation = PNOValidationModule(history_data)
            self.optimizer = PNOOptimizationModule()
            self.heisenberg = HeisenbergFilter()
            self.feedback = FeedbackSystem()
            self.sync = SynchronizationUnit()
            self.output = OutputUnit()
            self.previous_output = 20
        elif self.mode == 'STAT':
            self.validation = StatValidationModule()
            self.bayes = BayesianInference()
            self.kalman = KalmanFilterModule()
            self.optimizer = AdaptiveOptimizer()
            self.previous_output = 50
        else:
            raise ValueError("Neznámý režim: použijte 'PNO' nebo 'STAT'")

    def process(self, input_value):
        """
        Zpracuje vstupní data podle zvoleného režimu a vrátí strukturovaný výstup.
        """
        if self.mode == 'PNO':
            validated, corr = self.validation.validate(input_value)
            optimized = self.optimizer.optimize(validated + (input_value / 10))
            filtered = self.heisenberg.apply(optimized)
            adjusted = FeedbackSystem().adjust(filtered, self.previous_output)
            synced = SynchronizationUnit().synchronize(validated, optimized, adjusted)
            final_output = OutputUnit().generate_output(synced)
            final_validated, final_corr = self.validation.validate(final_output)
            self.previous_output = final_validated
            return {
                "input": input_value,
                "validated": validated,
                "corrected": corr,
                "optimized": optimized,
                "filtered": filtered,
                "adjusted": adjusted,
                "synced": synced,
                "final_output": final_output,
                "final_validated": final_validated,
                "final_corrected": final_corr,
                "mode": "PNO"
            }
        elif self.mode == 'STAT':
            validated, _ = self.validation.validate(input_value)
            bayesian_pred = self.bayes.update(validated)
            kalman_pred = self.kalman.update(bayesian_pred)
            optimized = self.optimizer.optimize(kalman_pred)
            self.previous_output = optimized
            return {
                "input": input_value,
                "validated": validated,
                "bayesian_prediction": bayesian_pred,
                "kalman_prediction": kalman_pred,
                "optimized_output": optimized,
                "mode": "STAT"
            }

# ===== Testovací blok (lze spustit pro základní ověření) =====

if __name__ == '__main__':
    # Testovací data
    x_data = np.linspace(0, 10, 100)
    y_actual = 2.0 * np.sin(1.5 * x_data) + 1.0 + np.random.normal(0, 0.1, len(x_data))
    initial_params = [1.0, 1.0, 1.0]

    # Spustíme prediktivní nelineární optimalizaci a vygenerujeme report
    optimal_params, history = predictive_nonlinear_optimization(x_data, y_actual, initial_params)
    print("Optimalizované parametry:", optimal_params)
    print(generate_report(history))

    # Test základní adaptivní logiky ILama v režimu PNO
    ilama = ILamaLogic(mode='PNO', history_data=np.array([10, 12, 15, 14, 16, 18, 17]))
    result = ilama.process(42)
    print("\nVýstup ILamaLogic (PNO režim) pro vstup 42:")
    for key, value in result.items():
        print(f"{key}: {value}")

    # Test statistického režimu
    ilama_stat = ILamaLogic(mode='STAT')
    result_stat = ilama_stat.process(42)
    print("\nVýstup ILamaLogic (STAT režim) pro vstup 42:")
    for key, value in result_stat.items():
        print(f"{key}: {value}")
