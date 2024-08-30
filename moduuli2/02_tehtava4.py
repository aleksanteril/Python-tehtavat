
#Kysytään 3 syötettä
num1 = int(input("Anna 1. kokonaisluku: "))
num2 = int(input("Anna 2. kokonaisluku: "))
num3 = int(input("Anna 3. kokonaisluku: "))

#Tehdään laskutoimitukset
num_sum = num1 + num2 + num3
num_product = num1 * num2 * num3
num_avg = (num_sum / 3)

#Tulostetaan tulokset
print("Lukujen summa on: " + str(num_sum) +
      "\nLukujen tulo on: " + str(num_product) +
      "\nLukujen keskiarvo on: " + str(num_avg))

