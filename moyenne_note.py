import statistics # calcule la moyenne

continuer= "oui"
while continuer =="oui":

    n = int(input("Combien de notes voulez-vous enregistrer ? :")) 
    note = [] 
    for i in range(n): 
        x = float(input(f"Entrez la note {i+1} :")) 
        note.append(x) 
 

    moyenne = statistics.mean(note) 
    print(f"les notes {note} font une moyenne de {moyenne}")

    if moyenne < float(10.0) :
        print("C'est insuffisant !")
    elif moyenne <= float(15.0): 
        print("C'est correct , continu tes efforts ")
    else:
        print("c'est tres bien , continu comme sa ")
    
    continuer=input("Voulez vous continuer ? (oui/non) :")
    if continuer =="non":
        break 
    
