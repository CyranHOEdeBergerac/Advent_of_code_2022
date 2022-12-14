#TROUVER LE SOUCIS D'INDICE DANS LES PERMUTATIONS DU TABLEAU
def trouver_marqueur_n (s : str, n : int):
    """Retourne la position après le marqueur de n caractères consécutifs tous différents dans la chaîne s"""
    pos_s = 0
    pos_m = 0
    marqueur = []
    for c in s :
        
        if c not in marqueur:
            marqueur.append(c)
            pos_m+=1
            if pos_m == n:
                print(marqueur)
                return pos_s+1
        else:
            i = marqueur.index(c)       #Il n'y aura toujours qu'une valeur possible car on n'a jamais ajouté deux fois au tableau de marquage la même valeur sur [0;pos_m[
            print("i = " + str(i))
            marqueur = marqueur[i+1:]
            marqueur.append(c)
            pos_m = marqueur.index(c) +1
        pos_s+=1
        
    return -1
    



def main():
    
    filename = input("Filename ?")
    with open(filename, 'r') as f:
        fichier = f.read()
        print(fichier)
        n = input("Quelle taille de marqueur ?")

        print(trouver_marqueur_n(fichier,int(n)))


 
if __name__ == '__main__':
	main()



        

