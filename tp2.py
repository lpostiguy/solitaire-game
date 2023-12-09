# Louis-Philippe Ostiguy
# Noah Tremblay Taillon
# 10 décembre 2023
#
# Ce programme, appelé dans un code HTML, permet de modifier ce code HTML afin
# de lancer unee partie d'Addiction Solitaire. Dans ce jeu, le joueur a comme
# but de placer en ordre de gauche à droite les carte allant du 2 jusqu'au
# roi, et ce en les les classant en couleur. Pour gagner, le joueur doit avoir
# réussi à placer toutes les cartes en ordre. Pour cela, il dispose de trois
# brasssages, permettant de brasser toutes les cartes sauf celles déjà bien
# placées. Les cartes pouvant être déplacées sont affichées en vert. Lorsque
# le joueur clique dessus, cette carte se place derrière la carte de la même
# couleur la précédant; par exemple, appuyer sur le 6 de coeur en surbrillance
# verte placera cette carte après le 5 de coeur. Le joueur perd lorsque'il ne
# peut plus brasser les cartes, et qu'aucune carte ne peut être déplacée (donc
# aucune carte n'est verte). Ce programme utilise un paquet où les cartes sont
# des valeurs de 0 à 51, où deux valeurs sont de la même couleur sur elle ont
# la même valeur à (carte % 4), et où deux valeurs ont le même nombres (as,
# 10, valet, ...) si leur valeur // 4 donnent la même chose. Ce même paquet a
# un équivalent utilisant un tableau de chaîne de caractères, où le premier
# élément d'une chaîne est la valeur de la carte, et le deuxième et la couleur,
# en anglais. Donc, l'as de coeur aurait la chaîne 'AH'.


import random
import math


# La procédure 'nouvelle_partie' ne prend pas de paramètre. Lorsque le bouton
# HTML 'nouvelle partie' est cliqué, cette procédure est appelée afin de créer
# une nouvelle partie. Bien que cette procédure ne fait qu'appeler init(), elle
# permet de mieux expliciter ce qui se passe à l'appuie du bouton.

def nouvelle_partie():
    init()


# La procédure 'init' ne prend pas de paramètre. Elle permet de créer une 
# nouvelle partie d'Addiction Solitaire. Pour ce faire, cette procédure 
# crée un paquet de carte, avec des nombres de 0 à 51, brasse ce paquet, et
# associe ces numéros brassés aux noms des cartes correspondantes. Elle
# appelle la procédure mise_a_jour_affichage, qui permet de lancer le jeu.

def init():
    
    # Initier les variables globales
    global cartes_br
    global noms_cartes
    global noms_cartes_br
    global brasse_restant

    # Nombre de brassage de cartes restant
    brasse_restant = 3

    # Tableau qui contiendra les numéros des cartes ordonnées
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
    noms_cartes_br = nombres_a_noms()
    
    # Met à jour le contenu de la page HTML
    mise_a_jour_affichage()
    


# La procédure 'mise_a_jour_affichage' ne prend pas de paramètre. Cette procédure
# modifie le code HTML de la page web, afin de mettre à jour le jeu au fur et 
# à mesure de l'avancement du joueur.

def mise_a_jour_affichage():

    # Paquet brassé avec le noms des cartes
    noms_cartes_br = nombres_a_noms()
    
    # Création des éléments HTML.
    ligne1 = lignes(noms_cartes_br[:13], 0)
    ligne2 = lignes(noms_cartes_br[13:26], 13)
    ligne3 = lignes(noms_cartes_br[26:39], 26)
    ligne4 = lignes(noms_cartes_br[39:], 39)

    # Changer le contenu HTML de l'élément ayant l'ID 'cb-body'
    racine = document.querySelector("#cb-body")
    racine.innerHTML = """
      <style>
        #jeu table { float:none; }
        #jeu table td { border:0; padding:1px 2px; height:auto; width:auto; }
        #jeu table td img { height:140px; }
        #jeu {padding-left: 10px;}
        #controles {padding-left: 10px;}
        #controles {padding-top: 5px;}
        #brasser {padding-top: 5px;}
        #brasser {padding-bottom: 5px;}
        #boutton {padding-top: 5px;}
        
      </style>
      <div id="jeu">
        <table>
          <tr>""" + ligne1 + """</tr>
          <tr>""" + ligne2 + """</tr>
          <tr>""" + ligne3 + """</tr>
          <tr>""" + ligne4 + """</tr>
        </table>
      </div>
    <div id="controles">
        <div id="brasser"></div>
        <div id="boutton">
        <button id="new-games" onclick="nouvelle_partie()">Nouvelle partie
        </button>
        </div>
    </div>"""

    # Affichage du bouton pour brasser les cartes
    bouton_brasser()

    # Matrice où les lignes sont composés de l'élément 0 qui est l'indice de 
    # la carte à mettre en vert, et l'élément 1 qui est l'indice où cette 
    # carte peut être déplacée.
    matrice_déplacements = voisins_as(noms_cartes_br)
    
    # Modification du code HTML pour mettre les cartes en verts et les rendre
    # cliquables
    cartes_vertes(matrice_déplacements)


