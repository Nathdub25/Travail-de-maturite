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

    def graineun(event) :
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
    fen.bind('<Button-1>', graine1)

J'ai utilisé les if et elif où quand la graine est en haut à droite, elle descend(y + 100), quand la graine est en bas à droite, elle va à gauche (x-100), quand la graine est en bas à gauche, elle monte (y - 100) et ensuite qu'elle se dirige vers la droite lorsqu'elle se trouve en haut à gauche. Maintenant, ajoutons une deuxième graine :

    can.create_oval (40,240,60,260, activewidth = 5)
    X = 50
    Y = 250
    CX = 140
    CY = 240
    def grainedeux(event) :
        global X,Y,CX,CY
        if X == 750 and Y == 350 :
            b = can.find_closest(X,Y)
            can.coords(b,740,240,760,260)
            Y = 250
            X = 750
            CX = 640
            CY = 240
        elif Y == 350 :
            n = can.find_closest(X,Y)
            can.coords(n,CX,CY,CX + 20,CY + 20)
            X = X + 100
            CX = CX + 100
        elif X == 50 and Y == 250 :
            n = can.find_closest(X,Y)
            can.coords(n,40,340,60,360)
            Y = 350
            CX = 140
            CY = 340
            X = 50
        else :
            n = can.find_closest(X,Y)
            can.coords(n,CX,CY,CX + 20,CY + 20)
            X = X - 100
            CX = CX - 100
    fen.bind('<Button-3>', grainedeux)

Voila, donc à présent lorsque je fais un clic gauche, c'est la graine 1 qui avance tandis que si je fais un clic droit, c'est la graine 2. J'ai juste repris le même code, en changeant les cordonnés du y et mis d'autres variables (en majuscule)

## 24.04.25

Aujourd'hui, j'ai vu mon mentor et il m'a permis de comprendre comment continuer ce que j'avais deja codé. Par exemple, la technique des lignes qui est bien utiles pour définir les trous remplis de graines.

C'est ainsi que je me suis décidé à faire un tableau pour l'instant de la première ligne. Alors je crée 1 graine par trou, dans les 8 trous de la première ligne :

    for i in range(140, 840, + 100):
        can.create_oval(i, 40, i + 20, 60)

Maintenant, voici mon tableau correspondant à cette ligne :

    ligne1 = [1,1,1,1,1,1,1,1]

Pour l'instant, j'aimerais éviter de placer plus de 1 graine par trou, alors je me suis dit qu'il vaudrait mieux remplacer la graine par le nombre de graines qu'il y a dans le trou, donc "1":

    for i in range(40, 840, + 100):
        can.create_text(i, 40, text = "1")
    
Voila, à présent il faudrait que quand je clique sur un "1", il ajoute + 1 au trou suivant. Pour ça, j'ai utilisé un tableau pour la première ligne, où chaque trou correspond à une case et le nombre écrit correspond à une graine. Lorsque je clique sur une case, la valeur du tableau correspondante fait + 1 :

    L1 = [1,1,1,1,1,1,1,1]
    tableau = []


    #fen.bind('<Button-1>', graineun)
    for i in range(len(L1)):
        un = can.create_text(i*100 + 40, 40, text = str(L1[i]))
        tableau.append(un)

    def adgr(event):
        global tableau
        clic_x = event.x
        clic_y = event.y 
        num_case = clic_x // 100
        L1[num_case] = L1[num_case] + 1
        can.itemconfig(tableau[num_case],text = str(L1  [num_case]))
    
    fen.bind('<Button-1>', adgr)

Ce que je fais est créer un tableau L1, qui contient les valeurs de base : "1". Ensuite je crée un tableau vide correspondant à la première ligne du plateau : tableau. Ensuite, grâce à la fonction "len", j'insère le texte qui est stocké dans L1, donc "1" pour chaque trou, déterminés par la longueur du tableau L1, donc 8. Cet "ajout" (can.create_texte) utilise la longueur du tableau L1 comme cordonnées, multipliées par 100 et affiche la valeur du même tableau.

