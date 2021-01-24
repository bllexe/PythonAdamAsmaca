
import random

image = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
  /    |
       |
--------"""]

while True:
    print("Sehir Tahmin Etme -----Adam Asmaca")
    
    sehirler=random.choice(['Adana', 'Adiyaman', 'Afyon', 'Ağrı', 'Amasya', 'Ankara', 'Antalya', 'Artvin',
    'Aydın', 'Balıkesir', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa', 'Çanakkale',
    'Çankırı', 'Çorum', 'Denizli', 'Diyarbakır', 'Edirne', 'Elazığ', 'Erzincan', 'Erzurum', 'Eskişehir',
    'Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkari', 'Hatay', 'Isparta', 'Mersin', 'İstanbul', 'İzmir', 
    'Kars', 'Kastamonu', 'Kayseri', 'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Kütahya', 'Malatya', 
    'Manisa', 'Kahramanmaraş', 'Mardin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu', 'Rize', 'Sakarya',
    'Samsun', 'Siirt', 'Sinop', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'Şanlıurfa', 'Uşak',
    'Van', 'Yozgat', 'Zonguldak', 'Aksaray', 'Bayburt', 'Karaman', 'Kırıkkale', 'Batman', 'Şırnak',
    'Bartın', 'Ardahan', 'Iğdır', 'Yalova', 'Karabük', 'Kilis', 'Osmaniye', 'Düzce'])
    hak = 0
    tahmin = []
   
   
    while True:
        print(image[hak])
        
        for i, char in enumerate(sehirler):
            print(char if i in tahmin else "-"),
            
        cevap = input("Kelimeyi  Tahmin Edin: ")
        
        if cevap == sehirler:
            print("Win")
            break
        else:
            while True:
                rastgele = random.randint(0, len(sehirler))
                if not rastgele in tahmin:
                    tahmin.append(rastgele)
                    break
            
            hak += 1
        
        if hak >= len(sehirler):
            print("Lose")
            break
        
    if not "y" == input("RePlay  (y/n): "):
        break
