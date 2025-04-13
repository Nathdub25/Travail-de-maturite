# Journal de bord
## 02.02.25
Voici les premières paroles que j'écris sur ce journal. Après le premier rendez-vous que j'ai eu avec mon mentor, j'ai réussi tant de bien que mal à faire en sorte que ce document sur lequel j'écris soit synchronisé sur mon compte Github. 
### Objectifs fixés ###
Pour l'instant, j'aimerais m'informer sur le sujet. Mon but est de programmer un jeu sur lequel je vais pouvoir jouer au bao game, un jeu africain, sur l'ordinateur. Je compte m'informer via des tutos youtube de programmation et pouvoir commencer à programmer dès la rentrée des vacances. Après, je m'informerai tout au long du projet afin de pouvoir perfectionner ou de répondre à des questions que je me poserai.

J'aimerais aussi pouvoir consacrer à ce projet du temps, et je compte 1 jour par semaine où je pourrai travailler dessus.
## 03.02.25
### "Programme" du TM
Avant toute chose, structurer mon plan de travail serait utile : juste avoir un fil rouge sur lequel il y aura les étapes en gros pour que je ne me perde pas ou que je ne sache pas quoi faire.

Les étapes sont donc les suivantes:

*L'aspect logique:* Pour commencer, j'aimerais me concentrer sur l'aspect logique de cette programmation. Avant de me documenter sur comment je vais programmer, il faut d'abord que je sache ce que je vais programmer. Pour ça, il faut les régles du jeu, le principe du jeu et des conditions afin que le robot informatique puisse participer à la partie.

*la documentation:* Une fois que j'ai la logique, il faudrait donc que je la traduise en quelque sorte en language python, et que je fasse en sorte que le jeu que je compte programmer soit exactement pareil au jeu réel. Mais pour faire ça, il faut d'abord que j'acquière les connaissances nécessaires pour pouvoir le programmer, ce jeu. Cette période sera plus centrée sur l'apprentissage du code et permettra de répondre aux questions : **comment programmer une interface visuel qui interfère avec le joueur?, comment programmer un robot capable de déplacer virtuellement les pièces?, comment programmer un jeu nécéssitant un adversaire imaginaire et comment l'adversaire peut être aperçu sur l'interface visuel?** ...en gros

*La programmation:* Afin que je puisse mettre en pratique tout ce que j'aurai appris pendant l'étape d'avant, je comptais d'abord programmer quelques petits jeux qui seront des exemples de codes pour chacune des questions que je me serais posées comme ça je pourrai aussi voir à quoi m'attendre lorsque je commencerai à programmer le jeu bao. 
Une fois que toutes ces étapes seront accomplies, il ne me manquera plus grand chose pour commencer à programmer. Il faudra donc que je'obtienne l'algorythme, le programme-->(traduction de la logique), les installations nécessaires pour l'interface visuel, et que je sache les dernières modifications personnalisées sur le jeu.

*La mise en pratique:* Cette étape ne sera pas très longue et consistera à "expérimenter" mon programme avec des proches autour. Cela, je trouve, permettra d'obtenir des avis externes sur le jeu et de pouvoir faire quelques modifications pour finaliser le projet. 

*La rédaction et la préparation à la présentation orale:* Une fois que toutes ces étapes seront accomplies, la rédaction du document annexe ne devrait pas prendre trop de temps. Il faut juste penser à y mettre l'introduction du jeu, ce que j'ai du faire et le résultat final, expliqué. La présentation attendra le moment de rendu du document annexe.
### Objectifs fixés
Je pense que pour les rendez-vous avec mon mentor, ce serait pas une mauvaise idée qu'ils soient fixés en tout cas entre chaque étape, afin que je puisse être sûr de pouvoir accéder à la prochaine. En terme de temps, je dirai que je n'ai pas spécifiquement d'attente, du moment que j'y consacre minimum 1 jour par semaine sur ce projet. Sinon je pense travailler dès que j'ai du temps, de toute façon.




## 10.02.25
Je vais donc commencer par la logique :
### règles et principe du jeu
Le jeu bao est un jeu traditionel africain qui se joue sur un plateau de 32 trous à 2 joueurs, donc 16 trous chacun, chacun des 16 trous se trouvant devant le joueur. Dans les trous, on va y retrouver des graines ou n'importe quoi d'assez petit et la position de départ est comme ceci (2 graines par trou):