Après je définis l'évènement "adgr" que lie avec le bouton gauche. L'évènement stock les cordonnées de l'objet le plus proche (grâce à event.x/y) du clic de souris en tant que "clic_x ou clic_y". Je définis ensuite la variable "num_case" grâce à la variable "clic_x" que je divise par 100, étant donné que ce sont des cordonnées. J'ajoute + 1 à la variable num_case, car c'est ce que je voulais à la base puis, grâce à la fonction "itemconfig", j'insère la variable num_case alors augmenté de 1 directement à l'intérieur de mon tableau vide "tableau" et je remplace le texte de base qui était affiché sur le trou correspondant ("1") par la valeur augmenté.

Maintenant, j'aimerais faire en sorte que ce soit la case d'après qui fass + 1 et que la case de départ descende à 0. Pour ça, j'ai just ajouté + 1 après la division par 100 des cordonnées, pour qu'on modifie bien la case suivante :

    num_case = clic_x // 100 + 1

J'ai aussi ajouté cette ligne, qui permet de remmetre à 0 la case de "départ" :

    can.itemconfig(tableau[num_case - 1], text = "0")

Ce que j'aimerais à présent, c'est ajouter la valeur de la case au lieu de + 1, ce qui correspondrait plus aux règles du jeu. Pour ça, j'ai ajouté 2 variables, une qui correspond à la case de départ (num_case_deb) et une qui correspond à celle d'après (num_case_fin). J'ai ajouté 2 lignes en plus, celle qui réduit la valeur de la case de début à 0 et une qui remplace la valeur visuellement :

    num_case_deb = clic_x // 100 
    num_case_fin = clic_x // 100 + 1
    L1[num_case_fin] = L1[num_case_deb] + L1[num_case_fin]
    L1[num_case_deb] = L1[num_case_deb] - L1[num_case_deb]
    can.itemconfig(tableau[num_case_fin],text = str(L1[num_case_fin]))
    can.itemconfig(tableau[num_case_deb],text = str(L1[num_case_deb]))

Maintenant, il faudrait ajouter la deuxième ligne du tableau, pour prendre en compte la ligne du bas. Pour ça, j'ai utilisé une matrice, qui met des "1" dans tous les trous de la première et la deuxième ligne :

    
    j1 = [[1]*8 for i in range(0,2)]
    tableau = [] #ici j1 pour "joueur 1"
Donc il y aurait 8* le chiffre "1" pour les 2 premières lignes. Ensuite, pour afficher la matrice aux trous correspondants, j'ai décidé, avec l'aide de mon mentor, d'utilisé 2 boucles "for" l'une à l'intérieur de l'autre :

    for j in range (2):
        for i in range (len(j1[0])):
            un = can.create_text(i*100 + 40,j*100 + 40, text = str(j1[j][i]))
            tableau.append(un)

La première boucle dit "tous les j de 0 à 2", qui correspond aux 2 premières lignes du premier joueur. Ensuite, pour chaque ligne de la boucle "j", une autre boucle for est utilisée, qui dirait "pour tous les i de la longueur de la première ligne (j1[0], ici = 8)", et un texte est écrit, appelé "un", qui se répèterait tous les "i*100 + 40" pour les x (donc les colonnes) et tous les j * 100 + 40" pour les y (donc les lignes), où le texte est la valeur correpondante à j1[i][j], donc 1 comme on l'a défini dans la matrice plus tôt.

Donc si je veux aussi avoir le joueur n°2, je n'ai qu'à remplacer la taille de la matrice et jusqu'à quelle valeur la variable "j" irait par 4 au lieu de 2.

Maintenant, il faudrait lier la matrice avec le plateau de jeu. Pour ça, je crée une matrice vide :

    tableau = [[None]*8 for i in range(0,4)]

Ensuite, j'écris un texte pour chaque trou (ici : "1") que je relie ensuite à la matrice vide, pour que chaque texte corresponde à une case de la matrice :

    for j in range (4):
        for i in range (len(jeu[0])):
            valcer = can.create_text(i*100 + 40,j*100 + 40, text = str(jeu[j][i])) #jeu est le nouveau nom pour "j1"
            print (j, i)
            tableau[j][i] = valcer
            print (tableau[j][i])

--> Les cordonnées du tableau [j][i] correspondent à valcer, qui est le texte créé des cordonnées correspondantes du tableau "jeu", une matrice 4x8 remplie que de "1".

Ensuite, j'aimerais faire en sorte donc qu'un clic permette de déplacer toutes les graines d'un trou dans le trou suivant. Pour ça j'ai défini un event :

    def adgr(event):
        global tableau
        clic_x = event.x
        clic_y = event.y 
    
        co = clic_x // 100 
        li = clic_y // 100 
        
        jeu[li][co] = 0
        jeu[li][co+1] = jeu[li][co+1] + 1
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li][co + 1],text = str(jeu[li][co + 1]))

