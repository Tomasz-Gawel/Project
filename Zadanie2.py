# Zadanie 2 Konwersja temperatury z Fahrenhaita na Celcjusza, oraz na Kelvina
# Zainicjalizuj temp w Farh
# Zainicjalizuj temp w Celcjuszach jako nowa zmienna np: temp_cel i przypisz do niej wynik konwersji
# Zainicalizuj temp w Kelwinach jako nowa zmienna np: temp_kel i przypisz do niej wynik konwersji

# Formula z Fahrenhaita na Celcjusza, °C = 5/9 * (°F - 32)
# Formula z Fahrenhaita na Kelwina K= 9/5*(°F−32)+273,15

# Zakładamy wynik jako liczba całkowita
tfarh = 80



temp_cel =5/9 *(tfarh-32)
temp_kel= 9/5*(tfarh- 32)+273.15

print("Temperatura w stopniach Celcjusza  wynosi:",(int(temp_cel)))
print("Temperatura w stopniach Kelwina wynosi:",(int(temp_kel)))