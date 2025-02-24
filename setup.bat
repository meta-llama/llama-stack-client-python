@echo off
REM Nastavovací skript pro projekt "llama-stack-client-python"
REM Ujisti se, že tento skript spouštíš z kořenového adresáře projektu.

REM 1. Vytvoření virtuálního prostředí, pokud ještě neexistuje
if not exist ".venv" (
    echo Vytvářím virtuální prostředí...
    python -m venv .venv
) else (
    echo Virtuální prostředí již existuje.
)

REM 2. Aktivace virtuálního prostředí
call .venv\Scripts\activate

REM 3. Aktualizace pipu
echo Aktualizuji pip...
python -m pip install --upgrade pip

REM 4. Instalace závislostí ze souboru requirements.txt
echo Instalace závislostí z requirements.txt...
pip install -r requirements.txt

REM 5. Instalace doplňkových balíčků, které mohou být potřeba pro testování
echo Instalace dodatečných balíčků (pytest, respx, dirty_equals)...
pip install pytest respx dirty_equals

REM 6. (Volitelně) Pokud používáš pip-compile a zdrojový soubor je requirements.in, můžeš odkomentovat následující řádek:
REM pip-compile requirements.in

REM 7. Spuštění jednotkových testů pomocí pytest
echo Spouštím testy...
pytest tests/

echo.
echo Nastavení dokončeno. Stiskni libovolnou klávesu pro ukončení.
pause
