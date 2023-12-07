# Louis-Philippe Ostiguy
# Noah Taillon
# 10 décembre 2023
#
# Description du programme

import random
import math


# Permet de faire un nouvelle partie
def nouvelle_partie():
    init()


# Procédure qui permet d'afficher et de jouer au jeu de Solitaire Addiction
def init():
    # Inicier les variables globales
    global cartes_br
    global noms_cartes
    global noms_cartes_br
    global brasse_restant

    # Nombre de brassage de cartes restant
    brasse_restant = 3

    # Tableau qui contiendra les cardes ordonnées
    cartes = []

    # Tableau  ordonnée de toutes les cartes
    for i in range(52):
        cartes.append(i)

    # Cartes brassées
    cartes_br = brasser(cartes)

    # Tableau contenant tous les noms des cartes, en ordres croissant et en
    # couleur
    noms_cartes = paquet_cartes()

    # Paquet brassé avec le noms des cartes
    noms_cartes_br = []

    # Boucle qui permet de trouver l'élément associé aux noms des cartes
    # Donc, l'as de diamonds (AD) est à l'indice 0 de noms_cartes. L'élément
    # 0 est retrouvé dans cartes_br, et son indice est retourné.
    for i in cartes_br:
        for k in range(len(noms_cartes)):
            if k == i:

                # Crée un nouveau tableau mélangé, avec le nom des cartes
                noms_cartes_br.append(noms_cartes[k])
    
    # Met à jour le contenu de la page HTML
    mise_a_jour_affichage()


# Procédure qui met à jour le contenu HTML de la page web.
# La procédure prend en paramètres 3 tableau, un tableau de cartes
# brassées (sous forme de chiffre, 0 à 52), un tableau contenant le
# numéro et l'enseigne des cartes, en ordre, et un tableau contenant
# le noms_des cartes brassées.
def mise_a_jour_affichage():

    # Paquet brassé avec le noms des cartes
    noms_cartes_br = []

    # Boucle qui permet de trouver l'élément associé aux noms des cartes
    # Donc, l'as de diamonds (AD) est à l'indice 0 de noms_cartes. L'élément
    # 0 est retrouvé dans cartes_br, et son indice est retourné.
    for i in cartes_br:
        for k in range(len(noms_cartes)):
            if k == i:

                # Crée un nouveau tableau mélangé, avec le nom des cartes
                noms_cartes_br.append(noms_cartes[k])
    
    
    # Tableau qui contiendra les cardes ordonnées

    # Création des éléments HTML. Ces lignes n'ont déjà plus les as
    # Moyen de faire ça plus efficacement?
    ligne1 = lignes(noms_cartes_br[:13], 0)
    ligne2 = lignes(noms_cartes_br[13:26], 13)
    ligne3 = lignes(noms_cartes_br[26:39], 26)
    ligne4 = lignes(noms_cartes_br[39:], 39)

    # Changer le contenu HTML de l'élément racine
    racine = document.querySelector("#cb-body")
    racine.innerHTML = (
        """
      <style>
        #jeu table { float:none; }
        #jeu table td { border:0; padding:1px 2px; height:auto; width:auto; }
        #jeu table td img { height:140px; }
      </style>
      <div id="jeu">
        <table>
          <tr>
            """
        + ligne1
        + """
          </tr>
          <tr>
            """
        + ligne2
        + """
          </tr>
          <tr>
            """
        + ligne3
        + """
          </tr>
          <tr>
            """
        + ligne4
        + """
          </tr>
        </table>
      </div>
          <div id="controles">
    <div id="brasser">
    </div>
    <button id="new-games" onclick="nouvelle_partie()">Nouvelle partie</button>
  </div>
      """
    )
    brasseur = document.querySelector("#brasser")

    # Si le joueur n'à plus de brassage de cartes restant
    if brasse_restant == 0:
        brasseur.innerHTML = """Vous ne pouvez plus brasser les cartes"""

    # Si le joueur à encore des brassages de cartes restant
    else:
        brasseur.innerHTML = (
            """
        Vous pouvez encore <button id="brasser_cartes" onclick="brasser_cartes()">
        brasser les cartes</button>
        """
            + str(brasse_restant)
            + " fois"
        )

    # Changer la couleur de fond de la case 0

    # matrice retourne une matrice où les sous-tableaux sont composés de
    # l'indice 0 qui est l'indice de la carte à mettre en vert, et l'indice
    # 1 qui est la position où cette carte peut être déplacée.
    matrice = voisins_as(noms_cartes_br)

    # TODO: en plus de les afficher en vert, il faut ajouter la fonction clic()
    # aux cartes pouvant être déplacées
    for i in matrice:
        
        # L'indice 0 des sous-tableau de tab contient la carte qui peut
        # être déplacée, qu'il faut mettre en vert
        cas = document.querySelector("#case" + str(i[0]))
        cas.setAttribute("style", "background-color: lime")

        # Ligne de la matrice contenant l'indice de la case qui peut être 
        # bougée et l'indice de l'endroit où elle peut être déplacée
        cases = i 
        
        cas.setAttribute(
            "onclick",
            "bouger("
            + str(cases[0])
            + ","
            + str(cases[1])
            + ")",
        )


