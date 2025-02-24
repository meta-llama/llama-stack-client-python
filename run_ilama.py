#!/usr/bin/env python
import sys
from ilama_core import ILamaLogic

def main():
    # Pokud není zadán argument, použijeme výchozí vstupní hodnotu
    if len(sys.argv) < 2:
        print("Použití: python run_ilama.py <input_value>")
        print("Nebyl zadán vstupní parametr, použit výchozí hodnota 42.")
        input_value = 42.0
    else:
        try:
            input_value = float(sys.argv[1])
        except ValueError:
            print("Chyba: Vstupní hodnota musí být číslo.")
            sys.exit(1)

    # Vytvoříme instanci ILamaLogic v režimu 'PNO'
    ilama = ILamaLogic(mode='PNO', history_data=None)
    
    # Zavoláme metodu process, která zpracuje vstupní hodnotu
    result = ilama.process(input_value)
    
    # Vypíšeme výsledky
    print("Výsledek ILamaLogic.process:")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    main()
