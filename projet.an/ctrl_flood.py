
from modele_flood import Modele
from vue_flood import Vue

class FloodControleur :
    def __init__(self) :
        self.__modele = Modele() 
        self.__vue = Vue(self.__modele,self)

    def creer_controleur_buton(self) :
        pass
    def controleur_btn(self,i,j) :
        self.__modele.choisit_couleur(i,j)
        self.__vue.redessin()
    
    def nouvelle_partie(self) :
        self.__modele.reinit()
        self.__vue.redessin() 

    def demarrer(self) :
        self.__vue.demarrer()





    
