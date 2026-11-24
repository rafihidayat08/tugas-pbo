class PengunjungFestival:
    nama = ""
    asal = ""
    band_favorit = ""
    lagu_favorit = ""
    album_favorit = ""
    
    band_kedua = ""
    lagu_kedua = ""
    
    energi = 100

    def sapa(self, lawan):
        print(f"[{self.nama}]: Wah, panas banget ya nunggu di depan stage begini. Kenalkan, saya {self.nama} jauh-jauh dari {self.asal}.")
        print(f"[{lawan.nama}]: Iya nih, suasananya asyik parah. Saya {lawan.nama} dari {lawan.asal}.")

    def obrolan_musik(self, lawan):
        print(f"[{lawan.nama}]: Kamu ke sini nungguin band siapa yang main nih, {self.nama}?")
        print(f"[{self.nama}]: Saya jelas nungguin {self.band_favorit} dong. Kalau kamu sendiri nungguin band apa, {lawan.nama}?")
        print(f"[{lawan.nama}]: Saya lagi nungguin {lawan.band_favorit} main nih. Kebetulan banget urutan line up-nya asyik, {self.band_favorit} main duluan, nah sehabis itu baru deh {lawan.band_favorit} yang main.")
        print(f"[{self.nama}]: Wah, pas banget urutannya! Bisa sekalian nonton bareng terus nih kita, soalnya saya juga suka dengerin {self.band_kedua}.")
        print(f"[{lawan.nama}]: Loh, kebetulan banget! Saya juga lumayan ngikutin {lawan.band_kedua} lho.")
        print(f"[{lawan.nama}]: Kalau gitu, lagu andalan kamu dari {self.band_favorit} apa nih?")
        print(f"[{self.nama}]: Saya paling suka {self.lagu_favorit}. Tapi kalau ditanya keseluruhan, saya pastinya paling suka album '{self.album_favorit}'.")
        print(f"[{self.nama}]: Nah, kalau kamu lagu andalan dari {lawan.band_favorit} apa?")
        print(f"[{lawan.nama}]: Kalau saya paling bener dengerin {lawan.lagu_favorit}. Untuk albumnya, saya paling suka album '{self.album_favorit}'.")
        print(f"[{lawan.nama}]: Terus kalau dari {lawan.band_favorit}, kamu paling suka lagu apa, {self.nama}?")
        print(f"[{self.nama}]: Saya suka banget {self.lagu_kedua}. The best lah pokoknya.")
        print(f"[{lawan.nama}]: Sefrekuensi banget kita! Kalau saya dari {self.band_favorit} sih sukanya dengerin {lawan.lagu_kedua}.")

    def vibing_bareng(self, lawan):
        print(f"\n--- Tiba-tiba suara musik dari panggung mulai terdengar ---")
        print(f"[{lawan.nama}]: Eh, {self.nama}, denger tuh! Intronya {self.band_favorit} udah mulai dimainin, lampu stage-nya udah nyala!")
        print(f"[{self.nama}]: Wah iya bener! Ayo maju dikit ke tengah biar dapet spot asik buat loncat-loncat nonton {self.band_favorit}.")
        print(f"[{lawan.nama}]: Gas! Nanti abis {self.band_favorit} kelar, kita lanjut stay di depan buat vibing pas {lawan.band_favorit} main!")
        print(f"[{self.nama}]: Let's gooo! Mari kita vibing bareng, {lawan.nama}!")

    def nonton_konser(self):
        print(f"\n--- [Konser Berlangsung: {self.band_favorit} & {self.band_kedua} Tampil Memukau] ---")
        print(f"[* {self.nama} dan kawan-kawan loncat-loncat, sing along, dan moshing sepanjang penampian... *]")
        self.energi -= 65  # Energi berkurang 65
        print(f"[Sistem status]: Energi {self.nama} berkurang! Sisa energi sekarang: {self.energi}%")

    def pamit_pulang(self, lawan):
        print(f"\n--- Acara Musik Selesai ---")
        if self.energi < 50:
            print(f"[{self.nama}]: Aduh, cape parah nih kaki udah mau lemes, energi sisa {self.energi}% doang haha.")
            print(f"[{self.nama}]: Saya pamit balik duluan ya, {lawan.nama}. Kamu habis ini langsung balik ke {lawan.asal}?")
            print(f"[{lawan.nama}]: Sama nih, saya juga udah pegel banget. Iya habis ini saya langsung balik ke {lawan.asal}. Thanks ya udah barengan!")
            print(f"[{self.nama}]: Siap, hati-hati di jalan balik ke {lawan.asal}! Saya juga mau OTW balik ke {self.asal}.")


# 1. Membuat Object
rapi = PengunjungFestival()
dimas = PengunjungFestival()

# 2. Mengisi Attributes Rapi
rapi.nama = "Rapi"
rapi.asal = "Cilegon"
rapi.band_favorit = "510"
rapi.lagu_favorit = "'Sorry' dari Album Origin dan 'R U Broken 2?' dari EP Spiritual" 
rapi.album_favorit = "Origin"
rapi.band_kedua = "Perunggu"
rapi.lagu_kedua = "'Prematur' sama 'Haru Paling Biru'"

# 3. Mengisi Attributes Dimas
dimas.nama = "Dimas"
dimas.asal = "Bekasi"
dimas.band_favorit = "Perunggu"
dimas.lagu_favorit = "'Gemilang' sama 'Kalibata 2012'"
dimas.album_favorit = "Memorandum"
dimas.band_kedua = "510"
dimas.lagu_kedua = "'Esa' sama 'Emotional Renegades'"

# 4. Memanggil Method
rapi.sapa(dimas)
print("-" * 55)
rapi.obrolan_musik(dimas)
rapi.vibing_bareng(dimas)

# Alur tambahan sampai acara selesai
rapi.nonton_konser()
rapi.pamit_pulang(dimas)