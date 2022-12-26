# pythonda birden fazla yerde aynı değer kullanılacaksa genelde o değer bir değişkende tutulur. İstenildiği zaman değişken çağırılır veya değişkenin değeri değiştirilerek o değişkenin kullanıldığı yerlerdeki değerler değiştirilmiş olur.

isciMaas = 8500
isciKesinti = 0.28

kesintiToplami =  isciMaas * isciKesinti
eleGecenPara = isciMaas - kesintiToplami
print(kesintiToplami)
print(eleGecenPara)

# Değişken Tanımlama Kuralları
# 1- Değişken tanımlandığı anda değeri aktarılmalıdır. Değişkene değer atamak için "=" operatörü kullanılır. EşitLiğin sağındaki ifade solundaki ifadeye aktarılır.
maas = 9850

# 2- Rakam ile başlayamaz.
# 1yaz = 52
yaz1 = 52

# 3- Büyük Küçük harf duyarlılığı vardır. Aynı kelimelerde 2 tane değişken tanımmış olsa bile bir tane harf diğerinden büyük veya küçük yazılmış ise bu iki deişken birbirinden farklıdır.

babaYasi = 74
BabaYasi = 84
print('Babamın Yaşadığı Zaman:')
print(babaYasi)
print('Babamın Yaşadığı Zaman:')
print(BabaYasi)


# 4- Türkçe Karakter kullanmamaya dikkat edilmelidir.
yaş = 32 # yaş yerine "yas" yazılabilir.
print(yaş)


# Her türlü değişken türüne göre değişken tanımlama
age = 15         # int
y = 5.78         # float
name = "Kerim"   # String
isStudent = True # Bool

# Her değişkene ayrı ayrı değer atayabileceğimiz gibi bir satırda tüm kişileri doyuran kişidir.
age, y, name, isStudent = (25, 8.74, "Kerim", True)