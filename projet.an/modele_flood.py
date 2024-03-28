import random
class Modele : 
    def __init__ (self,lig = 10 ,col = 10 ,couleur=6) :
        self.__lig = lig
        self.__col = col 
        self.__couleur = couleur
        self.__score = 0
        self.__mat = list()
        
        for i in range(self.__lig) :
            self.__mat.append([])
            for j in range(self.__col) :
                random_val = random.randint(0,self.__couleur-1)
                self.__mat[i].append(random_val)
    def nb_lig(self):
        return self.__lig
    def nb_col(self):
        return self.__col
    def nb_coleur(self) :
        return self.__couleur
    def retour_couleur(self,l,c):
        return self.__mat[l][c]
    def nb_score(self):
        return self.__score
    def choisit_couleur(self,l,c) :
        if self.__mat[0][0] != self.__mat[l][c]:
            self.__mat[0][0] = self.__mat[l][c]
            self.__score +=1
            
    def reinit(self):
        self.__score = 0
        random_val = random.randint(0,self.__couleur-1)
        self.__mat = []
        for i in range(self.__lig):
            self.__mat.append([])
            for j in range(self.__col):
                self.__mat[i].append(random_val)

    def affi_trait(self):
        " affi trait pour appliquer a str"
        res = ""
        for i in range(self.__col) :
            res += "-----"
        res += "\n"
        return res
    def affi_lig(self,lig) :
        "affi lig mais prend les indice de col pour affi les element sur lig"
        res = ""
        for i in range(self.__col) :
            val = str(self.__mat[lig][i])
            val = random.randint(0,self.__couleur-1)
            res += " |"
            if self.__mat[lig][i] < 10 :
                res += " " + str(val)
            else :
                res += str(val)
        res += "| \n"
        return res 
    def __str__(self) :
        "combine between trait and affi lig"
        res = " "
        for i in range(self.__lig):
            res += self.affi_lig(i)
            res += self.affi_trait()
        return res
    
#import modele_flood
#mod = Modele()
#print(mod.__str__())
#mod.nb_lig()
#mod.nb_col
#print(mod)

        

            
        