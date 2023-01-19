# Projet 11 -  Améliorez une application Web Python par des tests et du débogage


# Installation
####  Cloner ce dépôt : 
```
git clone https://github.com/batshanti/Projet11.git
cd Projet11/
```
####  Créer un environnement virtuel pour le projet :
(Linux or Mac)
```
 python3 -m venv venv
 source venv/bin/activate
```
(Windows)
```
 python -m venv env
 env\Scripts\activate
```
#### Installer les packages :
```
pip install -r requirements.txt
```
# Lancement de l'application
#### lancer l'application :
(Linux or Mac)
```
 export FLASK_NAME=server
 flask run
```
(Windows)
```
$env:FLASK_APP = "server.py"
flask run
```

#### lancer l'application en mode TEST / *Ce mode utilise une base de donnée différente pour réaliser les tests avec Pytest :*
(Linux or Mac)
```
export FLASK_NAME=server
ENV=TEST flask run
flask run
```
(Windows)
```
$env:FLASK_APP = "server.py"
$env:ENV = "TEST"
flask run
```
#### Utiliser l'application :
Se rendre à l'adresse http://127.0.0.1:5000/

# Test

Les tests unitaires, d'intégrations, fonctionnels et de performances se situent dans le dossier tests.

#### Tests unitaires / Test d'intégration / Tests fonctionnels  :
```
pytest -v
```
#### Couverture des tests
Générer un rapport de couverture:
```
pytest --cov=. --cov-report html
```
#### Test de performance
```
cd tests/performance_test
locust
```
Se rendre à l'adresse http://localhost:8089
