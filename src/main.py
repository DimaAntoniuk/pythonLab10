from src.script import script

def main():
    bank_Chernivtsi = Bank()
    bank_Lviv = Bank()
    bank_Kyiv = Bank()

    bank_Chernivtsi.name = "Chernivtsi"
    bank_Lviv.name = "Lviv"
    bank_Kyiv.name = "Kyiv"

    print("There are " + Bank.get_static_field() + " banks in Ukraine:")

    print(bank_Chernivtsi)
    print(bank_Lviv)
    print(bank_Kyiv)


main()
