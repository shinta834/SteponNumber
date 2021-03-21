def steponNumber (x):
    # jumlah baris (sumbu y)
    row = 6
    # jumlah kolom (sumbu x)
    col = x + 1
    # fungsi for loop untuk membentuk pola sumbu x dan y
    for i in range (x+1):
        for j in range (col+1):
            if i+j == x or i+j == x+2:
                print (j,end='')
            else:
                print (end=' ')
        print()
    # mencari nilai berdasarkan sumbu yang ditentukan dari list

# input
listAwal = [[4,2],[6,6],[3,4]]

steponNumber (listAwal)