![position de départ](https://thumbs.dreamstime.com/b/antique-boa-mancala-tradition-jeu-de-soci%C3%A9t%C3%A9-africain-vintage-bao-sculpt%C3%A9-plateau-en-bois-avec-des-boules-graines-baobab-212523322.jpg)

Le but du jeu va donc être de capturer toutes les pièces de l'adversaire qui se situent sur les 2 dernières rangées de 8 trous. 
Comment on joue? 

Un joueur commence. Il choisit un trou de la deuxième rangée. Il prend alors toutes les graines de ce trou et les redistribue 1 par 1, 1 graine par trou dans le sens contraire des aiguilles d'une montre, sans compter le trou dans lequel le joueur a pris les graines. Lorsque la dernière graine a atteint le dernier trou, il se peut qu'il y ait plusieurs graines dans ce trou. Dans ce cas, on répète le mécanisme jusqu'à ce que la dernière graine attérisse dans un trou vide.

#### Capture 
Si la dernière graine attérrit dans un trou vide de la deuxième rangée (la rangée du haut), le joueur capture toutes les graines de l'adversaire se situant dans le trou d'en face (donc le trou de la même position, de la 3ème rangée). Les graines capturées peuvent être mises sur le côté et ne seront plus utilisées jusqu'à la fin de la partie. **Attention** la capture ne fonctionne que si la dernière graine attérit dans la deuxième rangée et que si le trou de l'adversaire en face contient des graines. 

#### Fin d'un tour
Le tour se finit lorsque la dernière graine du joueur attérit dans un trou vide, ou après la capture si une capture a lieu. Dans ce cas, le tour revient au joueur suivant, qui lui aura les mêmes conditions.

#### Fin de la partie
La partie se termine lorsqu'un joueur capture la dernière graine de son adversaire. Le nombre de graines restantes ou perdues du gagnant n'est pas pris en compte.


Le principe du jeu est donc de faire en sorte de capturer plus de graines que d'en perdre. Il s'agit de savoir bien compter, prévoir les coups à l'avance et d'avoir une certaine stratégie qui permettra de capturer et de défendre, comme aux échecs.



### Conditions (aspect logique)
Je me disais que je pourrais programmer 3 niveaux, afin que tout le monde puisse jouer et trouver son niveau et aussi qu'il y ait un robot imbattable, qui aurait un programme plus complexe, une véritable machine.
Une fois toutes les règles expliquées et programmées, le robot devra :

#### niveau débutant

1. Choisir le gain maximal
    - gain max = capture maximale parmis les 16 coups
    - Si plusieurs gain max identique, choisir le premier

 Si le gain maximal = 0 : 

 2. Calculer la perte maximale
    - perte max = gain max de l'adversaire
    - Si plusieurs perte max identique, choisir la première


#### niveau intermédiaire


2. Pour chaque coup, calculer le gain et la perte par rapport aux 16 possibilités de l'adversaire
    - gain = nombre de graibe pouvant être capturées
    - perte n = gain de l'adversaire une fois que le coup est joué (il y a 16 pertes)
3. Parmis les 16 pertes par coup, choisir la perte maximale
    - perte n = perte max n
    - Si plusieurs pertes reviennent au même résultat, calculer le gain potentiel de chacune des pertes identiques
        - gain pot = perte de l'adversaire (il y a 16 gains pot pour chaque perte identique)
    1. choisir le gain potentiel minimal pour une perte identique. 
    2. Il y a donc autant de gain pot min que de perte identiques, parmis ceux la, choisir le gain potentiel minimal le plus bas
        - perte max n = gain potentiel minimal minimal
    3. Revenir à l'étape 3. 
4. Calculer la différence de chaque coup
    - différence = gain - perte max
5. Choisir le coup oú la différence est la plus élevée (elle peut être positive ou négative) et le jouer. 
    - Si plusieurs cas donnent le même résultat, choisir le premier cas

#### niveau imbattable

2. Pour chaque coup, faire tourner les 16 possibilités de l'adversaire et calculer le gain et la perte du robot pour chaque coup.
    - gain x = nombre de graines que le robot capture (il y en aurait 16) le gain peut être égal à 0
    - perte = gain x de l'adversaire (il y a 16 pertes par coup)
3. Pour une perte d'un coup, calculer le gain potentiel d'une perte que le robot pourrait avoir en faisant tourner les 16 possibilité du robot après chaque perte.
    - gain pot x = gain du robot après chaque perte (il y a 16 gains potentiels par perte)
4. Calculer la perte potentielle après un gain potentiel en faisant tourner les 16 possibilités d'un gain potentiel.
    - perte pot x = gain pot x de l'adversaire pour chaque gain potentiel du robot
5. Pour chaque gain potentiel d'une perte, calculer les différences potentielles entre le gain pot et la perte pot
    - différence pot n = gain pot - perte pot n (il y a 16 différences potentielles par gain potentiel)
6. Choisir la différence potentielle la plus élevée (elle peut être négative) pour chaque gain potentiel.
    - Si plusieurs différences potentielles sont les mêmes, cela veut dire que plusieurs pertes potentielles sont les mêmes.
    Il faut alors calculer, pour chaque perte potentielle identique, le gain potentiel^2 en faisant tourner les 16 possibilités de chaque perte potentielle identique
        - gain pot^2= perte pot de l'adversaire (Il y en a 16 par perte pot) 
    Ensuite, choisir le gain pot^2 le plus élevé pour chaque perte pot 
        - perte pot x = gain pot^2 max x
    Choisir ensuite, parmis les pertes potentielles initialement identiques, la perte potentielle minimale.
    Remplacer ensuite la perte potentielle par la perte potentielle minimale
        - perte pot = perte pot min
    Retourner à l'étape 5.
    - gain pot x = différence pot max x
7. Il y a alors 16 gains potentiels par perte, choisir le gain potentiel le plus élevé pour chaque perte
    - perte x = gain pot max x 
8. Calculer à présent les différences réelles pour chaque gain initial
    - différence réelle n = gain - perte n (il y a 16 différences réelles par gain)
9. Pour chaque gain, choisir la différence réelle la plus élevée (peut être négative)
    - gain x = différence réelle max x
    
10. On a maintenant une différence réelle maximale par coup, choisir le gain le plus élevé parmis ces 16 coups et le jouer.
    
    
### Parcours

1. -[x] aspect logique 
    - but et principe du jeu
    - conditions du robot
2. -[ ] documentation
    - interface visuel
    - déplacement virtuel des pièces
    - adversaire virtuel
3. -[ ] programmation
    - mini-jeux (exemples de programmes)
    - algorythme et programme
    - interface visuel
4. mise en pratique
    - finalisation du projet

### Objectifs
Je viens de finir la première étape, 
qui d'après moi, serait la plus simple et la plus rapide. Je pense qu'il serait temps de fixer le premier rendez-vous pour en parler. En terme de temps, je trouve que je m'en donne assez et j'avance à une vitesse favorable.

## 24.02.25
Aujourd'hui, j'ai vu mon mentor. Ca m'a beaucoup aidé car je me suis rendu compte qu'il fallait que je prenne un autre point de vue sur le travail et le réaliser par petites étapes. Par exemple, programmer l'interface visuel d'abord ensuite programmer ce qui se passe si je clique sur une graine ensuite programmer le jeu pour 2 joueurs réels etc...

## 11.04.25
Ce sont les vacances de printemps : aujourd'hui je commence par programmer l'interface visuel. Mais avant ça, je me documente. Je me trouve à cheval entre la documentation et la programmation, dans le sens oú j'avance mon programme pas à pas, comme mon mentor l'avait dit dans l'ancien rendez-vous.
J'ai modifié alors mon parcours pour donner ceci:


1. -[ ] documentation et programmation
    1. interface visuel
    2. déplacement virtuel des pièces
    3. adversaire réel (sur le même écran)
    
3. -[x] aspect logique (Cela déja étant fait, je l'introduirai dans mon programme plus tard.)
    - but et principe du jeu
    - conditions du robot
4. -[ ] Finalisation du projet
    1. Traduction de l'aspect logique en programme python
    2. Ajout du programme dans le programme de base.

### Commencement du programme 
A l'aide du document Cours_Python.pdf mis à disposition sur teams par mon mentor, voici le début du programme :

Le bao game est un jeu, je rappelle qui est composé de 8 trous, avec 2 graines par trou. Je commence alors par insérer un trou à l'aide de python. 
Il faut d'abord mettre les fonctions nécessaires afin que le cercle apparaisse sur une fenêtre, comme spécifié dans le cours.
Pour ça, j'ai décidé d'utiliser la fonction create_oval se trouvant à la page 70 du cours:

     from tkinter import *

     fen = Tk()

     fen.geometry("600x600")

    can = Canvas(fen, width=100, height=100)

     can.grid()

    can.create_oval (1,1,9,9)

    fen.mainloop()  

Sinon, le programme est mis à disposition sur un autre document. Donc une fois qu'on a réussi à dessiner un cercle, je vais dessiner le plateau entier, qui je rappelle est composé de 32 trous, avec 8 trous par ligne. Je commence alors à créer un rectangle, qui sera les limites du plateau:

    from tkinter import *

    fen = Tk()

    fen.geometry("820x420")
    can = Canvas(fen, width=820, height=600)
    can.grid()
    can.create_rectangle (10,10,810,410)
    fen.mainloop()
(J'ai un peu modifié les valeurs de la fenêtre afin que les longueurs correspondent bien). Maintenant, je divise le plateau en 4 lignes et 8 colonnes. Pour cela, j'ai décidé d'utiliser le code des lignes: 

    can.create_line (10,100,810,100)

Voici la première ligne. Je me suis dit que ça irait peut être plus vite si je les dessinais toutes d'un coup, alors j'ai décidé d'uiliser une boucle while, qui dessinerait une ligne et une colonne tous les "100" de l'axe x et y:

    x = 110 
    y = 110
    while x < 820 : 
        can.create_line (x,10,x,410)
        can.create_line (10,y,810,y)
        x = x + 100
        y = y + 100

(Cela fonctionne même si l'axe des x est plus grand que celui des y car mon espace de Canvas a été restreint pour l'axe y.) Maintenant, il faudrait mettre des trous un pour chaque carré du coup. J'ai décidé de dessiner des cercle qui ne touchent pas les côtés du carré de "10" :

    can.create_oval (20,20,100,100)

Encore une fois, dessiner tous les cercles du plateau prendrait une eternité. Alors j'ai encore utilisé la boucle while pour les dessiner tous les "100" de largeur et de longueur en même temps : 

    cx = 20
    cy = 20
    z = 20
    while z < 420:
        while cx < 820 : 
         can.create_oval (cx,z,cx + 80,z + 80)
         cx = cx + 100
         cy = cy + 100
        z = z + 100
        cx = 20
        cy = 20
    
Maintenant, je vais rajouter une graine dans un trou et essayer de la faire bouger en cliquant dessus. Voici la graine, dessiné dans le premier trou :

    can.create_oval (40,40,60,60,activewidth = 5)

J'ai rajouté la fonction "activewidth = 5" afin que le cercle s'épaississe lorsque la souris passe dessus, cela permet au joueur de mieux visualiser le grain qu'il s'agit. En premier temps, j'ai fait en sorte que la graine soit séléctionnée lorsqu'on clique dessus. Pour ça, j'ai relié l'évènement "clic gauche" à la fonction "go" que j'ai défini en tant que "crée un oval de largeur 5" :

    can.create_oval (40,40,60,60, activewidth = 5,)
    def go(event) :
        can.create_oval (40,40,60,60,width = 5)

    fen.bind('<Button-1>', go)

Pour comprendre ce système de "bind", je me suis aidé du cours et de cette vidéo tutorielle qui explique assez simplement : https://www.youtube.com/watch?v=Jb5Df2ul41M

Maintenant, au lieu que la graine soit plus large, j'aimerais qu'elle se déplace. Pour ça j'ai utilisé la foncton qui permet de changer les cordonnées de la graine can.coords():

    def sélectionner(event) :
        n = can.find_closest(50,50)
        can.coords(n,140,40,160,60)
        #can.create_oval (40,40,60,60,width = 5)
    fen.bind('<Button-1>', sélectionner)

Maintenant, j'aimerais que la graine change de coordonnées à chaque fois que je clique. Pour ça, j'ai changé la définition de l'event et ai remplacé les nombres par des variables : 

    x = 50
    y = 50
    cx = 140
    def sélectionner(event) :
        global x,y,cx
        n = can.find_closest(x,y)
        can.coords(n,cx,40,cx + 20,60)
        x = x + 100
        cx = cx + 100
    fen.bind('<Button-1>', sélectionner) 

La, je ne comprenais pas pourquoi cela ne marchait pas, sans le terme global alors j'a demandé à ma maman qui est spécialisée dans ce domaine et elle m'a effectivement expliqué le principe de ce terme. Maintenant, il faut que la graine se déplace dans le sens des aguilles d'une montre au lieu de sortir du cadre :

    x = 50
    y = 50
    cx = 140
    cy = 40      

    def sélectionner(event) :
        global x,y,cx,cy,dx,dy
        if x == 750 and y != 150 :
            b = can.find_closest(750,50)
            can.coords(b,740,140,760,160)
            y = 150
            x = 750
            cx = 640
            cy = 140
        elif x == 50 and y == 150 :
            n = can.find_closest(x,y)
            can.coords(n,40,40,60,60)
            y = 50
            x = 50
            cx = 140
            cy = 40
        elif y == 150 :
            n = can.find_closest(x,y)
            can.coords(n,cx,cy,cx + 20,cy + 20)
            x = x - 100
            cx = cx - 100
        else :
            n = can.find_closest(x,y)
            can.coords(n,cx,cy,cx + 20,cy + 20)
            x = x + 100
            cx = cx + 100
    fen.bind('<Button-1>', sélectionner)

J'ai utilisé les if et elif où quand la graine est en haut à droite, elle descend(y + 100), quand la graine est en bas à droite, elle va à gauche (x-100), quand la graine est en bas à gauche, elle monte (y - 100) et ensuite qu'elle se dirige vers la droite lorsqu'elle se trouve en haut à gauche. Maintenant, ajoutons une deuxième graine !