# Fonction pour bouger une carte. Destination = l'indice où la carte
# peut aller.

def bouger(origine, destination):
    temp = cartes_br[origine]
    cartes_br[origine] = cartes_br[destination]
    cartes_br[destination] = temp

    mise_a_jour_affichage()


# La fonction 'paquet_cartes' ne prend pas de paramètre. Elle retourne une
# liste contenant toutes les cartes d'un jeu de cartes classique en ordre
# croissant en couleur, commençant par le trèfle (C), le carreaux (D), le coeur
# (H) puis le pique (S). Ce paquet ne contient pas de Jokers. Pour ce faire,
# la fonction cycle au travers des quatres couleurs, et leur ajoute les
# 'nombres'. De plus, cette fonction ajoute les figures et les as.
def paquet_cartes():
    noms_cartes = []
    noms_couleurs = ["C", "D", "H", "S"]

    # Essaie de faire la liste des noms de cartes automatiquement
    # On a 1 = ace, 11 = valet,
    for i in range(1, 14):
        # Cycler au travers des 4 couleurs pour ajouter toutes les possibilités
        for couleur in noms_couleurs:
            # Si c'est un as, ajouter A
            if i == 1:
                noms_cartes.append("A" + couleur)

            # Si c'est un valet, ajouter J
            elif i == 11:
                noms_cartes.append("J" + couleur)

            # Si c'est une dame, ajouter Q
            elif i == 12:
                noms_cartes.append("Q" + couleur)

            # Si c'est un roi, ajouter K
            elif i == 13:
                noms_cartes.append("K" + couleur)

            # Si c'est une chiffre normal
            else:
                noms_cartes.append(str(i) + couleur)
    return noms_cartes


# La fonction 'brasser' prend en paramètre un tableau (tab) ne contenant que
# des éléments allant de 0 à 51 en ordre croissant. Ce tableau sera
# mélangé selon le principe suivant : échangeons le dernier élément n du
# tableau et échangeons le avec un élément aléatoire le précédant. Puis,
# même chose avec n-1, jusqu'à ce que tous les éléments aient été échangés.
# La fonction retourne ce tableau mélangé
def brasser(tableau):

    for i in range(len(tableau)):
        # Variable permettant de cycler au travers des éléments du tableau, en
        # partant par la fin.
        indice_dernier_element = len(tableau) - 1 - i

        # Choix aléatoire précédant le dernier élément
        aleatoire = math.floor(random.random() * len(tableau) - 1 - i)

        temp = tableau[indice_dernier_element]
        tableau[indice_dernier_element] = tableau[aleatoire]
        tableau[aleatoire] = temp
    return tableau


# La fonction 'ligne' prend en paramètre un tableau de chaînes de caractères
# non vide (tab), un entier correspondand à l'indice du premier élément de la
# ligne active (case). Elle retourne le code html permettant d'afficher une
# ligne d'un tableau HTML de chaque carte. Elle assigne une image à chaque nom
# présent dans le tableau (tab). De plus, elle retire les as, les transformant
# en cases vides.
def lignes(tab, case):
    # print(tab)
    # print(case)
    ligne = ""

    for i in tab:
        # Cas où la carte est un as
        if "A" in i:
            ligne += (
                """<td id=case""" + str(case) + """><img src="cards/absent.svg"></td>"""
            )
        else:
            ligne += (
                """<td id=case"""
                + str(case)
                + """><img src="cards/"""
                + i
                + """.svg"></td>"""
            )
        case += 1  # Ajustement de la case, pour la prochaine
    # print(ligne)
    return ligne


# Procédure qui brasse les cartes en tenant compte du nombre de
# brassé restant au joueur.
# La procédure prend en paramètres 3 tableau, un tableau de cartes
# brassées (sous forme de chiffre, 0 à 52), un tableau contenant le
# numéro et l'enseigne des cartes, en ordre, et un tableau contenant
# le noms_des cartes brassées.
def brasser_cartes():
    global brasse_restant

    # Décrémente le nombre de brassé restant au joueur
    brasse_restant -= 1

    en_ordre(cartes_br[:13])
    en_ordre(cartes_br[13:26])
    en_ordre(cartes_br[26:39])
    en_ordre(cartes_br[39:])
    
    # Brasse les cartes
    brasser(cartes_br)

    
    
    # Met à jour le contenu de la page HTML
    mise_a_jour_affichage()


