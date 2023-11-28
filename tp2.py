# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

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
