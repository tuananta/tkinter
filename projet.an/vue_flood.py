import random
import tkinter
class Vue :
    def __init__(self,modele, controleur):
        from modele_flood import Modele
        from ctrl_flood import FloodControleur
        self.__modele = modele
        self.__ctrl = controleur
        self.fenetre = tkinter.Tk()
        self.fenetre.title("Flood game")
        self.couleurs = self.cre_couleur()
        self.les_btns = []

    def cre_mat(self):
        # creer les butons pour fenetre
        # premier place
        self.pre_frame = tkinter.Frame(self.fenetre)
        self.pre_frame.pack(side="left")
        # deuxiem place
        self.deu_frame = tkinter.Frame(self.fenetre)
        self.deu_frame.pack(side="right")
        #buton: 2, label: 1
        btn_gauche= tkinter.Button(self.deu_frame, text="Nouveau") 
        btn_gauche.pack(side="left")
        btn_droit= tkinter.Button(self.deu_frame, command=self.fenetre.destroy, text="Quitter") #
        btn_droit.pack(side="right" )
        self.mess_score = tkinter.Label(self.deu_frame, text= self.__modele.nb_score() )
        self.mess_score.pack(side="top")
        # matrice du jeu
        for i in range(self.__modele.nb_lig()) :
            self.les_btns.append([])
            for j in range(self.__modele.nb_col()) :
                self.btn_couleur = tkinter.Button(self.pre_frame,command= self.__ctrl.controleur_btn(i, j), bg=self.matrice_couleur() )  
                self.btn_couleur.grid(row= i, column=j)
                #self.btn_couleur.bind("<Button-1>",command=lambda i=i, j=j: self.__ctrl.controleur_btn(i, j))
            self.les_btns[i].append(self.btn_couleur)

    # choix couleur par hasard pour matrice
    def matrice_couleur(self) :
        res = random.choice(self.couleurs)
        return res 
    # change couleur de matrice a position 0,0
    def change_couleur(self):
        for i in self.les_btns:
            for j in self.les_btns[i] :
                val  = self.les_btns[i][j]
                if i< len(self.les_btns) and j < len(self.les_btns[i]) :
                        self.les_btns[0][0].config(bg = val )
    
    # malenger pour obtion un list de couleur pour matrice
    def cre_couleur(self):
        res = []
        for i in range(self.__modele.nb_coleur()):
            rouge = random.randint(0, 255)
            vert = random.randint(0, 255)
            bleu = random.randint(0, 255)
            c = "#{:02x}{:02x}{:02x}".format(rouge, vert, bleu) 
            res.append(c)
        return res
               
    def redessin(self):
        self.mess_score.config()
        for i in range(self.__modele.nb_lig()) :
            for j in range(self.__modele.nb_col()) :
                self.les_btns[i][j].config(bg=self.matrice_couleur())   

    def demarrer(self) :
        self.change_couleur()
        self.matrice_couleur()
        self.cre_mat()
        self.fenetre.mainloop()



                





