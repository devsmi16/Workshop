class Ogrenci:
    'Tüm öğrenciler için temel sınıf'
    Ogrenci_sayisi = 0

    def __init__(self, name, numarasi):
        self.name = name
        self.numarasi = numarasi
        Ogrenci.Ogrenci_sayisi += 1

    def OgrenciSayisiGoster(self):
        print("Toplam öğrenci: %d" % Ogrenci.Ogrenci_sayisi)

    # ogrenci sayisini gosterıyo
    def OgrenciGoster(self):
        print("name : ", self.name, ", Numarası: ", self.numarasi)

        ogr1 = Ogrenci('Sami', '2151')
        print(ogr1.name)

        ogr1.OgrenciSayisiGoster()
        ogr1.OgrenciGoster()

        ogr2 = Ogrenci('ramazan', '234234')
        ogr2.OgrenciSayisiGoster()

        ogr1.OgrenciSayisiGoster()
