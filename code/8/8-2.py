def digit_art_horizontal(n):
    for i in range(n):
        for j in range(n):
            print(j+1, end=' ')
        print()
        
digit_art_horizontal(7)