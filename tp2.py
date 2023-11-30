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

    # Met à jour le contenu de la page HTML
    mise_a_jour_affichage(cartes_br, noms_cartes, noms_cartes_br)


# Procédure qui met à jour le contenu HTML de la page web.
# La procédure prend en paramètres 3 tableau, un tableau de cartes
# brassées (sous forme de chiffre, 0 à 52), un tableau contenant le
# numéro et l'enseigne des cartes, en ordre, et un tableau contenant
# le noms_des cartes brassées.
def mise_a_jour_affichage(cartes_br, noms_cartes, noms_cartes_br):
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
                index_carte = cartes_br.index(1)

                # Crée un nouveau tableau mélangé, avec le nom des cartes
                noms_cartes_br.append(noms_cartes[k])

    # Création des éléments HTML. Ces lignes n'ont déjà plus les as
    # Moyen de faire ça plus efficacement?
    ligne1 = lignes(noms_cartes_br[:13])
    ligne2 = lignes(noms_cartes_br[13:26])
    ligne3 = lignes(noms_cartes_br[26:39])
    ligne4 = lignes(noms_cartes_br[39:])

    # changer le contenu HTML de l'élément racine
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
      </div>"""
    )
    brasseur = document.querySelector("#brasser")

    # Si le joueur n'à plus de brassage de cartes restant
    if brasse_restant == 0:
        brasseur.innerHTML = """Vous ne pouvez plus brasser les cartes"""

    # Si le joueur à encore des brassages de cartes restant
    else:
        brasseur.innerHTML = (
            """
        Vous pouvez encore <button id="brasser_cartes" onclick="brasser_cartes(cartes_br, noms_cartes, noms_cartes_br)">
        brasser les cartes</button>
        """
            + str(brasse_restant)
            + " fois"
        )

    # changer la couleur de fond de la case 0
    case0 = document.querySelector("#case0")
    case0.setAttribute("style", "background-color: lime")


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
def brasser(tab):
    for i in range(len(tab)):
        # Variable permettant de cycler au travers des éléments du tableau, en
        # partant par la fin.
        indice_dernier_element = len(tab) - 1 - i

        # Choix aléatoire précédant le dernier élément
        aleatoire = math.floor(random.random() * len(tab) - 1 - i)

        temp = tab[indice_dernier_element]
        tab[indice_dernier_element] = tab[aleatoire]
        tab[aleatoire] = temp
    return tab


# La fonction 'ligne' prend en paramètre un tableau de chaînes de caractères
# non vide (tab). Elle retourne le code html permettant d'afficher une ligne
# d'un tableau HTML de chaque carte. Elle assigne une image à chaque nom
# présent dans le tableau (tab). De plus,elle retire les as, les transformant
# en cases vides.
def lignes(tab):
    ligne = ""

    for i in tab:
        index = tab.index(i)

        # Cas où la carte est un as
        if "A" in i:
            ligne += (
                """<td id=case"""
                + str(index)
                + """><img src="cards/absent.svg"></td>"""
            )
            continue

        ligne += (
            """<td id=case"""
            + str(index)
            + """><img src="cards/"""
            + i
            + """.svg"></td>"""
        )
    return ligne


# Procédure qui brasse les cartes en tenant compte du nombre de
# brassé restant au joueur.
# La procédure prend en paramètres 3 tableau, un tableau de cartes
# brassées (sous forme de chiffre, 0 à 52), un tableau contenant le
# numéro et l'enseigne des cartes, en ordre, et un tableau contenant
# le noms_des cartes brassées.
def brasser_cartes(cartes_br, noms_cartes, noms_cartes_br):
    global brasse_restant

    # Décrémente le nombre de brassé restant au joueur
    brasse_restant -= 1

    # Brasse les cartes
    cartes_br = brasser(cartes_br)

    # Met à jour le contenu de la page HTML
    mise_a_jour_affichage(cartes_br, noms_cartes, noms_cartes_br)


# Test unitaires ---------------------------------------------


# Difficile de faire un test unitaire
def testBrasser():
    tab = []
    for i in range(52):
        tab.append(i)

    tab_brasse = tab.copy()
    assert brasser(tab_brasse) != tab
    assert brasser([0]) == [0]
    assert brasser([]) == []


# Test unitaire de la fonction 'paquet_cartes()'
def test_paquet_cartes():
    assert paquet_cartes == [
        'AC', 'AD', 'AH', 'AS', '2C', '2D', '2H', '2S', 
        '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S',
        '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S',
        '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S',
        '9C', '9D', '9H', '9S', '10C', '10D', '10H',
        '10S', 'JC', 'JD', 'JH', 'JS', 'QC', 'QD', 'QH',
        'QS', 'KC', 'KD', 'KH', 'KS']


# Procédure qui effectue tous les test unitaires du programme.
def testUnitaires():
    testBrasser()


testUnitaires()
