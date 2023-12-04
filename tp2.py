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
    ligne1 = lignes(noms_cartes_br[:13], 0)
    ligne2 = lignes(noms_cartes_br[13:26], 13)
    ligne3 = lignes(noms_cartes_br[26:39], 26)
    ligne4 = lignes(noms_cartes_br[39:], 39)

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
        Vous pouvez encore <button id="brasser_cartes" onclick="brasser_cartes(cartes_br, noms_cartes, noms_cartes_br)">
        brasser les cartes</button>
        """
            + str(brasse_restant)
            + " fois"
        )

    # changer la couleur de fond de la case 0
    #print("premièrement",noms_cartes_br)
    #print(cartes_br)
    #print(noms_cartes_br)
    #print("aaaaa")
    tab = voisins_as(noms_cartes_br, cartes_br)
    #print(cartes_br)
    print(tab)
    
    for i in tab:
        #print(i)
        case_verte = cartes_br.index(i)
        #print(case_verte)
        cas = document.querySelector("#case" + str(i))
        cas.setAttribute("style", "background-color: lime")
    #case0 = document.querySelector("#case0")
    #case0.setAttribute("style", "background-color: lime")


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
    tableau = tab.copy()
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
    ligne = ""
    
    #tab_case = [] # Tableau qui contiendra les numéro des cases
    
    for i in tab:
        #print(i)
        #for k in range(nb_1, nb_2):
        index = tab.index(i)
        
        
        # Cas où la carte est un as
        if "A" in i:
            ligne += (
                """<td id=case"""
                + str(case)
                + """><img src="cards/absent.svg"></td>"""
            )
        else:
            ligne += (
                """<td id=case"""
                + str(case)
                + """><img src="cards/"""
                + i
                + """.svg"></td>"""
            )
        case += 1 # Ajustement de la case, pour la prochaine
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



# Fonction qui donne la carte qui doit suivre. 
# TODO : problème quand l'as est la première carte d'une ligne
    # (une carte en vert est la carte suivant la denrière de la ligne 
    # précédente, alors que ça doit être un 2)
# TODO : problème quand il y a deux as de suite
    # (donne un 2, puisque le second as suit une as. Mais, devrait 
    # ne rien donner)
def voisins_as (noms_cartes_brasse, cartes_brasse):
    indexe = 0
    print(noms_cartes_brasse)
    print(cartes_brasse)
    #print(cartes_br)
    #print("noms_cartes_br",noms_cartes_brasse)
    # tableau contenant les indices des voisins des as
    indexes_carte_suivante = [] 
    for carte in cartes_brasse:
        #print(carte)
        
        indexe = cartes_brasse.index(carte)
        if carte // 4 == 0: # Si c'est un as
            carte_avant_as = indexe-1
            #print("index",indexe)
            # valeur de noms_cartes selon l'indexe
            valeur_carte = noms_cartes_brasse[indexe-1]
            #print(valeur_carte) 
            print('carte devant un as: ',noms_cartes_brasse[indexe-1])
            
            # index de la carte devant l'as dans noms_cartes
            indexe_noms_cartes = noms_cartes.index(valeur_carte) 
            #print("",noms_cartes[indexe_noms_cartes+4])
            
            # Si la carte est un roi, continue car rien ne peut suivre cette carte
            if indexe_noms_cartes+4 > 51 :
                #print("C'est un roi\n")
                continue
            
            #print('Carte qui doit suivre:', 
            #      noms_cartes[indexe_noms_cartes+4], '\n')
            
            #indexes_carte_suivante.append(noms_cartes_brasse.index(noms_cartes[indexe_noms_cartes+4]))
            #print(noms_cartes_brasse.index(noms_cartes[indexe_noms_cartes+4]))
            print("indexe_noms_cartes",indexe_noms_cartes)
            print("indice de",noms_cartes[indexe_noms_cartes+4], ":", noms_cartes_brasse.index(noms_cartes[indexe_noms_cartes+4]))
            
            indice_suivant = noms_cartes_brasse.index(noms_cartes[indexe_noms_cartes+4])
            print("carte suivant",noms_cartes_brasse[indice_suivant], "\n")
            indexes_carte_suivante.append(noms_cartes_brasse.index(noms_cartes[indexe_noms_cartes+4]))
            
    return indexes_carte_suivante
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
"""
        'AC', 'AD', 'AH', 'AS', '2C', '2D', '2H', '2S', 
        '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S',
        '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S',
        '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S',
        '9C', '9D', '9H', '9S', '10C', '10D', '10H',
        '10S', 'JC', 'JD', 'JH', 'JS', 'QC', 'QD', 'QH',
        'QS', 'KC', 'KD', 'KH', 'KS']
"""

# Procédure qui effectue tous les test unitaires du programme.
def testUnitaires():
    testBrasser()


testUnitaires()

"""
cartes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,\
          19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,\
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
cartes_br = [21, 19, 38, 2, 29, 10, 7, 1, 45, 16, 15, 23, 5, 43, 41, 22, 40,\
             11, 26, 33, 6, 12, 0, 36, 44, 39, 51, 20, 49, 37, 48, 31, 24, 3,\
             4, 42, 28, 18, 50, 8, 27, 17, 9, 25, 46, 34, 14, 30, 13, 32, 35, 47]
noms_cartes = ['AC', 'AD', 'AH', 'AS', '2C', '2D', '2H', '2S', '3C', '3D', \
               '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', \
               '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', '8C', '8D', \
               '8H', '8S', '9C', '9D', '9H', '9S', '10C', '10D', '10H', '10S',\
               'JC', 'JD', 'JH', 'JS', 'QC', 'QD', 'QH', 'QS', 'KC', 'KD',\
               'KH', 'KS']
noms_cartes_br = ['6D', '5S', '10H', 'AH', '8D', '3H', '2S', 'AD', 'QD', '5C',\
                  '4S', '6S', '2D', 'JS', 'JD', '6H', 'JC', '3S', '7H', '9D', \
                  '2H', '4C', 'AC', '10C', 'QC', '10S', 'KS', '6C', 'KD', \
                  '10D', 'KC', '8S', '7C', 'AS', '2C', 'JH', '8C', '5H', 'KH',\
                  '3C', '7S', '5D', '3D', '7D', 'QH', '9H', '4H', '8H', '4D',\
                  '9C', '9S', 'QS']


for carte in cartes_br:
    
    indexe = cartes_br.index(carte)
    if carte // 4 == 0: # Si c'est un as
        carte_avant_as = indexe-1
        
        valeur_carte = noms_cartes_br[indexe-1] # valeur de noms_cartes selon l'indexe
        print('carte devant un as: ',noms_cartes_br[indexe-1])
        
        indexe_noms_cartes = noms_cartes.index(valeur_carte) # index de la carte devant l'as dans noms_cartes
        print('Carte qui doit suivre:',noms_cartes[indexe_noms_cartes+4], '\n')
"""