Donc co correspond aux cordonnées x du clic divisées par 100 : c'est-à-dire le numéro de la colonne, et li aux cordonnées y du clic divisées par 100 : donc le numéro de la ligne. Ainsi donc la commande jeu[li][co]=0 remet la valeur de la case correspondante de la matrice à 0! La case d'après (jeu[li][co+1]) vaut plus 1, étant donné qu'on a additionné la valeur de la case d'avant. Visuellement, il faudrait encore changer le texte par la valeur de la case, d'ou la commande itemconfig.

Mais au lieu de rajouter + 1 à chaque fois (même si cela marche pour le premier clic) il faudrait rajouter la valeur de la case correspondante, qui n'est pas toujours égale à 1, du coup :

    def adgr(event):
        global tableau
        clic_x = event.x
        clic_y = event.y 
    
        co = clic_x // 100 
        li = clic_y // 100 
        jeu[li][co+1] = jeu[li][co+1] + jeu[li][co]    
        jeu[li][co] = jeu[li][co]-jeu[li][co]
    
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li][co + 1],text = str(jeu[li][co + 1]))

Donc j'ai remplacé + 1 par la valeur de la case du clic et j'ai mis cette commande avant l'autre, avant qu'on ne baisse la valeur à 0.
Voila, maintenant il faudrait que cela fonctionne aux bords, que la valeur des graines descendent ou montent.

    def adgr(event):
    global tableau
    clic_x = event.x
    clic_y = event.y 
    
    co = clic_x // 100 
    li = clic_y // 100 
    if clic_y > 240 and clic_y < 340 and clic_x > 140:
        jeu[li][co-1] = jeu[li][co-1] + jeu[li][co]    
        jeu[li][co] = jeu[li][co]-jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li][co - 1],text = str(jeu[li][co - 1]))
    if clic_x > 0 and clic_x < 140 and clic_y > 240 and clic_y < 340:
        jeu[li+1][co] = jeu[li+1][co] + jeu[li][co]
        jeu[li][co] = jeu[li][co] - jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li+1][co],text = str(jeu[li+1][co]))
    if clic_y > 340 and clic_y < 440 and clic_x < 740:
        jeu[li][co+1] = jeu[li][co+1] + jeu[li][co]    
        jeu[li][co] = jeu[li][co]-jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li][co + 1],text = str(jeu[li][co + 1]))
    if clic_x > 740 and clic_x < 840 and clic_y > 340 and clic_y < 440:
        jeu[li-1][co] = jeu[li-1][co] + jeu[li][co]
        jeu[li][co] = jeu[li][co] - jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li-1][co],text = str(jeu[li-1][co]))
    if clic_y > 140 and clic_y < 240 and clic_x < 740:
        jeu[li][co+1] = jeu[li][co+1] + jeu[li][co]    
        jeu[li][co] = jeu[li][co]-jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li][co + 1],text = str(jeu[li][co + 1]))
    if clic_x > 740 and clic_x < 840 and clic_y > 140 and clic_y < 240:
        jeu[li-1][co] = jeu[li-1][co] + jeu[li][co]
        jeu[li][co] = jeu[li][co] - jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li-1][co],text = str(jeu[li-1][co]))
    if clic_y > 0 and clic_y < 140 and clic_x > 140:
        jeu[li][co-1] = jeu[li][co-1] + jeu[li][co]    
        jeu[li][co] = jeu[li][co]-jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li][co - 1],text = str(jeu[li][co - 1]))
    if clic_x > 0 and clic_x < 140 and clic_y > 0 and clic_y < 140:
        jeu[li+1][co] = jeu[li+1][co] + jeu[li][co]
        jeu[li][co] = jeu[li][co] - jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li+1][co],text = str(jeu[li+1][co]))

J'ai mis une condition pour chaque coin (8, 4 par joueur) ou pouvaient se trouver les cordonnées, en augmentant les x (co+1) ou les y (li+1), ou en les descendant (co-1/li-1).

