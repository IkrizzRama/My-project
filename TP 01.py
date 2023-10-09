#Muhammad Rizky Ramadhani - 2306240143
#Mengimport library yang akan digunakan
import turtle
from tkinter import messagebox
turtle.title('Super Mario Tower') #Judul dari turtle yang akan dibuat
turtle.Screen().bgcolor('white')
#menginput data yang diperlukan
beda_tower = 0
jarak_tower = 0
valid = False #
while(not valid):
    jumlah_tower = int(turtle.numinput('input', 'Jumlah tower yang akan dibuat(Minimal 1): '))  #Menginput Jumlah Tower yang akan dibuat
    if int(jumlah_tower) < 1:
        messagebox.showinfo("WARNING", "Jumlah tower harus minimal 1!")
    else:
        valid = True
        jumlah_tower = int(jumlah_tower)
    jumlah_tower = int(jumlah_tower)    
if jumlah_tower > 1: #If conditional bila user hanya ingin membuat 1 tower
    

    valid = False
    while(not valid):
        jarak_tower = int(turtle.numinput('input', 'Jarak antar tower yang akan dibuat(Minimal 2 dan maksimal 5): ')) #Menginput jarak antar tower
        if int(jarak_tower) < 2:
            messagebox.showinfo("WARNING", "Minimal jarak tower adalah 2!")
        elif int(jarak_tower) > 5:
            messagebox.showinfo("WARNING", "Maksimal jarak tower adalah 5!")
        else:
            valid = True
            jarak_tower = int(jarak_tower)

    valid = False
    while(not valid):
        beda_tower = int(turtle.numinput('input', 'Perbedaan jumlah lapisan setiap tower(Minimal 2 dan maksimal 5): ')) #Menginput beda layer pada setiap tower
        if int(beda_tower) < 2:
            messagebox.showinfo("WARNING", "Minimal beda jumlah lapisan adalah 2!")
        elif int(beda_tower) > 5:
            messagebox.showinfo("WARNING", "Maksimal beda jumlah lapisan adalah 5!")
        else:
            valid = True
            beda_tower = int(beda_tower)

valid = False
while(not valid):
    panjang_bata = int(turtle.numinput('input', 'Masukkan panjang satu buah batu bata(Maksimal 35): ')) #Menginput panjang bata yang akan dibuat
    if int(panjang_bata) > 35:
        messagebox.showinfo("WARNING", "Panjang satu buah batu bata maksimal 35!")
    else:
        valid = True
        panjang_bata = int(panjang_bata)

valid = False
while(not valid):
    lebar_bata = int(turtle.numinput('input', 'Masukkan lebar satu buah batu bata(Maksimal 25): ')) #Menginput lebar bata yang akan dibuat
    if int(lebar_bata) > 25:
        messagebox.showinfo("WARNING", "Lebar satu buah batu bata maksimal 25!")
    else:
        valid = True
        lebar_bata = int(lebar_bata)

valid = False
while(not valid):
    layer_1 = int(turtle.numinput('input', 'Masukkan jumlah layer pertama(Maksimal25): ')) #Menginput jumlah layer pertama dari tower
    if int(layer_1)>25:
        messagebox.showinfo("WARNING", "Jumlah layer pertama maksimal 25!")
    else:
        valid = True
        layer_1 = int(layer_1)

valid = False
while(not valid):
    lebar_layer = int(turtle.numinput('input', 'Masukkan lebar badan tower(Maksimal 10): ')) #Menginput lebar layer tower 
    if int(lebar_layer) > 10:
        messagebox.showinfo("WARNING", "Lebar badan tower maksimal 10!")
    else:
        valid = True
        lebar_layer = int(lebar_layer)

turtle.penup()
turtle.setposition(-400, -200) #Penempatan posisi tower
turtle.speed(0)
counter = 0
for x in range(jumlah_tower): 
    turtle.penup
    turtle.pendown
    layer_sekarang = layer_1 + x * beda_tower

    for x in range(layer_sekarang): #Membuat bagian badan tower
        for x in range(lebar_layer):
            turtle.color('maroon', '#CA7F65')
            turtle.pendown()
            turtle.begin_fill()
            for x in range (2):
                turtle.forward(panjang_bata)
                turtle.left(90)
                turtle.forward(lebar_bata)
                turtle.left(90)
            turtle.end_fill()
            turtle.penup()
            turtle.forward(panjang_bata)
        
        turtle.backward(panjang_bata * lebar_layer)
        turtle.left(90)
        turtle.forward(lebar_bata)
        turtle.right(90)
        counter += lebar_layer
    turtle.backward(panjang_bata // 2)
    
    for x in range(lebar_layer + 1): #Membuat bagian kepala dari tower
        turtle.color('maroon', '#693424')
        turtle.pendown()
        turtle.begin_fill()
        for x in range(2):
            turtle.forward(panjang_bata)
            turtle.left(90)
            turtle.forward(lebar_bata)
            turtle.left(90)
        turtle.forward(panjang_bata)
        turtle.end_fill()
        turtle.penup()
    counter += lebar_layer + 1
    layer_sekarang = layer_sekarang + x * beda_tower #Mulai membuat Jamur pada bagian atas kepala tower
    turtle.left(90)
    turtle.forward(lebar_bata)
    turtle.left(90)
    turtle.forward((panjang_bata / 2) + (lebar_layer// 2 + 1) * panjang_bata )
    turtle.right(180)
    turtle.color('black', '#F0E3CE')
    turtle.begin_fill()
    for x in range(6):
        turtle.forward(panjang_bata)
        turtle.left(90)
    turtle.end_fill()
    turtle.color('black','red')
    turtle.begin_fill()
    turtle.backward(panjang_bata*0.5)
    turtle.right(90)
    turtle.circle(panjang_bata * 1,180)
    turtle.left(90)
    turtle.forward(panjang_bata*0.5)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(panjang_bata*(lebar_layer//2 + 1))

    turtle.setposition(turtle.xcor() + jumlah_tower * panjang_bata, -200) #Penempatan posisi jamur
    
    


turtle.up()
turtle.goto(0, -400) #Posisi tulisan
turtle.down()
turtle.write(f"{jumlah_tower} Super Mario Tower has been built with a total of {counter}", #Menginput teks berapa banyak block yang telah dihasilkan di tower 
            align='center', font={'Times New Roman'})
turtle.done()


#Kolaborator:
#2306201792 - Ilham Ghani Adrin Sapta