# La procédure 'brasser_cartes' ne prend pas de paramètres. Elle brasse les
# cartes en tenant compte le nombre de brassage restant au joueur, modifiant
# ce nombre à chaque appel de la procédure. Elle prend aussi en compte les
# cartes déjà en ordre. Elle modifie les variables globales brasse_restant,
# qui contient le nombre de brassage restant à la partie, ainsi que cartes_br
# contenant les numéros des cartes brasés. Ensuite, elle modifie l'affichage
# du jeu en appelant mise_a_jour_affichage.

def brasser_cartes():
    global brasse_restant
    global cartes_br

    # Décrémente le nombre de brassé restant au joueur
    brasse_restant -= 1

    # Création de ligne du jeu, avec les cartes en ordre retirées des tableaux
    lignes = en_ordre(cartes_br[:13])
    ligne2 = en_ordre(cartes_br[13:26])
    ligne3 = en_ordre(cartes_br[26:39])
    ligne4 = en_ordre(cartes_br[39:])

    # Combiner les 4 lignes dans un tableau
    for i in ligne2:
        lignes.append(i)
    for i in ligne3:
        lignes.append(i)
    for i in ligne4:
        lignes.append(i)

    # Copie du tableau cartes_br
    cartes_br_copie = cartes_br.copy()
    
    # Tableau de cartes enlevées 
    tab_enleve = []
    
    # Enlever les cartes qui sont sont en ordre croissant
    for i in range(len(lignes)):
        
        # Les cartes qui on une valeurs de 99, sont en ordre
        if lignes[i] == 99:
            
            # Enlever les cartes qui sont en ordre du tableau qui
            # sera ensuite brassé, afin de les garder en place
            cartes_br_copie.remove(cartes_br[i])
            
            # Ajouter la carte enlevée dans le tableau des cartes enlevées
            tab_enleve.append(i)

    # Brasser les cartes
    brasser(cartes_br_copie)

    # Réinsérer les cartes qui sont en ordre dans le paquet de cartes brassées
    for i in tab_enleve:
        cartes_br_copie.insert(i, cartes_br[i])

    # Actualiser le paquet de carte brassé avec le nouveau paquet de carte qui 
    # conserve la place des cartes qui étaient en ordre.
    cartes_br = cartes_br_copie
    
    # Met à jour le contenu de la page HTML
    mise_a_jour_affichage()


# La fonction 'en_ordre' prend en paramètre un tableau non vide (tab). Elle 
# détecte les éléments (nombres entiers) qui sont en ordre croissant et qui ont
# une incrémentation de +1 entre eux, partant à la valeur 2, et à partir du 
# début du tableau. Les éléments en ordre sont remplacés par 99, un nombre 
# arbitraire non ambigüe avec les valeurs du paquet de cartes. La fonction 
# retourne le tableaun modifié, avec des 99 à la place des éléments biens 
# placés.
def en_ordre(tab):
    
    # Copie du tableau en paramètre 
    ligne_elem_croissant = tab.copy()
    
    # Initialisation de l'élément précédent
    elem_precedant = ligne_elem_croissant[0]
    
    # Index des cartes du tableau
    index = 1
    
    # Détecte si la première carte du tableau est de valeur 2, soit que
    # la valeur // 4 donne 1.
    if ligne_elem_croissant[0] // 4 == 1 or ligne_elem_croissant[0] == 8:
        
        # Remplace le 2 par 99 (chiffre pour représenté que la carte est en ordre)
        ligne_elem_croissant.insert(index - 1, 99)
        ligne_elem_croissant.remove(ligne_elem_croissant[index])

        # Détecte si les cartes sont en ordres croissant, +1 entre chaque carte
        for elem in ligne_elem_croissant[1:]:
            if elem == elem_precedant + 4:
                ligne_elem_croissant.insert(index, 99)
                ligne_elem_croissant.remove(ligne_elem_croissant[index + 1])
                
            # Si la carte suivant la carte de valeur 2 n'est pas en ordre, alors
            # ça ne sert à rien de vérifier les autres cartes de la ligne.
            else:
                break
            
            index += 1
            
            # Garder en mémoire l'élément précédant
            elem_precedant = elem
        
    return ligne_elem_croissant

