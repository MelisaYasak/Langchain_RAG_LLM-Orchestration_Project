# 1) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız

my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}
print("c" in my_dictionary.values())

# 2) Aşağıdaki listedeki sayılardan sadece çift sayı olanları başka bir listeye kaydeden bir kod yazınız.

my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]

evenList = [i for i in my_numbers if i %2 == 0]
print(evenList)

# 3) Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2 * pi * r)  Pi 3.14 alınabilir.

r_list = [3,2,5,8,4,6,9,12]
PI = 3.14
cevre = [2*PI*r for r in r_list]
print(cevre)

# 4) Aşağıdaki listede isim - yaş eşleşmelerinin bulunduğu yapılar mevcuttur. Sadece yaşların olduğu yeni ve ayrı bir liste oluşturunuz.

age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]
age_list = [i[1] for i in age_name_list]
print(age_list)

# 5) Aşağıdaki müzik gruplarından birini rastgele yazdıran bir kod yazınız

metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]
import random
print(random.choice(metal_list))

# 6) Aşağıdaki kodun çıktısı ne olacaktır?

number_list = [5,7,18,21,20,10,405,24]

# [num % 2 == 0 for num in number_list]
# >>> Çift sayıların olduğu bir liste

#7) Aşağıdaki string dizisinde, içinde sadece XYZ geçen barkodları gösterecek yeni bir liste oluşturunuz

barcodeList = ["ABC231","SA3123XYZ","XYZA123Q","QRE1231KJ","X112QGL"]
barcodeList_XYZ = [i for i in barcodeList if "XYZ" in i ]
print(barcodeList_XYZ)
#8) Aşağıda yazdırılan sınıfı incelediğinizde my_cat.multiply_age() kodunun çıktısı ne olacaktır?


class Cat:
    def __init__(self, name, age=5):
        self.name = name
        self.age = age

    def multiply_age(self):
        return self.age * 3

my_cat = Cat("Whiskers")
#my_cat.multiply_age()
# >>> 15
