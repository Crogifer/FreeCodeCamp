class Category:

    def __init__(self, category):
        self.description = category
        self.ledger = []
        self.balance = 0.0

    def __str__(self):
        output = self.description.center(30,"*") + "\n"
        for line in self.ledger:
            line_description = "{:<23}".format(line["description"])
            line_amount = "{:>7.2f}".format(line["amount"])
            output += "{}{}\n".format(line_description[:23], line_amount[:7])
        output += "Total: " + str(self.get_balance())
        return output

    def deposit(self, amount, description = ""):
        if description == False:
            description = ""
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def get_balance(self):
        return self.balance
    
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
        
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) == True:
            self.ledger.append(({"amount": amount*-1, "description": description}))
            self.balance -= amount
            return True
        else:
            return False
        
    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.description}"):
            category.deposit(amount, f"Transfer from {self.description}")
            return True
        else:
            return False
        
def create_spend_chart(categories):
    #for 4 or less categories
    if len(categories) >= 4:
        return False
    else:
        total_spent = []
        total_balance = []
        categories_tens = []

        #find total spend of all categories and calculate the number of 10-sized percentage markers for each category relative to total spend
        for category in categories:
            spent = 0
            for item in category.ledger:
                if item["amount"] < 0:
                    spent += abs(item["amount"])
                    total_spent.append(round(spent, 2))
        for totals in total_spent:
            categories_tens.append(int(((totals / sum(total_spent)) * 100)/10))

        #in list of each category, create list for each category and replace tens value with list of 10 indexes, if a ten for that 10 exists, append "o", else " "
        for index, value in enumerate(categories_tens):
            temp = categories_tens[index]
            categories_tens[index] = []
            x = 0
            while x <= 10:
                if x <= temp:
                    categories_tens[index].append("o")
                    x += 1
                else:
                    categories_tens[index].append(" ")
                    x += 1

        #Create chart, header text, and seperator line
        text_out = ""
        line0 = "Percentage spent by category"
        text_out += line0
        percentage = 100
        count = 0

        for category in categories_tens:
            category.reverse()

        while count <= 10:
            text_out += "\n" + f"{percentage}|".rjust(4) + f" {categories_tens[0][count]}  "
            if len(categories) > 1:
                text_out += f"{categories_tens[1][count]}  "
            if len(categories) > 2:
                text_out += f"{categories_tens[2][count]}  "
            if len(categories) > 3:
                text_out += f"{categories_tens[3][count]}  "
            percentage -= 10
            count += 1
        text_out += "\n" + "    " + "-" * ((3 * len(categories)) + 1) + "\n"

        #Create chart footer
        #find length of longest category
        max_len = 0
        for category in categories:
            if len(category.description) > max_len:
                max_len = len(category.description)

        #make all category names same length with spaces
        new_categories = []

        for category in categories:
            if len(category.description) < max_len:
                category_new = ""
                difference = max_len - len(category.description)
                category_new += category.description + " " * difference
                capitalised = category_new.capitalize()
                new_categories.append(capitalised)
            else:
                capitalised = category.description.capitalize()
                new_categories.append(capitalised)

        #create footer text
        footer_lines = 0
        footer = ""
        while footer_lines < max_len:
            footer += f"     {new_categories[0][footer_lines]}  "
            if len(categories) > 1:
                footer += f"{new_categories[1][footer_lines]}  "
            if len(categories) > 2:
                footer += f"{new_categories[2][footer_lines]}  "
            if len(categories) > 3:
                footer += f"{new_categories[3][footer_lines]}  "
            footer_lines += 1
            if footer_lines < max_len:
                footer += "\n"
            
        text_out += footer

        return text_out

        
"""
def test_create_spend_chart(self):
        self.food.deposit(900, "deposit")
        self.entertainment.deposit(900, "deposit")
        self.business.deposit(900, "deposit")
        self.food.withdraw(105.55)
        self.entertainment.withdraw(33.40)
        self.business.withdraw(10.99)
        actual = create_spend_chart([self.business, self.food, self.entertainment])
        return actual
"""

food = Category("food")
food.deposit(900, "deposit")
entertainment = Category("entertainment")
entertainment.deposit(900, "deposit")
business = Category("business")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
"""
print(food)
print("\n")
print(entertainment)
print("\n")
print(business)
"""
actual = create_spend_chart([business, food, entertainment])

f = open("myfile.txt", "w")
f.write(actual)
print(actual)
