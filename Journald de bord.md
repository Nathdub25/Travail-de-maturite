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

Le but de mon TM n'est pas de créer un adversaire imbattable, alors je vais vais sorte que mon robot ne prévoie qu'un tour ou 2 d'avance.

### Conditions (aspect logistique)
Une fois toutes les règles expliquées et programmées, le robot devra :

1. Faire tourner chacune des 16 possibilités
2. Choisir les possibilités qui permettent la capture et faire tourner ensuite les 16 possibilités de l'adversaire pour chacun des coups permettant la capture. 
    - Capture = nmbr de graines se situant dans le trou d'en face (revoir règles du jeu)
    - Si aucun coup pouvant être joué par le robot ne permet la capture, calculer pour tous les coups du robot --> gain = 0
3. Parmis les 16 possibilités de l'adversaire, choisir celle qui permettra de capturer le plus de graines du robot pour chaque coup calculé et choisi par le robot.
    - Si plusieurs coups reviennent au même résultat, choisir un coup aléatoirement parmis ceux-là
4. Comparer, pour chaque coup calculé et choisi initialement, le gain et la perte, c'est-à-dire le nombre de graine que le robot capture et le nombre de graine que le robot perd, au maximum.
    - gain = capture
    - perte = capture adversaire
    - Différence = gain - perte
5. Choisir le coup oú la différence est la plus élevée (elle peut être positive ou négative) et le jouer. 
    - Si plusieurs cas donnent le même résultat, choisir un coup aléatoirement parmis ces cas.

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
Je viens de finir la première étape, qui d'après moi, serait la plus simple et la plus rapide. Je pense qu'il serait temps de fixer le premier rendez-vous pour en parler. En terme de temps, je trouve que je m'en donne assez et j'avance à une vitesse favorable.