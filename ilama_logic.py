import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.linalg import hessenberg
import os
import smtplib
from email.mime.text import MIMEText
from getpass import getpass
from flask import Flask, request, jsonify

# === Konstanty ===
HESSENBERG_CONSTANT = 0.0003  # Konstanta použitá v Hessenbergově transformaci

# --- PNO moduly ---
class PNOValidationModule:
    """
    Validace vstupních dat pomocí historických hodnot.
    Pokud je vstup příliš vzdálen od průměru, provede se korekce.
    """
    def __init__(self, history_data):
        self.history_data = history_data

    def validate(self, input_data):
        mean_value = np.mean(self.history_data)
        std_dev = np.std(self.history_data)
        if std_dev == 0:
            std_dev = 1e-6  # Ochrana proti dělení nulou
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

# --- Fyzikální moduly ---
class HeisenbergFilter:
    """
    Fyzikální omezení – zajišťuje horní mez hodnoty.
    """
    def apply(self, input_data):
        return min(input_data, 95)

class FeedbackSystem:
    """
    Zpětná vazba – iterativní vyhlazení výstupu.
    """
    def adjust(self, input_data, previous_output):
        return (input_data + previous_output) / 2

class SynchronizationUnit:
    """
    Synchronizace výsledků validace, optimalizace a zpětné vazby.
    """
    def synchronize(self, validated, optimized, feedback):
        return np.clip(validated * 0.3 + optimized * 0.4 + feedback * 0.3, 0, 100)

class OutputUnit:
    """
    Generuje konečný výstup v platném rozsahu.
    """
    def generate_output(self, synced_value):
        return np.clip(synced_value, 0, 100)

# --- Statistické moduly ---
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
        posterior_variance = 1 / (1/self.prior_variance + 1/likelihood_variance)
        self.prior_mean = posterior_mean
        self.prior_variance = posterior_variance
        return posterior_mean

class KalmanFilterModule:
    """
    Kalmanův filtr pro dynamickou optimalizaci.
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
    Adaptivní optimalizátor využívající historii.
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

# --- Doplňující funkce ---
def heisenberg_relation(position_uncertainty):
    """
    Výpočet neurčitosti hybnosti na základě neurčitosti polohy.
    """
    return 1.0 / (4 * np.pi * position_uncertainty)

def hessenberg_equation(matrix):
    """
    Vypočítá Hessenbergovu transformaci zadané matice a aplikuje HESSENBERG_CONSTANT.
    """
    H, Q = hessenberg(matrix, calc_q=True)
    return H * HESSENBERG_CONSTANT

def generate_report(history):
    """
    Vytvoří textový report o iteracích optimalizace.
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
    residuals = y_actual - y_pred
    mse = np.mean(residuals ** 2)
    return mse

def predictive_nonlinear_optimization(x, y_actual, initial_params, max_iterations=100):
    """
    Prediktivní nelineární optimalizace s iterativní zpětnou vazbou.
    """
    history = []
    params = initial_params
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

# --- Hlavní řídicí jednotka ILama ---
class ILamaLogic:
    """
    Tato třída integruje PNO a statistické moduly a slouží jako hlavní logika ILama.
    Může pracovat v režimu 'PNO' nebo 'STAT'.
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

# --- Flask API endpoint pro testování ---
app = Flask(__name__)
LOGIC_MODE = 'PNO'  # Zvolte 'PNO' nebo 'STAT'
if LOGIC_MODE.upper() == 'PNO':
    ilama = ILamaLogic(mode='PNO', history_data=np.array([10, 12, 15, 14, 16, 18, 17]))
else:
    ilama = ILamaLogic(mode='STAT')

@app.route('/process', methods=['POST'])
def process_request():
    data = request.json
    if not data or "input_value" not in data:
        return jsonify({"error": "Chybí nebo je neplatná hodnota input_value"}), 400
    try:
        input_value = float(data["input_value"])
    except ValueError:
        return jsonify({"error": "input_value musí být číslo"}), 400
    result = ilama.process(input_value)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