Maintenant, j'aimerais faire en sorte que les graines d'un trou soient distribuées 1 par 1 dans les trous suivants.

    if clic_y > 240 and clic_y < 340 and clic_x > 140:
        for k in range(1, jeu[li][co]+1):
            jeu[li][co-k] = 1  + jeu[li][co-k] 
            jeu[li][co] = jeu[li][co]-jeu[li][co]
            can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
            can.itemconfig(tableau[li][co - k],text = str(jeu[li][co - k]))

J'ai utilisé une boucle for, donc pour tous les k allant de 1 à la valeur du trou correspondant du clic + 1, je rajoute 1 à la valeur des k trous suivants. Mais pour l'instant, cela marche que si les graines rentrent avant le bord du tableau. Il faut donc que les graines se distribuent aussi sur les lignes suivantes, dans le sens du jeu : 

        if clic_y > 240 and clic_y < 340:
    
        if jeu[li][co] <= co:
            val = jeu[li][co]
            for k in range(1, val+1):
                jeu[li][co-k] = 1  + jeu[li][co-k] 
                can.itemconfig(tableau[li][co - k],text = str(jeu[li][co - k]))
                jeu[li][co] = 0
                can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
            
        if jeu[li][co] > co:
            if co == 0:
                val = jeu[li][co]
                for h in range(0, val):
                    jeu[li+1][h] = jeu[li+1][h] + 1
                    can.itemconfig(tableau[li+1][h], text=str(jeu[li+1][h]))
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
            else:
                val = jeu[li][co]
                for g in range(1, co+1):
                    jeu[li][co-g] = jeu[li][co-g] + 1
                    can.itemconfig(tableau[li][co - g],text = str(jeu[li][co - g]))
                for h in range(0, val-co):
                        
                    jeu[li+1][h] = jeu[li+1][h] + 1
                    can.itemconfig(tableau[li+1][h], text = str(jeu[li+1][h]))
                        
                jeu[li][co] = 0
                can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                    

J'ai mis 2 conditions : si le contenu du trou est plus petit ou égal que le nombre de trous qui restent avant de descendre de ligne (donc <= le numéro de la case-->co) et si le contenu du trou est plus grand que co, auquel cas les graines devront aussi être distribuées sur la ligne du bas. Pour la première condition, j'ai repris le même code qu'avant, rien ne change.

Pour la deuxième condition donc si jeu[li][co] > co, ce que je fais c'est que je distribue les graines du trou sur la ligne d'abord (donc il y a autant de trous que les cordonnées de colonne : co) en utilisant la boucle for g in range et la fonction co-g. Et ensuite je distribue le reste sur la ligne du bas donc pour trouver le reste je fais le contenu du trou (jeu[li][co]) - le nombre de trous sur la ligne de base (co). La j'ai utilisé la boucle for h in range qui rajoute +h à co de jeu[li+1 car c'est la ligne du bas][co qui est égal à 0 car on part de la gauche, donc h]. J'ai aussi rajouté la condition de co==0, car si on soustrait le contenu de jeu[li][0] à 0 ben on obtient un nombre négatif donc ça va modifier le mauvais trou de la ligne en plus, et ce n'est pas ce que je veux. Donc pour cette condition co==0 j'ai utilisé le même code mais sans la ligne de base, donc toutes les graines de ce trou vont directement dans la ligne du bas.

Maintenant que ça c'est fait, il faut aussi le faire pour toutes les lignes donc encore 3 fois (2 pour monter : joueur 1 et joueur 2, et 2 pour descendre : joueur 1 et joueur 2 aussi).

Je ne vais pas écrire le code, mais il est disponible sur GitHub et il marche!

Maintenant, ce qu'il faudrait faire c'est répéter le processus tant que le trou de la dernière graine posée ne soit pas vide.

