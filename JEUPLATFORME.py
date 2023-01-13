#IMPORTATIONS DE MODULE:

#Pour l'accueil et les 3 jeux
from tkinter import *   # On importe tout le module tkinter




#NOTE A L'UTILISATEUR : Veillez bien à mettre dans le même dossier le fichier python, les 4 images, et le dossier contenant les sons du simon nommé "sons".
#L'ACCUEILL :

Accueil= Tk()                                                                   #fenêtre principale pour le choix du jeu
accueil = Canvas(Accueil, width=1350, height= 550, bg="ivory")                  #canvas principal
accueil.pack()


Button(Accueil,text='Valider', command=Accueil.destroy).pack(side=BOTTOM)   #Bouton pour quitter

Cj=PhotoImage(file="Choixjeu.gif")
accueil.create_image(650, 50, image=Cj)

bgm=PhotoImage(file="Bckgm.gif")                                                #importation des images
accueil.create_image(650, 300, image=bgm, tag="backgammon")

p4=PhotoImage(file="puissance4.gif")
accueil.create_image(250,300, image=p4, tag="puissance")

sim= PhotoImage(file="simon.gif")
accueil.create_image(1050,300,image=sim, tag="simon")

jeu_choisi=0                                                                    #variable globale
rectangle=0


def choix(event):                                                               # en fonction du clic on change la variable
    global jeu_choisi, rectangle
    accueil.delete(rectangle)
    if 100<event.x<400:
        jeu_choisi="puissance"
        rectangle=accueil.create_rectangle(100,100,400,500, outline="blue", width=5)
    elif 500<event.x<800:
        jeu_choisi="backgammon"
        rectangle=accueil.create_rectangle(500,105,800,490, outline="blue", width=5)
    elif 900<event.x<1200:
        jeu_choisi="simon"
        rectangle=accueil.create_rectangle(900,100,1200,500, outline="blue", width=5)



accueil.bind("<Button-1>", choix)
Accueil.mainloop()

