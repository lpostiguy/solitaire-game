# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

import random
import math


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
        indice_dernier_element = len(tab)-1-i
        
        # Choix aléatoire précédant le dernier élément
        aleatoire = math.floor(random.random()*len(tab)-1-i)

        temp = tab[indice_dernier_element]
        tab[indice_dernier_element] = tab[aleatoire]
        tab[aleatoire] = temp
    return tab


# Difficile de faire un test unitaire
def testBrasser():
    tab = []
    for i in range(52):
        tab.append(i)
        
    tab_brasse = tab.copy()
    assert brasser(tab_brasse) != tab
    assert brasser([0]) == [0]
    assert brasser([]) == []


# La fonction 'paquet_cartes' ne prend pas de paramètre. Elle retourne une
# liste contenant toutes les cartes d'un jeu de cartes classique en ordre 
# croissant en couleur, commençant par le trèfle (C), le carreaux (D), le coeur
# (H) puis le pique (S). Ce paquet ne contient pas de Jokers. Pour ce faire, 
# la fonction cycle au travers des quatres couleurs, et leur ajoute les 
# 'nombres'. De plus, cette fonction ajoute les figures et les as.
def paquet_cartes ():
    
    noms_cartes = []
    noms_couleurs = ["C", "D", "H", "S"]
    # Essaie de faire la liste des noms de cartes automatiquement
    # On a 1 = ace, 11 = valet,
    for i in range(1, 14):
        
        # Cycler au travers des 4 couleurs pour ajouter toutes les possibilités
        for couleur in noms_couleurs:
            
            # Si c'est un as, ajouter A
            if i == 1:
                noms_cartes.append('A' + couleur)
            
            # Si c'est un valet, ajouter J
            elif i == 11:
                noms_cartes.append('J' + couleur)
            
            # Si c'est une dame, ajouter Q
            elif i == 12:
                noms_cartes.append('Q' + couleur)
            
            # Si c'est un roi, ajouter K
            elif i == 13:
                noms_cartes.append('K' + couleur)
                
            # Si c'est une chiffre normal
            else:
                noms_cartes.append(str(i) + couleur)
    return noms_cartes


# Test unitaire de la fonction 'paquet_cartes()'
def test_paquet_cartes():
    assert paquet_cartes == ['AC', 'AD', 'AH', 'AS', '2C', '2D', '2H', '2S', 
                             '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S',
                             '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S',
                             '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S',
                             '9C', '9D', '9H', '9S', '10C', '10D', '10H',
                             '10S', 'JC', 'JD', 'JH', 'JS', 'QC', 'QD', 'QH',
                             'QS', 'KC', 'KD', 'KH', 'KS']


def init():

    # changer le contenu HTML de l'élément racine
    racine = document.querySelector("#cb-body")
    racine.innerHTML = """
      <style>
        #jeu table { float:none; }
        #jeu table td { border:0; padding:1px 2px; height:auto; width:auto; }
        #jeu table td img { height:140px; }
      </style>
      <div id="jeu">
        <table>
          <tr>
            <td id="case0"><img src="cards/2S.svg"></td>
            <td id="case1"><img src="cards/QH.svg"></td>
          </tr>
          <tr>
            <td id="case2"><img src="cards/JC.svg"></td>
            <td id="case3"><img src="cards/10D.svg"></td>
          </tr>
        </table>
      </div>"""

    # changer la couleur de fond de la case 0
    case0 = document.querySelector("#case0")
    case0.setAttribute("style", "background-color: lime")