# Tests unitaires de la fonction 'en_ordre()'

def test_en_ordre():
    assert en_ordre([1,2,3,4,5]) == [1,2,3,4,5]
    assert en_ordre([5,9,10,14]) == [99,99,10,14]
    assert en_ordre([5,7,11,15]) == [99,7,11,15]
    assert en_ordre([12,16,20,24]) == [12,16,20,24]

# La fonction 'brasser' prend en paramètre un tableau (tab) ne contenant que
# des éléments allant de 0 à 51 en ordre croissant. Ce tableau sera
# mélangé selon le principe suivant : échangeons le dernier élément n du
# tableau et échangeons le avec un élément aléatoire le précédant. Puis,
# même chose avec n-1, jusqu'à ce que tous les éléments aient été échangés.
# La fonction retourne ce tableau mélangé.

def brasser(tableau):

    for i in range(len(tableau)):
        # Variable permettant de cycler au travers des éléments du tableau, en
        # partant par la fin.
        indice_dernier_element = len(tableau) - 1 - i

        # Choix aléatoire précédant le dernier élément
        aleatoire = math.floor(random.random() * len(tableau) - 1 - i)

        # Échanger les éléments
        temp = tableau[indice_dernier_element]
        tableau[indice_dernier_element] = tableau[aleatoire]
        tableau[aleatoire] = temp
        
    return tableau
    

# Test unitaire de la fonction 'brasser()'

def test_brasser():
    tab = []
    for i in range(52):
        tab.append(i)

    tab_brasse = tab.copy()
    assert brasser(tab_brasse) != tab
    assert brasser([0]) == [0]
    assert brasser([]) == []


# La fonction 'ligne' prend en paramètre un tableau de chaînes de caractères
# non vide représentant le nom des cartes (tab_valeurs), un entier 
# correspondand à l'indice du premier élément de la ligne active (case). Elle 
# retourne le code HTML permettant d'afficher une ligne d'un tableau HTML avec
# chaque carte. Elle assigne une image à chaque nom présent dans le tableau 
# tab_valeur. De plus, elle retire les as, les transformant en cases vides. 
# Elle retourne la chaîne de caractères correspondant à une ligne du jeu en 
# HTML, soit un tableau d'images.

def lignes(tab_valeurs, case):
    
    ligne = ""

    for i in tab_valeurs:

        # Cas où la carte est un as. Mettre 'absent' dans le code de l'image
        if "A" in i:
            ligne += (
                """<td id=case""" + str(case) 
                + """><img src="cards/absent.svg"></td>"""
            )
            
        # Cas pour toutes les autres cartes
        else:
            ligne += (
                """<td id=case"""
                + str(case)
                + """><img src="cards/"""
                + i
                + """.svg"></td>"""
            )
        case += 1  # Ajustement de la case, pour la prochaine carte
        
    return ligne


# Test unitaire de la fonction 'lignes()'

def test_lignes():
    # Cas de base
    assert lignes(
        ["JS", "7S", "6S", "QS", "4C", "8D", "5C", "9S", "2H", "AC", "8H",\
         "5D", "10C"],
        0,) == (
        """<td id=case0><img src="cards/JS.svg"></td>"""
        +"""<td id=case1><img src="cards/7S.svg"></td>"""
        +"""<td id=case2><img src="cards/6S.svg"></td>"""
        +"""<td id=case3><img src="cards/QS.svg"></td>"""
        +"""<td id=case4><img src="cards/4C.svg"></td>"""
        +"""<td id=case5><img src="cards/8D.svg"></td>"""
        +"""<td id=case6><img src="cards/5C.svg"></td>"""
        +"""<td id=case7><img src="cards/9S.svg"></td>"""
        +"""<td id=case8><img src="cards/2H.svg"></td>"""
        +"""<td id=case9><img src="cards/absent.svg"></td>"""
        +"""<td id=case10><img src="cards/8H.svg"></td>"""
        +"""<td id=case11><img src="cards/5D.svg"></td>"""
        +"""<td id=case12><img src="cards/10C.svg"></td>"""
    )

