name = str(input("Masukkan name: "))
nim = str(input("Masukkan NIM: "))
budgetLaptop = int(input("Masukkan budget laptop anda: "))

print(f"\n{name} dengan NIM {nim} ingin membeli laptop dengan budget {budgetLaptop:,}".replace(',', '.'))


budgetAcer= int(budgetLaptop - (budgetLaptop * 0.05))
budgetAsus = int(budgetLaptop - (budgetLaptop * 0.07))
budgetLenovo = int(budgetLaptop - (budgetLaptop * 0.10))


print(f"\nbudget Acer setelah diskon 5% : {budgetAcer:,}".replace(',', '.'))
print(f"budget Asus setelah diskon 7% : {budgetAsus:,}".replace(',', '.'))
print(f"budget Lenovo setelah diskon 10% : {budgetLenovo:,}".replace(',','.'))