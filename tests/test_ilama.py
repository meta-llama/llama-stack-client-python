# tests/test_ilama.py

import numpy as np
from ilama_core import ILamaLogic

def test_process_pno():
    ilama = ILamaLogic(mode='PNO', history_data=np.array([10, 12, 15, 14, 16, 18, 17]))
    result = ilama.process(42)
    # Ověříme, že výstupy jsou v očekávaném rozsahu
    assert 0 <= result["final_output"] <= 100
    assert result["mode"] == "PNO"

def test_process_stat():
    ilama = ILamaLogic(mode='STAT')
    result = ilama.process(42)
    # Zkontrolujeme, že režim STAT vrací odpovídající klíče
    assert "bayesian_prediction" in result
    assert "kalman_prediction" in result

if __name__ == "__main__":
    test_process_pno()
    test_process_stat()
    print("Všechny testy proběhly úspěšně.")