# La fonction 'paquet_cartes' ne prend pas de paramètre. Elle retourne une
# liste contenant toutes les cartes d'un jeu de cartes classique en ordre
# croissant en couleur, commençant par le trèfle (C), le carreaux (D), le coeur
# (H), puis le pique (S). Ce paquet ne contient pas de Jokers. Pour ce faire,
# la fonction cycle au travers des quatres couleurs, et leur ajoute les
# valeurs. De plus, cette fonction ajoute les figures et les as. Le paquet
# complet est retourné.

def paquet_cartes():
    
    # Tableau qui contiendra toutes les cartes
    noms_cartes = []
    
    # Tableau contenant toutes les couleurs, en anglais
    noms_couleurs = ["C", "D", "H", "S"]

    # Création de la liste de toutes les valeurs de cartes, dans toutes les
    # couleurs. Commencer par cycler au travers de toutes les valeurs.
    for i in range(1, 14):
        
        # Cycler au travers des 4 couleurs
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


# La procédure 'nombres_a_noms' ne prend pas de paramètre. Elle utilise les 
# variables globales cartes_br et noms_cartes afin d'associer les chiffres du
# tableau cartes_br aux indices du tableau noms_cartes afin de mélanger 
# noms_cartes de la même manière que cartes_br. Elle retourne alors un nouveau
# tableau, un doublon de carte_br, mais avec le nom des cartes.

def nombres_a_noms ():
    tab_noms = []
    for i in cartes_br:
        for k in range(len(noms_cartes)):
            if k == i:

                # Crée un nouveau tableau mélangé, avec le nom des cartes
                tab_noms.append(noms_cartes[k])
    return tab_noms


# La procédure 'bouton_brasser' ne prend pas de paramètre. Elle utilise le
# paramètre global brasse_restant, qui contient le nombre de brassage restant
# au joueur. Cette procédure modifie le code HTML de la page web pour changer
# l'affichage du bouton brasser; s'il ne reste plus de brassage disponible,
# le bouton disparait. Sinon, on affiche le bouton avec le compteur.

def bouton_brasser():
    brasseur = document.querySelector("#brasser")
    
    # Si le joueur à gagné la partie
    if partie_gagne():
        brasseur.innerHTML = "Vous avez réussi! Bravo!"
    
    # Si le joueur n'à plus de brassage de cartes restant
    elif brasse_restant == 0:
        brasseur.innerHTML = """Vous ne pouvez plus brasser les cartes"""

    # Si le joueur à encore des brassages de cartes restant
    else:
        brasseur.innerHTML = (
            """Vous pouvez encore <button id="brasser_cartes" 
            onclick="brasser_cartes()"> brasser les cartes</button> """ 
            + str(brasse_restant) + " fois")


# La procédure 'cartes_vertes' prend en paramètre une matrice. L'élément à 
# l'indice 0 de chaque ligne de la matrice corresopnd à l'indice d'une carte
# qui doit être mise en vert. L'indice 1 de chaque ligne correspond à l'indice
# de la position où cette carte peut être déplacée, si elle est cliquée. Cette
# procédure modifie le code HTML afin de mettre en vert les cartes qui le 
# doivent, et leur ajoute la possibilité d'être déplacées.

def cartes_vertes (matrice):
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


# La procédure 'bouger' prend en paramètre un indice d'origine et un indice de
# destination. Elle utilise le tableau global cartes_br et échange l'élément
# à l'indice d'origne avec l'élément à l'indice de destination. Ensuite,
# elle met à jour l'affichage du jeu pour prendre en compte cette 
# modification, en appelant mise_a_jour_affichage..

def bouger(origine, destination):
    temp = cartes_br[origine]
    cartes_br[origine] = cartes_br[destination]
    cartes_br[destination] = temp

    mise_a_jour_affichage()


# La fonction voisins_as prend en paramètre un tableau brassé ayant le noms des
# cartes (noms_cartes_brasse). Cette fonction trouve les as dans le paquet,
# trouve la valeur de la carte la précédant, et la carte qui devrait aller à la
# place de l'as. Elle retourne donc un tableau dont le premier élément est
# l'indice de la carte pouvant être déplacée, et dont le deuxième élément est
# l'indice de la position où elle peut être déplacée. Étant donnée le caractère
# aléatoire de cartes_br, cette fonction ne possède pas de tests unitaires.

