# 🎮 Snake sur matrice LED avec ESP32

Projet réalisé dans le cadre de la matière Yboost (2ème année Bachelor Informatique).  
L’objectif était de développer un projet en lien avec la spécialité que je souhaite rejoindre l’année prochaine (robotique).

J’ai choisi de recréer le jeu Snake sur une ESP32 avec matrices LED, un joystick pour les contrôles, et quelques bonus pour le fun !

## 🐍 Description du projet

Le jeu reprend le classique Snake mais adapté sur hardware voici ce que j'ai utilisé :  

* Matrices LED (au minimum 1 exigée, ici j’en ai utilisé 2 pour agrandir la zone de jeu).  

* Joystick analogique  pour les déplacements (plus intuitif et fluide que des boutons).    

* Buzzer pour jouer une petite musique au lancement et à la fin de la partie.  

Fonctionnalités de base : _(à retrouver dans le code snake.py)_

- Déplacement du serpent en temps réel avec le joystick.

- Apparition aléatoire de pommes à manger pour allonger le serpent.

- Gestion de la collision avec soi-même et avec les bords.

- Petit plus apporté ("apple beurk" => si le joueur mange cette pomme = Game Over)

Dans une seconde version du jeu _(à retrouver dans le code : SnakeVersionComplete.py)_, plusieurs types de pommes ont été ajoutés :

**Apple classique** → fait grandir le serpent (règle du jeu normal).

**Apple Beurk** → game over instantané si mangée.

**Apple Ghost** → rend le serpent invisible pendant quelques secondes (sa longueur est toujours comptée -> il peut toujours se mordre lui-même).

**Apple Boost** → augmente la vitesse du serpent (cumulable).

_Support modélisé sur Fusion360 et imprimé en 3D pour intégrer les matrices et le joystick (façon manette)._
![Image de la modélisation3D](image_modélisation3D_manette/.png)

## 📂 Structure du projet

snake.py → version de base du jeu (fonctionnelle).

SnakeVersionComplete.py → version améliorée avec différents types de pommes et bonus.

## Schéma de câblage

Voici le schéma de câblage utilisé pour connecter l’ESP32, les matrices LED, le joystick et le buzzer :  

![Schéma câblage](images/schema_cablage.png)

