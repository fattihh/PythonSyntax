def buyuk_olan(s1, s2):
    if s1 > s2:
        return s1
    if s2 > s1:
        return s2


a = int(input("Bir sayı giriniz : "))
b = int(input("Bir sayı giriniz : "))

print(f'{buyuk_olan(a,b)} daha büyüktür.')