def voisins_as(noms_cartes_brasse):
    
    index = 0 # Variable comparant les indices

    # Tableau contenant les indices des voisins des as
    index_carte_suivante = []

    # Passe à travers toutes les cartes du paquet
    for carte in cartes_br:
        
        # Trouver l'indice d'une carte dans le paquet mélangé
        index = trouver_indice(cartes_br, carte)
        
        # Si la carte est un AS
        if carte // 4 == 0:
            
            # Nom de la carte
            valeur_carte = noms_cartes_brasse[index]
            
            # Indice de ce nom de carte dans le paquet ordonné avec les
            # noms de cartes
            index_noms_cartes = trouver_indice(noms_cartes, valeur_carte)

            # Pour que la première case donne la possibilité de mettre toutes
            # les cartes ayant la valeur 2
            if index == 0 or index == 13 or index == 26 or index == 39:
                for deux in range(4, 8):
                    index_carte_suivante.append(
                        [trouver_indice(cartes_br, deux), index]
                    )
                    
            # Si il y a plusieurs AS à la suite de l'autre
            if cartes_br[index - 1] // 4 == 0:
                continue
            
            # Si la carte est un roi, continue car rien ne peut suivre cette 
            # carte
            if cartes_br[index - 1] + 4 > 51:
                continue

            else:
                # Valeur de la carte précédant la case vide (AS)
                valeur_carte = noms_cartes_brasse[index - 1]

                # Index de la carte devant l'as dans noms_cartes
                index_noms_cartes = trouver_indice(noms_cartes, valeur_carte)

                # Index de la carte suivante après la carte qui se trouve avant
                # la carte vide (AS)
                index_suivant = trouver_indice(
                    noms_cartes_brasse, noms_cartes[index_noms_cartes + 4]
                )

                # Ajouter la carte suivante au tableau qui contient la
                # liste de carte à afficher en vert
                index_carte_suivante.append([index_suivant, index])
    
    return index_carte_suivante


# La fonction 'trouver_indice' prend en paramètre un tableau (tab) et un 
# élément à chercher dans ce tableau (a_trouver). Si l'élément n'est pas
# présent dans le tableau, la fonction retourne False. Sinon, cette 
# fonction retourne l'indice de l'élément à chercher.

def trouver_indice(tab, a_trouver):
    
    # Cas si le tableau est vide
    if len(tab) == 0:
        return False
    
    else:
        
        # Si on trouve a_trouver
        for i in range(len(tab)):
            if tab[i] == a_trouver:
                return i
        # Si l'élément ne fut pas trouvé
        return False


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


# La fonction 'partie_gagne' ne prend pas de paramètre. Cette fonction détecte
# si une partie est gagnée, soit si toutes les cartes du jeu sont en ordres
# croissant, en couleur. La fonction retourne un booléen; True pour une partie
# gagnée et False pour une partie non gagnée. Étant donnée le caractère
# aléatoire de cartes_br, cette fonction ne possède pas de tests unitaires.

def partie_gagne():
    global cartes_br
    
    # Création de ligne du jeu, avec carte en ordre retiré des tableaux
    tab_cartes = en_ordre(cartes_br[:13])
    ligne2 = en_ordre(cartes_br[13:26])
    ligne3 = en_ordre(cartes_br[26:39])
    ligne4 = en_ordre(cartes_br[39:])
    
    # Combiner les quatres lignes dans un tableau
    for i in ligne2:
        tab_cartes.append(i)
    for i in ligne3:
        tab_cartes.append(i)
    for i in ligne4:
        tab_cartes.append(i)
    
    # Tableau de cartes enlevées 
    tab_carte_en_ordre = []
    
    # Ajouter les cartes qui sont en ordre croissant
    for i in range(len(tab_cartes)):
        
        # Les cartes qui on une valeurs de 99, sont en ordre (provient de la
        # fonction en_ordre)
        if tab_cartes[i] == 99:
            # Ajouter la cartes en ordre dans le tableau
            tab_carte_en_ordre.append(i)
    
    # Vérifie si les 52 cartes sont en ordre    
    if len(tab_carte_en_ordre) == 52:
        return True # Cas de victoire
    else:
        return False # Cas de non victoire


# Procédure qui effectue tous les test unitaires du programme.

def test_unitaires():
    test_trouver_indice()

    test_brasser()

    test_paquet_cartes()

    test_lignes()

    test_en_ordre()

test_unitaires()
