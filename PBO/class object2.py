class Band:
    pass
class Lagu:
    pass

band1 = Band()
band1.nama = "Sleep Token"
band1.genre = "Alternative Metal"

band2 = Band()
band2.nama = "Sleep Theory"
band2.genre = "Rock"

print("Nama Band 1:", band1.nama, "| Genre:", band1.genre)
print("Nama Band 2:", band2.nama, "| Genre:", band2.genre)

lagu1 = Lagu()
lagu1.judul = "Euclid"
lagu1.durasi = 5.14

lagu2 = Lagu()
lagu2.judul = "Words Are Worthless"
lagu2.durasi = 3.40

print("Judul Lagu 1:", lagu1.judul, "| Durasi:", lagu1.durasi, "menit")
print("Judul Lagu 2:", lagu2.judul, "| Durasi:", lagu2.durasi, "menit")