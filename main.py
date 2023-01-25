#tik-tak-toe
soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
gutel = [0,1,2,3,4,5,6,7,8,9]
zlist = [" "," "," "," "," "," "," "," "," "," "]
winl = [[],[]]

# Function to print Tic Tac Toe
def print_tic_tac_toe(wert):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(wert[1],wert[2],wert[3]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(wert[4],wert[5],wert[6]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(wert[7],wert[8],wert[9]))
    print("\t     |     |")
    print("\n")
print_tic_tac_toe(gutel)

def eingabe(x,b):
    if x > 9 or x < 1:
        print("Falsche Eingabe")
        exit()
    elif gutel[x] == "x" or gutel[x] == "o":
        print("Doppelt")
        exit()
    else:
        gutel[x] = str(b)

while True:
    for x in soln:
        if winl[0] == x:
            print("2 gewinnt")
            exit()
        if winl[1] == x:
            print("1 gewinnt")
            exit()
        if len(winl[0]) > 4:
            print("unentschieden")
            exit()
        if len(winl[1]) > 4:
            print("unentschieden")
            exit()

    if len(winl[0]) < len(winl[1]):
        t = "o"
        p = "2"
        z = 0
    else:
        t = "x"
        p = "1"
        z = 1

    print("Spieler {}".format(p))
    y = int(input("Wahl: "))
    winl[z].append(y)
    eingabe(y, t)
    print_tic_tac_toe(gutel)


