def tikrinimas(listas):
    matrica = [["","",""],["","",""],["","",""]]
    address = 0
    for row in range(len(matrica)):
        for column in range(len(matrica[0])):
            matrica[row][column] = listas[address]
            address += 1

    # suformuojama pirma istrizaine
    istrizaine1 = [matrica[x][y] for y in range(len(matrica[0])) for x in range(len(matrica)) if
                     (x == 0 and y == 0) or (x == 1 and y == 1) or (x == 2 and y == 2)]
    # suformuojama antra istrizaine
    istrizaine2 = [matrica[y][x] for y in range(len(matrica[0])) for x in range(len(matrica)) if
                     (x == 0 and y == 2) or (x == 1 and y == 1) or (x == 2 and y == 0)]
    # ar pirma istrizaine uzpildyta tuo paciu simboliu
    if sum(type(x) is str for x in istrizaine1 if x == istrizaine1[0] and istrizaine1[0] != " ") == len(matrica):
        # jei yra, grazinu simboli kuris turi uzpildes istrizaine
        return istrizaine1[0]
        # ar antroje istrizaineje yra X arba O
    if sum(type(x) is str for x in istrizaine2 if x == istrizaine2[0] and istrizaine2[0] != " ") == len(matrica):
        # jei yra, grazinu simboli kuris turi uzpildes istrizaine
        return istrizaine2[0]
    #einama per eilutes elementus
    for row in range(len(matrica)):
        #suformuoju tuscia stulpeli
        stulpelis = []
        #einama per matricos stulpelius
        for column in matrica:
            #pildomas stulpelis
            stulpelis.append(column[row])
        #ar eiluteje yra uzpildyta tuo paciu simboliu ir simbolis nėra tuščias
        if sum(type(x) is str for x in matrica[row] if x == matrica[row][0] and matrica[row][0] != " " ) == len(matrica):
            #jei yra, grazinu simboli kuris turi uzpildes eilute
            return matrica[row][0]
        #ar stulpelis uzpildytas tuo paciu simboliu ir simbolis nėra tuščias
        if sum(type(x) is str for x in stulpelis if x == stulpelis[0] and stulpelis[0] != " ") == len(matrica):
            # jei yra, grazinu simboli kuris turi uzpildes stulpeli
            return stulpelis[0]