if jeu_choisi=="backgammon":
    from tkinter import *
    from random import randint # On importe randint du module random

    def triangle_noirhaut(abscisse, ordonnee):                                      #crée un triangle noir tourné vers le haut et avec abscisse et  du premier point (le plus à gauche) en paramètres
        can.create_polygon(abscisse, ordonnee, abscisse+50, ordonnee-350, abscisse+100 ,ordonnee , fill="black")

    def triangle_blanchaut(abscisse, ordonnee):                                     #crée un triangle marron tourné vers le haut et avec abscisse et  du premier point (le plus à gauche) en paramètres
        can.create_polygon(abscisse,ordonnee , abscisse+50, ordonnee-350, abscisse+100 ,ordonnee , fill="#B9121B" )

    def triangle_noirbas(abscisse,ordonnee ):                                       #crée un triangle noir tourné vers le bas et avec abscisse et  du premier point (le plus à gauche) en paramètres
        can.create_polygon(abscisse,ordonnee, abscisse+50, ordonnee+350, abscisse+100, ordonnee, fill="black")

    def triangle_blancbas(abscisse,ordonnee ):                                      #crée un triangle marron tourné vers le bas et avec abscisse et  du premier (le plus à gauche) point en paramètres
        can.create_polygon(abscisse,ordonnee, abscisse+50, ordonnee+350, abscisse+100,ordonnee , fill="#B9121B" )



    pair=[0,2,4,6]                                                                  #liste des chiffres pairs utilisée plus tard
    impair=[1,3,5]                                                                  #liste des chiffres impairs utilisée plus tard




    def plateau():                                                                  #fonction qui crée le plateau de jeu
        for i in range (6):                                                         #crée le jan gauche rouge
            x=0+100*i                                                               #abcisse du premier point
            y=0                                                                     # du premier point
            if i in impair:                                                         #pour alterner triangles noirs et clairs
                triangle_noirbas(x,y)
            if i in pair:
                triangle_blancbas(x,y)
        can.create_line(650,0,650,800, width=50, fill="black")                      #crée la barre centrale
        for i in range (6):                                                         #crée le jan droit rouge
            x=700+100*i
            y=0
            if i in impair:
                triangle_noirbas(x,y)
            if i in pair:
                triangle_blancbas(x,y)
        for i in range (6):                                                         #crée le jan gauche blanc
            x=0+100*i
            y=800
            if i in pair:
                triangle_noirhaut(x,y)
            if i in impair:
                triangle_blanchaut(x,y)
        for i in range (6):                                                         #crée le jan droit blanc
            x=700+100*i
            y=800
            if i in pair:
                triangle_noirhaut(x,y)
            if i in impair:
                triangle_blanchaut(x,y)





    coordonnee=[[], [], [], [], [], [], [], [], [],[], [], [], []]                  #Liste avec toutes les cos pour les pions...
    n=0
    for j in range (13):                                                            #fonctionne en colonnes (de 0 à 12)
        for i in range (5):                                                         #et en lignes (10 par colonne/ 5 par triangle avec pour  0 2 4 6... 18
            coordonnee[n].append(20+100*j)
            coordonnee[n].append(10+70*i)
        n+=1

    n=0
    for j in range (13):                                                            #lignes du bas
        for i in range (5):
            coordonnee[n].append(20+100*j)
            coordonnee[n].append(450+70*i)
        n+=1



    def pionrouge(lettre, rangee):                                                  #Affiche un pion rouge avec les cos en paramètre : colonne/ligne
        var1=can.create_oval(coordonnee[lettre][rangee], coordonnee[lettre][rangee+1], coordonnee[lettre][rangee]+60, coordonnee[lettre][rangee+1]+60, fill="red", tag=("rouge", "pion"))
        return var1

    def pionblanc (lettre, rangee):                                                 #Affiche un pion blanc avec les cos en paramètre
        var2=can.create_oval(coordonnee[lettre][rangee], coordonnee[lettre][rangee+1], coordonnee[lettre][rangee]+60, coordonnee[lettre][rangee+1]+60, fill="white", tag=("blanc", "pion"))
        return var2





    def mise_en_place():                                                            #met les pions du début en place. On utilise les cos de la liste créée plus haut : (colonne, ligne)
        global pion_actif, joueur, p_r_1,p_r_2,p_r_3,p_r_4,p_r_5,p_r_6,p_r_7p_r_8,p_r_9,p_r_10,p_r_11p_r_12,p_r_13,p_r_14,p_r_15 , p_b_1,p_b_2,p_b_3,p_b_4,p_b_5,p_b_6,p_b_7,p_b_8,p_b_9,p_b_10,p_b_11,p_b_12,p_b_13p_b_14,p_b_15

        p_b_1=pionblanc(12,0)
        p_b_2=pionblanc(12,2)
        p_b_3=pionblanc(7,10)
        p_b_4=pionblanc(7,12)
        p_b_5=pionblanc(7,14)
        p_b_6=pionblanc(7,16)
        p_b_7=pionblanc(7,18)
        p_b_8=pionblanc(4,14)
        p_b_9=pionblanc(4,16)
        p_b_10=pionblanc(4,18)
        p_b_11=pionblanc(0,0)
        p_b_12=pionblanc(0,2)
        p_b_13=pionblanc(0,4)
        p_b_14=pionblanc(0,6)
        p_b_15=pionblanc(0,8)

        p_r_1=pionrouge(0,10)
        p_r_2=pionrouge(0,12)
        p_r_3=pionrouge(0,14)
        p_r_4=pionrouge(0,16)
        p_r_5=pionrouge(0,18)
        p_r_6=pionrouge(4,0)
        p_r_7=pionrouge(4,2)
        p_r_8=pionrouge(4,4)
        p_r_9=pionrouge(7,0)
        p_r_10=pionrouge(7,2)
        p_r_11=pionrouge(7,4)
        p_r_12=pionrouge(7,6)
        p_r_13=pionrouge(7,8)
        p_r_14=pionrouge(12,16)
        p_r_15=pionrouge(12,18)

        pion_actif=-1
        joueur=0                                                                    #joueur 1 pions blancs et joueur 2 pions rouges



    def les_des():                                                                  #affiche un résultat aléatoire pour le tirage des dés
        global de1, de2, joueur, pion_actif                                         #variable globale
        d1.delete("all")                                                            #supprime la dernière valeur du tirage
        d2.delete("all")
        can.itemconfig(pion_actif, outline="black", width=1)                        #deselectionne le pion actif
        pion_actif=-1                                                               #variable pion_actif devient -1 et on peut sélectionner un nouveau pion
        de1=randint(1,6)                                                            #détermine la valeur de chaque dé
        de2=randint(1,6)
        d1.create_text(25, 25, text=de1, fill="white", font="bold")                 #affiche les valeurs dans les canvas d1 et d2
        d2.create_text(25, 25, text=de2, fill="white", font="bold")
        if joueur==1:                                                               #le joueur change à chaque tirage
            joueur=2
        else:
            joueur=1

        return de1, de2                                                             #retourne les valeurs des dés






    def clic(event):                                                                #selon l'action du joueur
        global pion_actif, joueur

        position_scroll=hbar.get()                                              #Retourne la positon de la scrollbar sous forme de tuple
        position_scroll=list(position_scroll)                                   #transforme en liste


        if 0-(position_scroll[0])*1300<event.x<=100-(position_scroll[0])*1300:  #pour centrer les pions sur les colonnes selon la position de la scrollbar
            event.x=20
        elif 100-(position_scroll[0])*1300<event.x<=200-(position_scroll[0])*1300:
            event.x=120
        elif 200-(position_scroll[0])*1300<event.x<=300-(position_scroll[0])*1300:
            event.x=220
        elif 300-(position_scroll[0])*1300<event.x<=400-(position_scroll[0])*1300:
            event.x=320
        elif 400-(position_scroll[0])*1300<event.x<=500-(position_scroll[0])*1300:
            event.x=420
        elif 500-(position_scroll[0])*1300<event.x<=600-(position_scroll[0])*1300:
            event.x=520
        elif 600-(position_scroll[0])*1300<event.x<=700-(position_scroll[0])*1300:
            event.x=620
        elif 700-(position_scroll[0])*1300<event.x<=800-(position_scroll[0])*1300:
            event.x=720
        elif 800-(position_scroll[0])*1300<event.x<=900-(position_scroll[0])*1300:
            event.x=820
        elif 900-(position_scroll[0])*1300<event.x<=1000-(position_scroll[0])*1300:
            event.x=920
        elif 1000-(position_scroll[0])*1300<event.x<=1100-(position_scroll[0])*1300:
            event.x=1020
        elif 1100-(position_scroll[0])*1300<event.x<=1200-(position_scroll[0])*1300:
            event.x=1120
        elif 1200-(position_scroll[0])*1300<event.x<=1300-(position_scroll[0])*1300:
            event.x=1220


        if 0<event.y<=75:                                                           #et sur les lignes
            event.y=10
        elif 75<event.y<=150:
            event.y=80
        elif 150<event.y<=225:
            event.y=150
        elif 225<event.y<=300:
            event.y=220
        elif 300<event.y<=375:
            event.y=290
        elif 375<event.y<=450:
            event.y=360
        elif 450<event.y<=525:
            event.y=450
        elif 525<event.y<=600:
            event.y=520
        elif 600<event.y<=675:
            event.y=590
        elif 675<event.y<=750:
            event.y=660
        elif 750<event.y<=825:
            event.y=730


        if pion_actif!=-1:                                                          #si pion séléctionné
            if not(350<event.y<450) or 600<event.x<700:                                #si on clique autre part que dans la zone interdite du milieu de plateau
                pions = can.find_withtag("pion")                                    #tous les id des pions dans la variable pions
                tags_p_a = can.gettags(pion_actif)                                  #tous les tags du pion actif dans variable tags_p_a


                test_case_occupee= False                                            #boléen pour savoir si la case demandée est déjà occupée
                test_bout_fleche= False                                             #boléen pour savoir si on est sur la case en bout de flèche dans laquelle la superposition est autorisée
                test_meme_couleur=True                                              #boléen pour savoir si le pion en bout de flèche est de la même couleur que le pion actif, auquel cas on ne bouge pas le pion


                pions_case_testee = can.find_enclosed(event.x-1, event.y-1, event.x + 61, event.y + 61)  #renvoit les ids des objets existant dans la case testée (-1 et +1 car ne prend pas en compte les objets qui sont pile dans le rectangle annoncé)

                test_case_occupee = len(pions_case_testee) > 0                      #si objets existent dans la case testée test_case_occupee devient True
                test_bout_fleche = event.y==290 or event.y==450                     #si on est en bout de flèche test_bout_fleche devient True
                if test_case_occupee:                                               #si case occupée
                    tags_pion = can.gettags(pions_case_testee[0])                   #tags du pion testé dans variable tags_pion
                    if "blanc" in tags_p_a and "rouge" in tags_pion or "rouge" in tags_p_a and "blanc" in tags_pion: #si pion dans la case testée de couleur différente de pion_actif
                        test_meme_couleur = False                                   #test meme_couleur devient False

                if test_case_occupee == False or (test_bout_fleche==True and test_meme_couleur==True): #si clique sur case vide ou sur case dans laquelle superposition est possible (= bout de flèche) et pion de même couleur
                    coord_p_a = can.coords(pion_actif)                              #coordonées du pion actif dans variable coord_p_a
                    can.coords(pion_actif, event.x,event.y,event.x+60,event.y+60)   #efface et redessine le pion actif sur la case demandée en fonction du clic
                    can.itemconfig(pion_actif, width=1, outline="black")            #déselectionne visuellement

                    UpdateTexte(coord_p_a[0], coord_p_a[1])                         #fonction UpdateTexte pour les cos du pion actif
                    UpdateTexte(event.x, event.y)                                   #fonction UpdateTexte pour les cos de la case d'arrivée du pion
                    pion_actif=-1                                                   #déselectionne
                if test_case_occupee == True:                                       #Si on clique sur un pion où la superposition est impossible
                    can.itemconfig(pion_actif, outline="black", width=1)            #déselectionne visuellement
                    pion_actif=-1                                                   #déselectionne

        else:                                                                       #aucun pion selectionné
            pion_actif= can.find_withtag("current")                                 #le pion sur lequel on clique entre dans la variable pion_actif (sous forme d'un tuple)

            if can.type(pion_actif) == "text":                                      #si on clique sur un pion ayant du texte
                pion_actif = Select_p_a(event.x, event.y)                           #retourne dans pion_actif l'id du pion sur lequel on a voulu cliqué

            tags = can.gettags(pion_actif)                                          #tous les tags du pion actif dans la variable tags

            if ("blanc" in tags and joueur == 1 or "rouge" in tags and joueur == 2) and "pion" in tags:  #si bon joueur sur bonne couleur
                can.itemconfig(pion_actif, width=4, outline="pink")                 #sélectionne en épaississant la bordure
            else:
                pion_actif = -1                                                     #sinon déséléctionne



    def Select_p_a (x, y):                                                          #pour les pions recouvert par du texte : permet de sélectionner le pion quand on clique sur le texte

        elements_case_testee = can.find_enclosed(x-1, y-1, x + 61, y + 61)          #trouver les élements dans la case sur laquelle on a cliqué

        elements_case_testee = list(elements_case_testee)                           #les mettre sous forme de liste
        elements_case_testee.reverse()                                              #inverser la liste pour avoir en premier le pion en foreground
        i=0
        while i < len(elements_case_testee):                                        #parcourir la liste
            if "pion" in can.gettags(elements_case_testee[i]):                      #si l'objet parcouru est un pion
                return elements_case_testee[i]                                      #on return son id
            i = i + 1



    def UpdateTexte(x, y):                                                          #Affiche les nombres si on superpose des pions
        elements_case_testee = can.find_enclosed(x-1, y-1, x + 61, y + 61)          #trouver les élements dans la case sur laquelle on a cliqué
        i = 0
        while i < len(elements_case_testee):                                        #Parcourir les éléments
            if "texte" in can.gettags(elements_case_testee[i]):                     #s'il y a du texte dans les éléments
                can.delete(elements_case_testee[i])                                 #on le supprime
            i = i + 1
        pions_case_testee = can.find_enclosed(x-1, y-1, x + 61, y + 61)             #trouve les éléments dans la case testée : il ne reste que des pions
        if len(pions_case_testee) > 1:                                              #s'il y a plus d'1 pion
            can.create_text(x + 30,y + 30,text = len(pions_case_testee), font="bold", fill="black" , tag=("texte")) #texte sur le pion pour indiquer le nombre de pions sur la case




    def isTheEnd(couleur):                                                          #pour message de fin
        ids = can.find_withtag(couleur)                                             #tous les ids de pions d'une même couleur dans variable ids
        if len(ids) == 0:                                                           #si aucun pion de la même couleur sur le plateau
            can.create_text(650,400,text = "Les "+couleur + "s ont gagné !", font="bold", fill="white") #fin de partie



    def clicFin2 (event):                                                           #pour sortir les pions blancs
        global pion_actif, joueur
        if pion_actif!=-1 and joueur==1:                                            #si pion séléctionné et joueur 1 clique dans zone grise
            coord_p_a = can.coords(pion_actif)
            can.delete(pion_actif)                                                  #on supp le pion actif
            isTheEnd("blanc")                                                       #on teste la fin de partie
            UpdateTexte(coord_p_a[0], coord_p_a[1])
        can.itemconfig(pion_actif, width=1, outline="black")
        pion_actif=-1                                                               #déséléctionne




    def clicFin1(event):                                                            #pour sortir les pions rouges
        global pion_actif, joueur
        if pion_actif!=-1 and joueur==2:
            coord_p_a = can.coords(pion_actif)
            can.delete(pion_actif)
            isTheEnd("rouge")
            UpdateTexte(coord_p_a[0], coord_p_a[1])
        can.itemconfig(pion_actif, width=1, outline="black")
        pion_actif=-1



    def regles():                                                                   #crée une nouvelle fenêtre avec le texte pour l'aide
        aide= Tk()                                                                  #nouvelle fenêtre
        txt_regles="Bienvenue sur notre Backgammon !! \nVous pouvez lire les règles complètes sur notre page web. Si vous les connaissez déjà cette aide sera suffisante ! \nLancez les dés pour initier la partie : le joueur blanc commence. Cliquez sur un pion pour le sélectionner puis cliquez sur une case vide pour le déplacer en fonction du tirage des dès. Il n’y a pas de limite dans le nombre de déplacement : vous pouvez donc tester plusieurs mouvements avant de passer la main à votre adversaire ! Relancez les dés pour changer de joueur. \nSi votre adversaire sort un de vos pions, vous devrez le placer sur la barre centrale en le sélectionnant puis en cliquant sur la barre dès que vous avez la main (après le tirage des dés). \nSi vous voulez placer plus de 5 pions sur une flèche vous pouvez superposer les pions sur la case en bout de flèche. Un numéro vous indique le nombre de pions sur cette case. \nEn fin de partie vous pourrez sortir vos pions en les sélectionnant et en cliquant sur la zone grise (à droite du plateau) correspondant à votre couleur. Cette action est irréversible : attention aux erreurs ! \nEnjoy !"
        texte= Text ( aide, height=20, width=100, bg="grey")                        #zone de texte de 20 lignes et 100 caractère pas ligne
        texte.insert(INSERT, txt_regles)                                            #insérer le texte dans la zone créée
        texte.pack()


                    #MAIN...

    root= Tk()                                                                      #Crée une fenêtre


    can= Canvas(root, width=1300, height=800,scrollregion=(0,0,1300,800))                                        #crée canevas général de 800x1300
    can.pack(side = LEFT)
    hbar=Scrollbar(can,orient=HORIZONTAL)
    hbar.pack(side=BOTTOM,fill=X)
    hbar.config(command=can.xview)


    can.config(width=300,height=300)
    can.config(xscrollcommand=hbar.set)
    can.pack(side=LEFT,expand=True,fill=BOTH)



    bouton= Button(root, text = "Lancer les dés", command = les_des)                #crée le bouton pour lancer les dés
    bouton.pack(pady=15, padx=5)

    bouton_aide=Button(root, text = "Aide",command= regles)                         #crée le bouton pour afficher l'aide
    bouton_aide.pack()

    d1= Canvas(root, width=50, height=50, bg="black")                               #crée les 2 canvas pour afficher les résultats des dés
    d1.pack(side= RIGHT)
    d2= Canvas(root, width=50, height=50, bg="black")
    d2.pack(side= RIGHT)

    img= PhotoImage(file="Bois.gif")                                                #insère une image de bois pour le fond dans une variable "img"; Bien mettre Bois.gif et le fichier py dans le même dossier !!
    can.create_image(0,0, image=img)                                                # fait apparaître img sur le canevas général en position 0, 0

    fin1= Canvas(root, width=80, height=80, bg="grey")                              #canvas pour mettre les pions qui sortent du plateau
    fin1.pack(pady=60, side=TOP)
    fin1.create_text(40,40,text="Sortie Rouges")                                    #Ajoute le texte Sortie Rouges sur la case grise

    fin2= Canvas(root, width=80, height=80, bg="grey")                              #canvas pour mettre les pions qui sortent du plateau
    fin2.pack(pady=60, side=BOTTOM)
    fin2.create_text(40,40,text="Sortie Blancs")                                    #Ajoute le texte Sortie Blancs sur la case grise


    plateau()                                                                       #met en place le plateau
    mise_en_place()                                                                 #met en place les premiers pions



    can.bind("<Button-1>", clic)                                                    #permet la séléction / le déplacement d'un pion
    fin1.bind("<Button-1>", clicFin1)                                               #permet de sortir un pion rouge en cliquant dans la zone grise
    fin2.bind("<Button-1>", clicFin2)                                               #permet de sortir un pion blanc en cliquant dans la zone grise

    root.mainloop()                                                                 #pour que la fenêtre reste ouverte















