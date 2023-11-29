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
