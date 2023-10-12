# Un nouveau projet ?
- prendre connaissance du brief / cdc / sijet ...
- comprendre / analyser / choix techniques / retro planning / UX-UI: uml
- git + .gitignore
    - partager avec rcarlier
    - https://github.com/github/gitignore/
- créer un dossier
- venv + activer + package + "requirements.txt"
- 1er commit
- code ... test... code ... git... code ... test... code ... git... 


# Projet Password Generator

## Création venv
bash
mac / linux
python3 -m venv venv
source venv/bin/activate

#win python3 -m venv venv
.\venv\Scripts\activates.ps1
## packages
sh
#installer les dépendances
win : .\venv\Scripts\pip install pyside6
./venv/bin/pip install pyside6

#geler les dépendances
win : .\venv\Scripts\pip freeze > requirements.txt
./venv/bin/pip freeze > requirements.txt 