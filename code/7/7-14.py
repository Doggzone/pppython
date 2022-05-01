def tower_of_hanoi(n, source, destin, temp):
    if n > 1:
        tower_of_hanoi(n-1, source, temp, destin)
        print("Move a disk from", source, "to", destin)
        tower_of_hanoi(n-1, temp, destin, source)
    else:
        print("Move a disk from", source, "to", destin)