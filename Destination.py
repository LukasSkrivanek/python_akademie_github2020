# Pozdrav klienta
print("="*25)
print("Welcome to the DESTINATION")
print("place where people plan their trips")
print("="*25)

# Nabídni mu destinace
print("We can offer you the following destinations: ")
print("-"*25)
print("""
1 - Prague	1000
2 - Wien	1100
3 - Brno	2000
4 - Svitavy	1500
5 - Zlin	2300
6 - Ostrava	3400
""")
print("-"*25)
# Získej vstup uživatele o destinaci
mesta = ("Prague","Wien","Brno","Svitavy","Zlin","Ostrava")
cena = (1000,1100,2000,1500,2300,3400)
cilova_destinace_index = int(input("Please enter the destination number:"))
destinace = mesta[cilova_destinace_index -1]
cena_cilove_destinace = cena[cilova_destinace_index -1]
print("REGISTRATITON:")
print("-"*25)
print("in order to complete your reservations, please share few details about yoursefl with us.")

# Přiřaď proměnným příslušná data

# Získej data z proměnných podle vstupu uživatetele

# Začni registraci

# Získej vstup uživatele o jeho osobních datech
print("-"*25)
name = input("NAME: ")
print("="*25)
surname = input("SURNAME: ")
print("="*25)
year = input("YEAR OF BIRTH: ")
print("="*25)
email = input("EMAIL: ")
print("="*25)
password = input("PASSWORD: ")
print("="*25)

# Poděkuj uživateli použitím jeho jménaa informuj jej/jí o provedení rezervace
print("Thank you ",name)
print("We have made your reservation to ",destinace)
print("The total price is ",cena_cilove_destinace)