from Tikrinimas import tikrinimas

def do_or_die(table):
    index = [i for i, x in enumerate(table) if x == " "]
    for laukelis in index:
        table[laukelis] = "X"
        if tikrinimas(table):
            table[laukelis] = " "
            return laukelis
        else: table[laukelis] = " "
    for laukelis in index:
        table[laukelis] = "O"
        if tikrinimas(table):
            table[laukelis] = " "
            return laukelis
        else:
            table[laukelis] = " "
