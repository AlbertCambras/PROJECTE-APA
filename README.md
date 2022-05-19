# PROJECTE-APA

**NOMÉS EL PRIMER COP**
=======================

**1. Fer un FORK del repositori.**  

  1.1 Aneu a https://github.com/AlbertCambras/PROJECTE-APA i apreteu FORK (Crea una copia al vostre compte)  

**2. GIT CLONE**
  2.1  
  ```bash
  git clone https://github.com/User/PROJECTE-APA.git  
  ```
  2.2 COMPROVAR URL DEL REPOSITORI  
  
    2.2.1 git remote -v  
    
  2.3 AFEGIR URL DEL REPOSITORI ORIGINAL  
  ```bash
     git remote add upstream https://github.com/AlbertCambras/PROJECTE-APA
  ```
  
**SEMPRE**
===========

1. OBTINDRE ELS CANVIS DEL REPOSITORI 
```BASH
$ git pull -r upstream main
```
2. CREAR UNA BRANCA  
Cada cop que vulguem pujar un canvi, es pujarà en un branca a part i després mesclem a la branca principal.
Això es fa així per si hi ha fallos veure on comença a tindre'ls.
Llavors, cada cop que fem alguna cosa nova, fem una branca i la pujem. Després de puja-la s'ha d'anar al repo original i ficar-la en el main.
Si voleu podem editar directament el main però crec que per tema de si estem fent coses a la vegada i eso, és millor així.
2.1 Creació de la branca
```
$ git checkout -b nombre-rama
```
3. PUJAR EL COMMIT  

```BASH
// Agreguem els arxius a git.
git add .
// Fem un commit
git commit -m "WHAT YOU CHANGED?"
git push upstream nombre-rama

```
4. ANAR A GITHUB
Aneu al vostre github i hi haurà una opció de PULL REQUEST apreteu... 
Això és per pujar els canvis al repositori general.
Aviseu-me quan ho feu perquè crec que haig de ser jo qui faci una cosa.
