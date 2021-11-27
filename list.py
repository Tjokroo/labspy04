list=["h","u","r","u","f"]

print ("Tampilkan elemen ke-tiga: ", list[2])
print ("Ambil nilai elemen ke2 sampai ke4: ", list[1:4])
print ("Ambil elemen terakhir: ", list[-1])

# Merubah elemen ke4 menjadi nilai lain
list[3] = "k"
print ("Merubah elemen ke 4 dengan nilai lain: ", list)

# Merubah elemen ke 4 sampai terakhir
list[3:] = "a","h"
print ("Merubah elemen ke 4 sampai terakhir :", list)




# Tambah elemen list 
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# Ambil 2 buah bagian list A ke list B
b.append(a[1:3])
print("2 bagian dari list A dijadikan list B :", b)

# Tambah list B dengan nilai string
b.append("Hallo")
print("Tambah list B dengan string: ", b)

# Tambah list B dengan 3 nilai
print("Tambah list B dengan 3 nilai: ", b+[11,12,13])

# Menggabungkan list B dengan list A
c=b+a
print("Hasil dari penggabungan list B dengan list A: ", c)
