def porownanie(lst1, lst2):
    if len(lst1)==len(lst2): #stały czas
        m1=max(lst1) # 0(n)
        m2=min(lst2) # 0(n)
        if m1>m2: #stały czas
            return "Istnieje taki element."
        else:
            "Nie istnieje taki element."
    else:
        return "Listy nie są tej samej długości!"

print(porownanie([2,5,3,7],[3,7,4,8]))
#Stały czas równy 2n gdzie n to długość list.

def porownanie1(lst1, lst2):
    if len(lst1) == len(lst2):
        n=len(lst1) #stały czas
        for i in range (n): # 0(n)
            for j in range (n): #0(n)
                if lst1[i]>lst[j]:
                    return "Istnieje taki element."
            j=+1
        i=+1
        return "Nie istnieje taki element."
    else:
        return "Listy nie są tej samej długości!"

print(porownanie([2,5,3,7],[3,7,4,8]))
#Optymistyczny: w pierwszym porównaniu się uda czyli 3 operacje -> 0(1)
#Pesymistyczny: w ostatnim, czyli 0(n^2)