Voici mon code pour un joueur :

    while True :
        
        dern_li = li
        dern_co = co
        if clic_y > 240 and clic_y < 340: #3ème rangée
            if jeu[li][co] <= co: #si nmbr de graine plus petit que nmbr de trou suivants
                val = jeu[li][co]
                for k in range(1, val+1): # + 1 trous suivants
                
                    jeu[li][co-k] = 1  + jeu[li][co-k] 
                    can.itemconfig(tableau[li][co - k],text = str(jeu[li][co - k]))
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                dern_co = co-val
            
            else: #si besoin de distribuer dans la rangée du dessous
                if co == 0: #juste la ligne du dessous
                    val = jeu[li][co]
                    for h in range(0, val):
                        jeu[li+1][h] = jeu[li+1][h] + 1
                        can.itemconfig(tableau[li+1][h], text=str(jeu[li+1][h]))
                        jeu[li][co] = 0
                        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                    dern_li = li + 1
                    print (co,val)
                    dern_co = co + val -1
                    print (dern_co)
                    
                
                elif co > 0:
                    #les trous suivants + la ligne du dssous
                    val = jeu[li][co]
                    for g in range(1, co+1):
                        jeu[li][co-g] = jeu[li][co-g] + 1
                        can.itemconfig(tableau[li][co - g],text = str(jeu[li][co - g]))
                    for h in range(0, val-co):
                        
                        jeu[li+1][h] = jeu[li+1][h] + 1
                        can.itemconfig(tableau[li+1][h], text = str(jeu[li+1][h]))
                        
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                    dern_li = li + 1
                    dern_co = val-co-1
                
                    
        
                    
        if clic_y > 340 and clic_y < 440: #4ème rangée
            if jeu[li][co] <= 7-co: #si nmbr de graine plus petit que nmbr de trou --> distribuer que sur rangée
                val = jeu[li][co]
                for k in range(1, val+1):
                    jeu[li][co+k] = 1  + jeu[li][co+k] 
                    can.itemconfig(tableau[li][co + k],text = str(jeu[li][co + k]))
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                dern_co = co + val
                print (co, val)
            else:
                val = jeu[li][co]
                if co == 7: #distribuer ligne du dessus
                    for h in range(0, val):
                        jeu[li-1][7-h] = jeu[li-1][7-h] + 1
                        can.itemconfig(tableau[li-1][7-h], text=str(jeu[li-1][7-h]))
                        jeu[li][co] = 0
                        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                    dern_li = li - 1
                    dern_co = 7-val+1
                    
                else: #distribuer ligne du dessus + trou qui restent
                    val = jeu[li][co]
                    for g in range(1, 7-co+1):
                        jeu[li][co+g] = jeu[li][co+g] + 1
                        can.itemconfig(tableau[li][co + g],text = str(jeu[li][co + g]))
                    for h in range(0, val-(7-co)):
                        jeu[li-1][7-h] = jeu[li-1][7-h] + 1
                        can.itemconfig(tableau[li-1][7-h], text = str(jeu[li-1][7-h]))
                        
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                    dern_li = li - 1
                    dern_co = 7- (val - (7-co) - 1)
        if jeu[dern_li][dern_co] == 1:
            break
        elif jeu[dern_li][dern_co] > 1:
            li = dern_li
            co = dern_co
            print(jeu)
            print (li, co)
        if dern_li == 3:
            clic_y = 350
        if dern_li == 2:
            clic_y = 250

Ce que j'ai fait, c'est que j'ai rajouté le "dern_co et dern_li" Ces variables correspondent aux cordonnées du dernier trou dans lequel la graine rattérit. La boucle while true fait que, tant que le dernier trou donc jeu[dern_li][dern_co] ne contient pas une seule graine, la dernière (voir règles), le processus se répète en boucle avec dern_co qui devient le nouveau co et dern_li qui devient le nouveau li, tout en augmentant ou diminuant de 100 clic_y suivant si li = 2 ou li = 3. 

Maintenant il faudrait rajouter la règle de la "prise" qui dit que si le trou en face de celui que la graine rattérit (que sur rangée du dessus), les graines de l'adversaire disparaissent. Pour ça, j'ai décidé de d'abord programmer le joueur 2. 

Maintenant que c'est fait, j'ai donc programmer cette règle de prise :

         if jeu[dern_li][dern_co] == 1: #si dernière graine attérit dans une case vide
            if dern_li == 2: #joueur 1 prend les graines de l'adversaire
                jeu[dern_li-1][dern_co] = 0
                can.itemconfig(tableau[dern_li-1][dern_co],text = str(jeu[dern_li-1][dern_co]))
                
            elif dern_li == 1: #joueur 2
                jeu[dern_li+1][dern_co] = 0
                can.itemconfig(tableau[dern_li+1][dern_co],text = str(jeu[dern_li+1][dern_co]))

Le code consiste à changer la valeur de la case en face de celle dans laquelle la dernière graine rattérit par 0 (le joueur prend les graines). Mais cette règle ne marche que pour la rangée du dessus, donc j'ai écrit 2 cas de figures : quand dern_li = 2 (donc la rangée du dessus du premier joueur)
et quand dern_li = 1(rangée du dessus du deuxième joueur).
Donc si la valeur de la dernière case = 1 (derière graine), suivant les cas de figures, la case du dessus (dern_li -1) ou la case du dessous (dern_li +1) vaut 0.

