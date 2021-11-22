# Code Boyer-Moore-Horspool

def tableau_sauts(motif):
    return {motif[i]: len(motif)-1-i for i in range(len(motif)-2,-1,-1)}
        



def boyer_moore_horspool(texte, motif,tDs):
    size = len(texte)
    taille = len(motif)
    positions = []
    if (taille<=size):
        i=0
        trouve=False
        while (i<=size-taille):
            for j in range (taille-1,-1,-1):
                trouve=True
                if(texte[i+j]!=motif[j]):
                    if(texte[i+j] in tDs and tDs[texte[i+j]]<=j):
                        i+=tDs[texte[i+j]]
                    else:
                        i+=j+1
                    trouve=False
                    break
            if (trouve):
                positions.append(i)
                i += 1
                trouve=False
    return positions[0]

if __name__ == "__main__" :
    texte = "ayoubbilaladam"
    motif = "bilal"
    tDs=tableau_sauts(motif)
    azetr = boyer_moore_horspool(texte, motif, tDs)
    print(azetr)
    