# Retourne un tableau contenant en indice 0 la carte qui peut être déplacée
# et à l'indice 1 la position où elle peut être déplacée.
def voisins_as(noms_cartes_brasse):
    indexe = 0

    # tableau contenant les indices des voisins des as
    indexes_carte_suivante = []

    # Passe à travers toute les cartes du paquets
    for carte in cartes_br:
        indexe = trouver_indice(cartes_br, carte)
        if carte // 4 == 0:  # Si c'est un AS
            valeur_carte = noms_cartes_brasse[indexe]
            indexe_noms_cartes = noms_cartes.index(valeur_carte)

            # Si la carte est un roi, continue car rien ne peut suivre cette carte
            if cartes_br[indexe - 1] + 4 > 51:
                continue

            # Si il y a plusieurs AS à la suite de l'autre
            if cartes_br[indexe - 1] // 4 == 0:
                continue

            # Pour que la première case donne la posibilité de mettre toute
            # les cartes ayant la valeur 2
            if indexe == 0 or indexe == 13 or indexe == 26 or indexe == 39:
                for deux in range(4, 8):
                    indexes_carte_suivante.append(
                        [trouver_indice(cartes_br, deux), indexe]
                    )

            else:
                # Valeur de la carte précédant la case vide (AS)
                valeur_carte = noms_cartes_brasse[indexe - 1]

                # Index de la carte devant l'as dans noms_cartes
                indexe_noms_cartes = trouver_indice(noms_cartes, valeur_carte)

                # Index de la carte suivante après la carte qui se trouve avant
                # la carte vide (AS)
                index_suivant = trouver_indice(
                    noms_cartes_brasse, noms_cartes[indexe_noms_cartes + 4]
                )

                # Ajouter la carte suivante au tableau qui contient la
                # liste de carte à afficher en vert
                indexes_carte_suivante.append([index_suivant, indexe])

    return indexes_carte_suivante


# La fonction trouver_indice prend en paramètre un tableau (tab) et un élément
# à chercher dans ce tableau (a_trouver). Cet elément doit nécessairement être
# présent dans le tableau. Cette fonction retourne l'indice de l'élément à
# chercher.
def trouver_indice(tab, a_trouver):
    if len(tab) == 0:
        return False
    else:
        for i in range(len(tab)):
            if tab[i] == a_trouver:
                return i
        return False


# La fonction en_ordre sert à détecter les eléments (nombre entiers)
# qui sont croissants et ayant une incrémentation de +1 entre
# élément du tableau. Les éléments qui sont en ordre sont remplacé par le
# boléen 'True'.
# La fonction prend en paramètre un tableau (tab).

def en_ordre(tab):
    ligne_elem_croissant = tab.copy()
    
    elem_precedant = 0
    index = 0
    for elem in tab:
        if elem == elem_precedant + 4:
            ligne_elem_croissant.insert(index-1, 1)
            ligne_elem_croissant.insert(index, 1)
            
        index += 1
        elem_precedant = elem
    print(ligne_elem_croissant)
    return ligne_elem_croissant

# Test unitaires ------------------------------------------------------


# Test unitaire de la fonction 'trouver_indice()'
def test_trouver_indice():
    # Cas de base
    assert trouver_indice([1, 3, 4, 6, 5], 4) == 2

    # Cas quand le paramètre a_trouvé
    # ne fait pas partie de la liste
    assert trouver_indice([1, 2, 3, 4, 5], 8) == False

    # Cas quand le tableau est vide
    assert trouver_indice([0], 8) == False

    # Cas quand le tableau ne contient pas d'éléments
    assert trouver_indice([], 5) == False


# Test unitaire de la fonction 'brasser()'
def test_brasser():
    tab = []
    for i in range(52):
        tab.append(i)

    tab_brasse = tab.copy()
    assert brasser(tab_brasse) != tab
    assert brasser([0]) == [0]
    assert brasser([]) == []


# Test unitaire de la fonction 'paquet_cartes()'
def test_paquet_cartes():
    # Cas de base
    assert paquet_cartes() == [
        'AC', 'AD', 'AH', 'AS', '2C', '2D', '2H', '2S', 
        '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S',
        '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S',
        '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S',
        '9C', '9D', '9H', '9S', '10C', '10D', '10H',
        '10S', 'JC', 'JD', 'JH', 'JS', 'QC', 'QD', 'QH',
        'QS', 'KC', 'KD', 'KH', 'KS']

# Test unitaire de la fonction 'lignes()'
def test_lignes():
    # Cas de base
    assert lignes(
        ["JS", "7S", "6S", "QS", "4C", "8D", "5C", "9S", "2H", "AC", "8H", "5D", "10C"],
        0,
    ) == (
        """<td id=case0><img src="cards/JS.svg"></td><td id=case1><img src="cards/7S.svg"></td><td id=case2><img src="cards/6S.svg"></td><td id=case3><img src="cards/QS.svg"></td><td id=case4><img src="cards/4C.svg"></td><td id=case5><img src="cards/8D.svg"></td><td id=case6><img src="cards/5C.svg"></td><td id=case7><img src="cards/9S.svg"></td><td id=case8><img src="cards/2H.svg"></td><td id=case9><img src="cards/absent.svg"></td><td id=case10><img src="cards/8H.svg"></td><td id=case11><img src="cards/5D.svg"></td><td id=case12><img src="cards/10C.svg"></td>"""
    )


# Procédure qui effectue tous les test unitaires du programme.
def test_unitaires():
    test_trouver_indice()

    test_brasser()

    test_paquet_cartes()

    test_lignes()


test_unitaires()
