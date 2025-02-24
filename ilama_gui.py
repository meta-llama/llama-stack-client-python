import tkinter as tk
from tkinter import scrolledtext
import requests
import json

def send_request():
    # Načte vstupní hodnotu z textového pole
    input_val = entry.get()
    try:
        data = {"input_value": float(input_val)}
    except ValueError:
        text_area.insert(tk.END, "Zadejte platné číslo.\n")
        return

    # Odeslání POST požadavku na API endpoint
    try:
        response = requests.post("http://127.0.0.1:8080/process", json=data)
        result = response.json()
        # Vypíše odpověď ve formátu JSON (odsazené pro lepší čitelnost)
        text_area.insert(tk.END, json.dumps(result, indent=2) + "\n")
    except Exception as e:
        text_area.insert(tk.END, f"Chyba při odesílání požadavku: {str(e)}\n")

# Vytvoření hlavního okna
root = tk.Tk()
root.title("ILama API Test GUI")

# Rámec pro vstupní pole a tlačítko
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Zadejte vstupní hodnotu:")
label.pack(side=tk.LEFT)

entry = tk.Entry(frame, width=10)
entry.pack(side=tk.LEFT, padx=5)

button = tk.Button(frame, text="Odeslat", command=send_request)
button.pack(side=tk.LEFT)

# Textové pole se scrollbarem pro zobrazení odpovědí
text_area = scrolledtext.ScrolledText(root, width=60, height=20)
text_area.pack(padx=10, pady=10)

root.mainloop()
