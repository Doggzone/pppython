def digit_art_horizontal_alternate(n):
    for i in range(n):
        for j in range(n):
            if i % 2 == 0:
                print(j+1, end=' ')
            else:
                print(n-j, end=' ')
        print()