if jeu_choisi=="puissance" :
    def jeu():                                                                  #fonction qui crée le plateau de jeu et posent les bases du programme
        global joueur, stop, colonne1, colonne2, colonne3, colonne4, colonne5, colonne6, colonne7, plateau
        can.delete(ALL)                                                         #on supprime l'ancien jeu en cas de nouvelle partie
        for i in range(8):                                                      #on crée les ligne verticlales du plateau
            x = i*100+100
            can.create_line(x, 100, x, 700, width=3, fill='blue')
        for j in range(7):                                                      #on crée les ligne horizontales du plateau
            y = j*100+100
            can.create_line(100, y, 800, y, width=3, fill='blue')
        joueur = 1                                                              #le joueur jaune (1) commencera
        stop = False
        colonne1 = ["0","0","0","0","0","0"]                                    #chaque liste correspond à une colonne du jeu, plus on avance dans la liste plus on descend dans la colonne
        colonne2 = ["0","0","0","0","0","0"]
        colonne3 = ["0","0","0","0","0","0"]
        colonne4 = ["0","0","0","0","0","0"]
        colonne5 = ["0","0","0","0","0","0"]
        colonne6 = ["0","0","0","0","0","0"]
        colonne7 = ["0","0","0","0","0","0"]
        plateau = [colonne1, colonne2, colonne3, colonne4, colonne5, colonne6, colonne7]#ici, on a le plateau entier dont on se sert pour les victoires



    def pion_jaune(x,y):                                                        #fonction pour créer un pion jaune
        can.create_oval(x+5, y+5, x+95, y+95, width=2, fill='yellow', tag="pion")


    def pion_rouge(x,y):                                                        #fonction pour créer un pion rouge
        can.create_oval(x+5, y+5, x+95, y+95, width=2, fill='red', tag="pion")



    def action(event):                                                          #fonction principale qui définit ce qui se passe à chaque clic
        global joueur, stop, colonne1, colonne2, colonne3, colonne4, colonne5, colonne6, colonne7, plateau

        if 100 < event.y < 700:                                                     #si on est bien placé en ordonnée sur le plateau
            if 100 < event.x < 200 and colonne1[0]=="0":                            #si on est bien placé en abscisse sur dans la colonne 1 (en partant de la gauche) et que la colonne n'est pas remplie totalement
                a=5
                for i in range(5):
                    while colonne1[a]!="0":                                         #tant que la case de la colonne n'est pas vide,
                        a = a-1                                                     #on remonte d'une case
                if joueur == 1:                                                     #si c'est au tour du joueur jaune
                    pion_jaune(100,(a+1)*100)                                          #on place un pion jaune dans la case vide la plus en bas possible
                    colonne1[a]="J"                                                    #on note que cette case est maintenant remplie par un pion jaune dans cette colonne (et donc dans la liste de listes "plateau")
                    joueur = 2                                                         #on change de joueur car le joueur jaune a fini son tour
                else:                                                                  #si c'est au tour du joueur rouge
                    pion_rouge(100,(a+1)*100)                                          #on place un pion rouge dans la case vide la plus en bas possible
                    colonne1[a]="R"                                                    #on note que cette case est maintenant remplie par un pion rouge dans cette colonne (et donc dans la liste de listes "plateau")
                    joueur = 1                                                         #on change de joueur car le joueur rouge a fini son tour

            elif 200 < event.x < 300 and colonne2[0]=="0":                              #même fonctionnement pour les autres colonnes, ici la colonne 2
                a=5
                for i in range(5):
                    while colonne2[a]!="0":
                        a = a-1
                if joueur == 1:
                    pion_jaune(200,(a+1)*100)
                    colonne2[a]="J"
                    joueur = 2
                else:
                    pion_rouge(200,(a+1)*100)
                    colonne2[a]="R"
                    joueur = 1

            elif 300 < event.x < 400 and colonne3[0]=="0":                      #colonne 3
                a=5
                for i in range(5):
                    while colonne3[a]!="0":
                        a = a-1
                if joueur == 1:
                    pion_jaune(300,(a+1)*100)
                    colonne3[a]="J"
                    joueur = 2
                else:
                    pion_rouge(300,(a+1)*100)
                    colonne3[a]="R"
                    joueur = 1

            elif 400 < event.x < 500 and colonne4[0]=="0":                      #colonne 4
                a=5
                for i in range(5):
                    while colonne4[a]!="0":
                        a = a-1
                if joueur == 1:
                    pion_jaune(400,(a+1)*100)
                    colonne4[a]="J"
                    joueur = 2
                else:
                    pion_rouge(400,(a+1)*100)
                    colonne4[a]="R"
                    joueur = 1

            elif 500 < event.x < 600 and colonne5[0]=="0":                      #colonne 5
                a=5
                for i in range(5):
                    while colonne5[a]!="0":
                        a = a-1
                if joueur == 1:
                    pion_jaune(500,(a+1)*100)
                    colonne5[a]="J"
                    joueur = 2
                else:
                    pion_rouge(500,(a+1)*100)
                    colonne5[a]="R"
                    joueur = 1

            elif 600 < event.x < 700 and colonne6[0]=="0":                      #colonne 6
                a=5
                for i in range(5):
                    while colonne6[a]!="0":
                        a = a-1
                if joueur == 1:
                    pion_jaune(600,(a+1)*100)
                    colonne6[a]="J"
                    joueur = 2
                else:
                    pion_rouge(600,(a+1)*100)
                    colonne6[a]="R"
                    joueur = 1

            elif 700 < event.x < 800 and colonne7[0]=="0":                      #colonne 7
                a=5
                for i in range(5):
                    while colonne7[a]!="0":
                        a = a-1
                if joueur == 1:
                    pion_jaune(700,(a+1)*100)
                    colonne7[a]="J"
                    joueur = 2
                else:
                    pion_rouge(700,(a+1)*100)
                    colonne7[a]="R"
                    joueur = 1
        victoire()
        peut_jouer()



    def peut_jouer():                                                           #fonction qui affiche un message si toutes les colonnes sont remplies sans qu'il n'y ait eu de vainqueur (voir fonction victoire)
        global joueur, stop, colonne1, colonne2, colonne3, colonne4, colonne5, colonne6, colonne7, plateau
        if stop==False:
            if colonne1[0]!="0" and colonne2[0]!="0" and colonne3[0]!="0" and colonne4[0]!="0" and colonne5[0]!="0" and colonne6[0]!="0" and colonne7[0]!="0":
                stop = True
                can.create_text(450, 50, text="PARTIE TERMINEE ! EGALITE : PERSONNE NE GAGNE !")
            else:
                pass



    def victoire():                                                             #fonction qui affiche un message si un joueur a aligné correctement 4 pions
        global joueur, stop, colonne1, colonne2, colonne3, colonne4, colonne5, colonne6, colonne7, plateau
        for i in range(0,7):                                                    #test vertical
            for j in range(0,3):
                if plateau[i][j]==plateau[i][j+1]==plateau[i][j+2]==plateau[i][j+3]!="0":
                    if plateau[i][j]=="J":
                        can.create_text(450, 50, text="PARTIE TERMINEE ! VICTOIRE DES JAUNES !")#on affiche un message comme quoi les jaunes ont gagné
                        stop = True
                    else:
                        can.create_text(450, 50, text="PARTIE TERMINEE ! VICTOIRE DES ROUGES !")#on affiche un message comme quoi les rouges ont gagné
                        stop = True
        for j in range(0,6):                                                    #test horizontal
            for i in range(0,4):
                if plateau[i][j]==plateau[i+1][j]==plateau[i+2][j]==plateau[i+3][j]!="0":
                    if plateau[i][j]=="J":
                        can.create_text(450, 50, text="PARTIE TERMINEE ! VICTOIRE DES JAUNES !")#on affiche un message comme quoi les jaunes ont gagné
                        stop = True
                    else:
                        can.create_text(450, 50, text="PARTIE TERMINEE ! VICTOIRE DES ROUGES !")#on affiche un message comme quoi les rouges ont gagné
                        stop = True
        for i in range(0,4):                                                    #test diagonale bas à gauche vers haut à droite
            for j in range(5,2,-1):
                if plateau[i][j]==plateau[i+1][j-1]==plateau[i+2][j-2]==plateau[i+3][j-3]!="0":
                    if plateau[i][j]=="J":
                        can.create_text(450, 50, text="PARTIE TERMINEE ! VICTOIRE DES JAUNES !")#on affiche un message comme quoi les jaunes ont gagné
                        stop = True
                    else:
                        can.create_text(450, 50, text="PARTIE TERMINEE ! VICTOIRE DES ROUGES !")#on affiche un message comme quoi les rouges ont gagné
                        stop = True
        for i in range(0,4):                                                    #test diagonale haut à gauche vers bas à droite
            for j in range(0,3):
                if plateau[i][j]==plateau[i+1][j+1]==plateau[i+2][j+2]==plateau[i+3][j+3]!="0":
                    if plateau[i][j]=="J":
                        can.create_text(450, 50, text="PARTIE TERMINEE ! VICTOIRE DES JAUNES !")#on affiche un message comme quoi les jaunes ont gagné
                        stop = True
                    else:
                        can.create_text(450, 50, text="PARTIE TERMINEE ! VICTOIRE DES ROUGES !")#on affiche un message comme quoi les rouges ont gagné
                        stop = True



                             #MAIN

    root = Tk()

    can = Canvas(root, bg='white', height=800, width=900)                       #c'est le canevas où l'on met le plateau de jeu
    can.pack()

    can.bind("<Button-1>", action)                                              #le clic entraîne une action sur le plateau

    Button(root, text='Nouvelle partie', command=jeu).pack()                    #on peut recommencer une nouvelle partie en cliquabt sur ce bouton

    jeu()

    root.mainloop()                                                             #pour que la fenêtre reste ouverte










