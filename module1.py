# Créé par Aimen, le 08/05/2017 en Python 3.2
import pickle
scores=   {"Aimen":2, "lila":3,"Antoine":2,"Marie":1, "Jean":0
             }


with open('BestScoresSimon.txt', 'wb') as fichier: # on engistre les nouveaux scores dans le fichier
                score=pickle.Pickler(fichier)
                score.dump(scores)
