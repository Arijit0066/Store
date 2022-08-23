
from os import system


class Store():
    def __init__(self, storeProduct):
        self.product = storeProduct

    def displayProduct(self):
        print("====Available Products====")
        for productDisplay in self.product:
            print("   -" + productDisplay)

    def buyItem(self, itemName):
        if itemName in self.product:
            print(f"Thank Your for Purchasing {itemName}. Have A good Day!")
            self.product.remove(itemName)
            return True
        else:
            print(f"Sorry this item is not availabe in Store. Kindly wait for some days.")
            return False
        
    def Additem(self, AdditemName):
        self.product.append(AdditemName)
        print("Done Sir")

    def ReportSave(self, ReportSave):
        with open("report.txt", "a") as f:
            f.write(f"-{ReportSave}  ")
            print("Sorry for this. we will try to solve your problem.")


class User():

    def RequestItem(self):
        print("====> Send Your Request Here <====")
        self.product = input("Enter The Item Name(Pascal Case) : ")
        if self.product in allProd:
            print("This Item Available In Store. Please Check the Store Again!!")
        else:
            with open("ReqItem.txt", "a") as f:
                f.write(f"'{self.product}', ")
                print(
                    "Thank You For Requesting The Item !! We will try to bring the Item.")

    def buyproductIN(self):
        self.product = input("Enter The Product you want to but? : ")
        return self.product

    def report(self):
        self.product = input("What's the problem you will faced sir? : ")
        return self.product


class manager():
    def AdditemManager(self):
        self.product = input("Item Name Please : ")
        return self.product
    




if __name__ == "__main__":
    moreItem = ''
    allProd = ['Biscuit', 'Chocolate', 'Ice Cream', 'Juice', 'Pen', 'pencil', 'candy']
    cityStore = Store(allProd)
    person = User()
    arijit = manager()
    system("cls")
    while(True):
        print("=======> Welcome To CityStore <=======")
        print("\tPlease choose an option")
        print("\t1. All Item List.")
        print("\t2. Request A Item.")
        print("\t3. Buy Item.")
        print("\t4. Report or FeedBack.")
        print("\t5. Add Item(Not For Customers)")
        print("\t6. Exit.")
        userChoice = int(input("\tEnter Your Choice : "))
        if userChoice == 1:
            cityStore.displayProduct()
        elif userChoice == 2:
            person.RequestItem()
        elif userChoice == 3:
            cityStore.buyItem(person.buyproductIN())
        elif userChoice == 4:
            cityStore.ReportSave(person.report())
        elif userChoice == 5:
            cityStore.Additem(arijit.AdditemManager())
        elif userChoice == 6:
            print("Thanks for coming City Store. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