#PARTIE SIMON


if jeu_choisi=="simon":

    from tkinter import *
    from random import randint
    from tkinter.messagebox import * #on importe  tout  lese fonctions de tkinter.messagebox
    import pygame #On importe pygame pour les sons
    from pygame.locals import *
    import pickle #on importe pickle etc

    pygame.mixer.init()

    #On importe les sons
    Musique = pygame.mixer.Sound("sons/Musique2.wav")
    son1 = pygame.mixer.Sound("sons/PIANO1.wav")
    son2 = pygame.mixer.Sound("sons/PIANO2.wav")
    son3 = pygame.mixer.Sound("sons/PIANO3.wav")
    son4 = pygame.mixer.Sound("sons/PIANO4.wav")
    Perte = pygame.mixer.Sound("sons/BADOUM.wav")



    fenetre=Tk() #ON crée une instance
    fenetre.title("SIMON") #On nomme la fenêtre
    Musique.play(-1) #ON LANCE LA MUSIQUE
    Musical="True"

    #ON CREE LES LISTES et VARIABLES UTILES POUR LA SUITE

    caracteresacceptes=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    combinaison=[]   # on crée la liste qui servira à la construction de  la combinaison
    combi_joueur=[]  # on crée la liste qui servira pour la combi que le joueur fera
    pseudo_joueur=""
    COMMENCER="POSSIBLE"       #permet au joueur de commencer le jeu ou de recommencer quand il a perdu (cela évite qu'il lance plusieurs fois le jeu y jouer)
    tour=0              #Compte les tours
    ROLE="ORDI"          #Role permet de différencier quand c'est au joueur de jouer ou non (évite que le joueur fasse bugguer lors de l'affichage de la combinaison de lumière)


    #ON MET EN PLACE LE JEU 'GRAPHIQUEMENT':

    jeu= Canvas(fenetre,width=500, height = 500, bg= 'white') # On crée un canevas de 500x500 pixels avec un fond couleur blanc
    jeu.pack(side= LEFT) # On indique au canevas de se placer à gauche dans la fenêtre principale

    jeu.create_oval(50, 50,450,450, fill = 'black')     # On crée un cercle en fonction des coordonnées de son centre (au centre du canevas) c'est le l'ensemble de jouet
    a=jeu.create_oval(110,120,230,240, fill = '#F7FFA1') # POUR B 170 pixels à droite de A et C 150 pixels en dessous de A  #
    b=jeu.create_oval(280,120,400,240, fill = '#FF9999') # etc
    c=jeu.create_oval(110,270,230,390, fill = '#9CB4FF')
    d=jeu.create_oval(280,270,400,390, fill = '#9CFFB6')

    #Affichage des tours:
    Tour= Label(fenetre,text="Tour "+str(tour))
    Tour['fg']='black'
    Tour.pack(side=TOP)

    def affichage_tour(): #cette fonction permet de raffraichir l'affichage des tours
        Tour.configure(text="Tour "+ str(tour))


    #Fonction permettant de jouer:


    def Donne_pseudo():
        global pseudo_joueur
        while TRUE:
            pseudo_joueur=input("Quel est ton pseudo ? (sans caractère spécial ni accent: lettres de A-Z, a-z et nombres acceptés)")
            for i in pseudo_joueur:                      #ON VERIFIE SI LE PSEUDO EST CORRECT, si l'un des caractères donnés n'appartient pas à la liste caracteresacceptés une erreur s'affichera et le joueur doit redonner un pseudo
                  if i in caracteresacceptes:
                    continue
                  else:
                     showinfo("ERREUR","PSEUDO INCORRECT")
                     Donne_pseudo()
            break


    def COMMENCER_LE_JEU():
        global ROLE
        global COMMENCER                #Les changements sur COMMENCER et ROLE seront pris en compte à l'echelle global
        if COMMENCER=="POSSIBLE" :           #Le joueur peut commcer seulement s'il ne joue pas déjà et s'il ne s'amuse pas avec les touches
            COMMENCER="IMPOSSIBLE"
            ROLE="ORDI"
            la_combi_se_forme()


    def tout_seteint():                     #Une fonction qui change la couleur de tous les cercles pour les 'eteindre'
        jeu.itemconfig(a, fill="#F7FFA1")
        jeu.itemconfig(b, fill="#FF9999")
        jeu.itemconfig(c, fill="#9CB4FF")
        jeu.itemconfig(d, fill="#9CFFB6")

    def la_combi_se_forme():              #Fonction Qui forme la combinaison de lumières au fil du jeu en ajoutant une valeur et donc une lumière à chaque tour
        Musique.stop()

        affichage_tour()

        global combinaison               # on veut que les changements effectués sur const et Arret soient à l'echelle globale du programme
        global const
        global Arret
        global Musical
        Arret=False                     #Arret sert à savoir quand l'affichage de la combinaison de lumière s'arrete pour laisser le joueur saisir la sienne

        const=0                         #Cette variable servira à parcourir la liste Combinaison
        Musical="False"
        combinaison.append(randint(1,4)) #Combinaison = liste qui se remplie  (de random de 1 à 4)  const= variable qui permet de traverser Combinaison
        la_combi_saffiche()

    def la_combi_saffiche(): # foncition qui allume les couleurs selon la combinaison

            Communication.configure(text = "Suis attentivement ! :D")

            tout_seteint() # on s'assure que les lumières soient eteintes avant qu'une s'allume

            global const    # on veut que les changements effectués sur const et Arret soient à l'echelle globale du programme
            global Arret

            if const<len(combinaison)-1: #on verifie que la const est inférieur à la longueur de la liste

                if combinaison[const]==combinaison[const+1]: # on cherche à savoir si l'element qui suit
                    fenetre.after(500,tout_seteint)

            if combinaison[const]==1:

                 jeu.itemconfig(a, fill="yellow") # si le numéro est 1 alors c'est le jaune qui s'allume
                 son1.play()


            elif combinaison[const]==2:
                jeu.itemconfig(b, fill="red") # pour le 2 c'est le rouge
                son2.play()

            elif combinaison[const]==3:
                jeu.itemconfig(c, fill="blue") #pour le 3 c'est le bleu
                son3.play()

            else:
                jeu.itemconfig(d, fill="green") #sinon c'est le vert
                son4.play()

            if const<len(combinaison)-1: # on s'interesse à la deuxieme valeur de la liste associé à une des couleurs qui s'allume
                const+=1

            else:
                fin_affichage()
                Arret=TRUE         #Lorsque la liste est parcourue en entier Arret = False

            if Arret==False:                #Permet d'arreter la boucle qui affiche les couleurs
                fenetre.after(1000,la_combi_saffiche)

    def fin_affichage():
        fenetre.after(1000,le_joueur_forme_sa_combi)


    def le_joueur_forme_sa_combi(): # la partie ou le jour va former sa combi en cliquant
            tout_seteint()
            global combi_joueur
            combi_joueur=[] #on réinitialise la liste qui servira à la combinaison que le joueur fera
            #on ne réinitialise plus la liste_comparaison ici car elle est déjà réinitialisée au debut de verification
            global ROLE
            ROLE="JOUEUR"
            Communication.configure(text = "A TOI DE JOUER ! ;)")


    def clic(event): #les clics du joueurs sont associés à une zone qui changera de couleur après du clic


        if ROLE =="JOUEUR" or ROLE =="FUN":

             if 110<event.x<230 and 120<event.y<240:         #intervalles d'abscisses et d'ordonnées correspondant à la zone associée  au bouton jaune

                  LEJOUEURVAVITE()                          #si le joueur va vite on veut pas que toutes les lumieres s'allument en même temps et que les sons soient joués en meme temps
                  jeu.itemconfig(a, fill="yellow")        #le bouton jaune s'allume en cas de clic dans la zone

                  if len(combi_joueur)<len(combinaison):    #Evite le out of range si le joueur clic trop par erreur
                            combi_joueur.append(1)                  #la valeur 1 (associée à la couleur jaune dans notre jeu) s'ajoute à la suite combi_joueur

                  son1.play()
                  fenetre.after(1000,verification)

             if 280<event.x<400 and 120<event.y<240:   #même principe pour le bouton rouge
                  LEJOUEURVAVITE()
                  jeu.itemconfig(b, fill="red")
                  if len(combi_joueur)<len(combinaison):
                      combi_joueur.append(2)

                  son2.play()
                  fenetre.after(1000,verification)

             if 120<event.x<230 and 270<event.y<390:     #même principe pour le bouton bleu
                  LEJOUEURVAVITE()
                  jeu.itemconfig(c, fill="blue")

                  if len(combi_joueur)<len(combinaison):
                      combi_joueur.append(3)


                  son3.play()
                  fenetre.after(1000,verification)

             if 280<event.x<400 and 270<event.y<390:     #même principe pour le bouton vert
                  LEJOUEURVAVITE()
                  jeu.itemconfig(d, fill="green")

                  if len(combi_joueur)<len(combinaison):
                     combi_joueur.append(4)


                  son4.play()
                  fenetre.after(1000,verification)

    def LEJOUEURVAVITE():
        tout_seteint()
        son1.stop()
        son2.stop()
        son3.stop()
        son4.stop()

    def verification():                         #verification au fur et à mesure que le joueur fait sa combi

       liste_comparaison=[]                    #liste qui va être utile pour vérifier ce que le jour vient de saisir
       global ROLE
       global tour
       global combinaison
       global COMMENCER
       if ROLE=="JOUEUR":
        for i in range(len(combi_joueur)):          #on utilise la liste_comparaison pour copier le debut de "combinaison" afin de le comparer à combi_joueur actuelle
                liste_comparaison.append(combinaison[i])

        if liste_comparaison==combi_joueur:
            Communication.configure(text = "Bien !")
        else :
             Presentation_scores() # on reintialise l'affichage des scores
             ROLE="ORDI"
             combinaison = []       #la combinaison est rénitialisée
             Perte.play()           #Son de défaite
             fenetre.after(5000,MUSIQUERECOMMENCE)  # la musique repart au bout de 5 secondes
             COMMENCER="POSSIBLE"

             if tour<5:
                Communication.configure(text = "Perdu ! Ton score est de "+str(tour)+". Ce n'est pas très glorieux.")
             elif 5<tour<10:
                Communication.configure(text = "Perdu ! Ton score est de "+str(tour)+". Dommage.")
             elif 10<tour<15:
                Communication.configure(text = "Perdu ! Ton score est de "+str(tour)+". Pas mal ! ")
             elif 15<tour<20:
                Communication.configure(text = "Perdu ! Ton score est de "+str(tour)+" T'es super bon.")
             else:
                Communication.configure(text = "Perdu ! Ton score est de "+str(tour)+" Incroyable !!!")

             tour=0      #on réinitialise les tours

        if combi_joueur==combinaison:           #On cherche à savoir si le joueur a resaisi la combinaison en entier
            tour+=1                             #le tour augmente de 1
            ROLE="ORDI"
            fenetre.after(1000,la_combi_se_forme)                 #on repart pour une combinaison avec une valeur de plus




    def Presentation_scores():
        pseudos=[]
        records=[]

        if pseudo_joueur=="":                            #si le joueur n'a pas donné de pseudo

         with open('BestScoresSimon.txt', 'rb') as fichier: #on récupère le fichier.txt des scores
            LEFICHIER=pickle.Unpickler(fichier)
            scores=LEFICHIER.load()                            #on copie le dictionnaire qui se trouve sur le fichier pour l'assimiler à score

         for cle,valeur in scores.items():           #on crée 2 listes à partir du dictionnaire l'une contenant les pseudos et l'autre avec les records
             pseudos.append(cle)
             records.append(valeur)

         for j in range(len(pseudos)-1,0,-1):                      # On compare les deux liste: tri bulle on trie les scores pour les mettre dans l'ordre et on change en même temps l'ordre des pseudos dans l'autre liste
                for i in range(0,j):
                     if int(records[i+1]) < int(records[i]):
                        pseudos[i],pseudos[i+1] = pseudos[i+1],pseudos[i]
                        records[i],records[i+1] = records[i+1],records[i]
         pseudos.reverse()                                          #On fait un reverse pour que les meilleurs scores soient au début de la liste et non à la fin
         records.reverse()


         Pseudo1=pseudos[0]
         Pseudo2=pseudos[1]
         Pseudo3=pseudos[2]
         Pseudo4=pseudos[3]
         Pseudo5=pseudos[4]

         SCORE1=str(records[0])
         SCORE2=str(records[1])
         SCORE3=str(records[2])
         SCORE4=str(records[3])
         SCORE5=str(records[4])


         SCORES.configure(text = "High Scores: \n \n "+Pseudo1+": "+SCORE1+"\n"+Pseudo2+": "+SCORE2+"\n"+Pseudo3+": "+SCORE3+"\n"+Pseudo4+": "+SCORE4+"\n"+Pseudo5+": "+SCORE5,borderwidth=20)
        else:

             with open('BestScoresSimon.txt', 'rb') as fichier: #on récupère le fichier.txt des scores
                 LEFICHIER=pickle.Unpickler(fichier)
                 scores=LEFICHIER.load()                              #on copie le dictionnaire qui se trouve sur le fichier pour l'assimiler à score

             for cle,valeur in scores.items():           #on crée 2 listes à partir du dictionnaire l'une contenant les pseudos et l'autre avec les records
                 pseudos.append(cle)
                 records.append(valeur)

             a=pseudo_joueur.capitalize()
             if  a in pseudos:              #on cherche à savoir si le pseudo est déjà inscrit  dans les meilleurs scores si c'est le cas il n'est pris en compte que si le joueur a fait mieux que la dernière fois
                for i in range(len( pseudos)):

                    if a== pseudos[i]:
                        if int(records[i])<tour:
                            records[i]=str(tour)

             else:                                      #autrement on l'ajoute
                 pseudos.append(pseudo_joueur.capitalize())
                 records.append(tour)

             for j in range(len(pseudos)-1,0,-1):                      # On compare les deux liste: tri bulle on trie les scores pour les mettres dans l'ordre et on change en même temps l'ordre des pseudos dans l'autre liste
                for i in range(0,j):
                     if int(records[i+1]) < int(records[i]):
                        pseudos[i],pseudos[i+1] = pseudos[i+1],pseudos[i]
                        records[i],records[i+1] = records[i+1],records[i]
             pseudos.reverse()                                          #On fait un reverse pour que les meilleurs scores soient au début de la liste et non à la fin
             records.reverse()



             scores=   {                                #On recrée un dictionnaire avec les differents pseudos et scores à partir des deux listes
             pseudos[0]:str(records[0]),
             pseudos[1]:str(records[1]),
             pseudos[2]:str(records[2]),
             pseudos[3]:str(records[3]),
             pseudos[4]:str(records[4]),
             }

             Pseudo1=pseudos[0]
             Pseudo2=pseudos[1]
             Pseudo3=pseudos[2]
             Pseudo4=pseudos[3]
             Pseudo5=pseudos[4]

             SCORE1=str(records[0])
             SCORE2=str(records[1])
             SCORE3=str(records[2])
             SCORE4=str(records[3])
             SCORE5=str(records[4])

             with open('BestScoresSimon.txt', 'wb') as fichier: # on engistre les nouveaux scores dans le fichier
                score=pickle.Pickler(fichier)
                score.dump(scores)

             #On modifie le label pour afficher les pseudos et les scores

             SCORES.configure(text = "High Scores: \n \n "+Pseudo1+": "+SCORE1+"\n"+Pseudo2+": "+SCORE2+"\n"+Pseudo3+": "+SCORE3+"\n"+Pseudo4+": "+SCORE4+"\n"+Pseudo5+": "+SCORE5,borderwidth=20)

    def MUSIQUERECOMMENCE():           #arreter la musique si elle est arretée
        global Musical
        if Musical=="False":
            Musique.play(-1)
            Musical="True"

    def MUSIQUESTOP():              #arreter la musique si elle est en cours
        global Musical
        if Musical=="True":
            Musique.stop()
            Musical="False"

    def regles():                                   #crée une nouvelle fenetre pour afficher l'aide
        aide= Toplevel()
        CAN_AIDE= Canvas(aide,width=1000,height=800)
        CAN_AIDE.pack()
        img= PhotoImage(file="SIMONAIDE.gif")
        item=CAN_AIDE.create_image(500,400, image=img)
        aide.mainloop()

    def quitter():
        Musique.stop()
        if askyesno('NE ME QUITTE PAS', 'Êtes-vous sûr de vouloir faire ça?'):      #demande au joueur s'il est sûr de quitter
            fenetre.destroy()
        else:
            showinfo('MERCI', 'Cool!')


    #FUN#
    #Bouton qui sert uniquement à pouvoir appuyez sur les sons hors jeu,pas utile pour jouer
    def je_suis_un_musicien():
        global ROLE
        if COMMENCER=="POSSIBLE" and ROLE=="ORDI": #On peut s'amuser avec les touches seulement lorsqu'on ne joue pas
            ROLE="FUN"
            Musique.stop()
    #FUN


    #Lié le clic
    jeu.bind("<Button-1>", clic)
    jeu.pack




    #Label pour communiquer avec le joeur
    Communication= Label(fenetre)
    Communication.pack(side=TOP)
    Communication.configure(text = "Donne ton pseudo avant de commencer !")


    #bouton en haut à droite

    Button(fenetre, text='Donne ton pseudo',width=30,command=Donne_pseudo).pack() #Bouton pour que l'ordi demande le pseudo au joueur
    Button(fenetre, text='Commencez le jeu !',width=30, command = COMMENCER_LE_JEU).pack() #Bouton pour commencer le jeu
    Button(fenetre, text='Jouer avec les touches :)',width=30,command = je_suis_un_musicien).pack() #Bouton pour commencerà s'amuser avec les touches sans lancer le jeu

     #Label qui présente les scores les plus hauts enregistrés

    SCORES= Label(fenetre)
    SCORES.pack()
    Presentation_scores()

    #les bouton qui se trouvent en bas à droite du jeu

    Button(fenetre,text='Quitter', command=quitter).pack(side=BOTTOM)                      #Bouton pour quitter le jeu qui par ailleurs eteind aussi la musique
    Button(fenetre,text='Arrêter la Musique',command =MUSIQUESTOP).pack(side=BOTTOM)    #Bouton pour mettre la musique en pause
    Button(fenetre,text='Relancer la musique',command =MUSIQUERECOMMENCE).pack(side=BOTTOM) #Bouton pour remettre la musique en marche
    bouton_aide=Button(fenetre, text = "Aide",command= regles).pack(side=BOTTOM)   #Bouton pour voir l'aide (règles du jeu)
    fenetre.mainloop()