Maintenant, j'aimerais afficher les graines prises directement sur l'écran. Pour ça, j'ai ajouté ces lignes au code:

    can.create_text (150, 450, text = "player 1 : ")
    can.create_text (550, 450, text = "player 2 : ")
    graines_j1 = can.create_text(150,470, text = "0")
    graines_j2 = can.create_text(550,470, text = "0")

Ensuite, j'ai défini le nombre de graines capturées des deux joueurs à 0 :

    nbr_graine_mangees_j1 = 0
    nbr_graine_mangees_j2 = 0
    !C'est important de le faire en dehors de l'event, pour éviter de définir la valeur à 0 à chaque fois!

Et pour finir, j'ai ajouté ces lignes dans le code pour les règles de "prise": 

        total = nbr_graine_mangees_j1 + jeu[dern_li-1][dern_co] #la cagnotte totale devient l'addition des graines capturées et des graines venant d'être capturées
        can.itemconfig(graines_j1, text = str(total))#afficher le total des graines capturés par le joueur 1
        nbr_graine_mangees_j1 = total

Donc la "cagnotte" est l'addition des graines présentes déjà dans dans la cagnotte de départ (au début = 0) et les graines capturées à ce moment la. A chaque tour donc on remplace le nombre de graines mangées du joueur 1 par la cagnotte totale. (itemconfig). La cagnotte totale devient alors le nouveau nombre de graine mangées, qui viendra s'addtionner au prochain tour avec les graines venant d'être capturées.

Voici le code pour le joueur 2 :

    elif dern_li == 1: #joueur 2
        total = nbr_graine_mangees_j2 + jeu[dern_li+1][dern_co] #la cagnotte totale devient l'addition des graines capturées et des graines venant d'être capturées
        can.itemconfig(graines_j2, text = str(total))#afficher le total des graines capturés par le joueur 2
        nbr_graine_mangees_j2 = total 
                
        jeu[dern_li+1][dern_co] = 0
        can.itemconfig(tableau[dern_li+1][dern_co],text = str(jeu[dern_li+1][dern_co]))

Maintenant que le jeu est fonctionnel, il y a cependant quelques petits problèmes à modifier, notamment le fait que python bug lorsqu'on appuie sur un trou vide. Un autre problème, c'est qu'il n'y a pas de fin. J'aimerais alors faire apparaitre une fenêtre à la fin de la partie et à chaque fois qu'on clique sur une case vide. Pour ça, je me suis renseigné sur ce site : https://blog.alphorm.com/utiliser-tkinter-messagebox-python#tkinter-askokcancel-confirmation-okannuler qui explique le principe du messagebox.

j'ai donc mis ce code :

          if jeu[li][co] == 0:
            messagebox.askokcancel("Case vide", "Vous avez cliqué sur une case vide")
            return

Et celui-la : 

    if total == 32:
                    messagebox.askokcancel("Fin de la partie", "Le joueur 1 remporte la partie!!")
                    return

Voila, maintenant j'ai remplacé les nombres par des points (..), pour transformer les points en valeur, j'ai juste pris la fonction len(). Le code marche avec ses points, et maintenant, une chose que j'aimerais régler c'est à qui de jouer. Le joueur 1 ne devrait pas pouvoir jouer 2 fois de suite. Avant ça, il faut faire en sorte que ce soit le premier joueur qui commence, et que la ligne du haut (comme dans les règles). J'ai donc ajouté ce code au début:
(Avec prm_tour = 1 au départ, en dehors de la boucle)

      if prm_tour == 1:
        if li == 0 or li == 1:
            messagebox.askokcancel("Mauvais joueur", "Ce n'est pas à vous de commencer.")
            return
        if li == 3:
            messagebox.askokcancel("coup illégal", "Vous ne pouvez pas commencer à jouer sur cette rangée, veuillez choisir un emplacement sur la 3ème rangée.")
            return
        if li == 3:
            prm_tour == 2

Donc tant qu'on ne clique pas sur li = 3, prm_tour vaut 1, donc les messages s'afficheront en boucle tant qu'on clique pas sur la bonne rangée.
