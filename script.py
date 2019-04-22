class Bank:

    banks = 0

    def __init__(self, name = "Credit Dnipro", number_of_clients = 1000,
            number_of_credits = 300, location = "Ukraine",
             year_of_foundation = 2001, capital = 1000000):
        self.name = name
        self.number_of_clients = number_of_clients
        self.number_of_credits = number_of_credits
        self.location = location
        self.year_of_foundation = year_of_foundation
        self.capital = capital
        Bank.banks = Bank.banks + 1

    def __del__(self):
        print("Destructor")

    def __str__(self):
        return"name" + self.name + "\n" \
            + "numberOfClients: " + str(self.number_of_clients) + '\n'\
            + "numberOfCredits: " + str(self.number_of_credits) + '\n'\
            + "location: " + self.location + '\n'\
            + "yearOffoundation: " + str(self.year_of_foundation) + '\n'\
            + "capital: " + str(self.capital)


    @staticmethod
    def get_static_field():
        return Bank.banks

def main():
    bank_Chernivtsi = Bank()
    bank_Lviv = Bank()
    bank_Kyiv = Bank()

    bank_Chernivtsi.name = "Chernivtsi"
    bank_Lviv.name = "Lviv"
    bank_Kyiv.name = "Kyiv"

    print("There are " + str(Bank.get_static_field()) + " banks in Ukraine:")

    print(bank_Chernivtsi)
    print(bank_Lviv)
    print(bank_Kyiv)


main()
