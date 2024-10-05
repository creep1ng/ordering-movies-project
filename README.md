Este proyecto necesita tener un entorno configurado para correr Tk. Tk viene ya como una de las dependencias de este proyecto, pero quizás requiera de mayor ajuste en otros entornos.

En MacOs, se podría instalar con brew:

```bash
$ brew install python-tk
```

En entornos Windows no hay problemas. En linux podría ser necesario usar el gestor de paquetes del sistema para instalar tk.

De todos modos, recomiendo antes probar el setup normal de este proyecto:

```bash
cd ordering-movies-project
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python src/main.py
```
