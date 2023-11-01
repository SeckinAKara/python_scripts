from random import randint

in_bounds = [(-2, 3), (-1, 3),         (1, 3), (2, 3),
             (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2),
             (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1),
                      (-1, 0), (0, 0), (1, 0),
                      (-1, -1),(0, -1),(1, -1),
                               (0, -2)
             ]

moveset = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

def move(letter, z, o, s):
    direction = moveset[letter]
    z_new = (z[0]+direction[0], z[1]+direction[1])
    if z_new not in in_bounds:
        return ("cannot", z, o, s)
    o_new = (o[0]-direction[0], o[1]-direction[1])
    if o_new not in in_bounds:
        o_new = o
    s_new = (s[0]+direction[0], s[1]+direction[1])
    if s_new not in in_bounds:
        s_new = s
    if o_new == s_new:
        o_new = o
        s_new = s
    elif o_new == s and s == o_new:
        o_new = o
        s_new = s
    if o_new == z_new or s_new == z_new:
        return("killed", z, o, s)
    elif (o_new == (-1, 2) and s_new == (1, 2)) or (s_new == (-1, 2) and o_new == (1, 2)):
        movements.append(letter)
        return("complete", z_new, o_new, s_new)
    else:
        movements.append(letter)
        return("moved", z_new, o_new, s_new)

complete = False
while not complete:
    movements=[]
    link = (0, 0)
    opposite = (0, 2)
    same = (0, -2)
    while True:
        j = ["L", "R", "U", "D"][randint(0, 3)]
        (outcome, link, opposite, same) = move(j, link, opposite, same)
        print(movements)
        if outcome == "complete":
            print("WINNING MOVESET: " , movements)
            complete = True
            break
        elif len(movements) > 25:
            break
