#Python'da değişkenleri ve matematiksel operatörleri kullanarak vücut kitle indeksi hesaplama aracı
boy = input("Boy Uzunluğunuz (metre cinsinden 1.92 gibi): ")
kilo = input("Kilonuz: (kilogram cinsinden): ")
metrekare = float(boy)*float(boy)
vki = float(kilo)/(metrekare)
print(vki)