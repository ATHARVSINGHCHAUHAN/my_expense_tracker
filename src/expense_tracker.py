import json
import os
from datetime import datetime

# I chose json I chose for storage it is simple and we can easily read it

class ExpenseTracker:

    def __init__(self) :

        self.my_expense_list  =  [  ]  

        self.data_file = "my_expenses.json"  #  M ore spec ific filename

        #these catogries covers most of ex penses

        self.spending_types  =  ["Food" , "Transport" , "Entertainment" , "Bills" , "Shopping" , "Other"]

        self.load_expenses(  )



    
    def load_expenses(self):

        """I added error handling here because file operations can fail
        If the file doesn't exist or is corrupted, we start fresh"""

        if  os.path.exists (self.data_file)  :

            try :

                with open (self.data_file, 'r') as file  :

                    self.my_expense_list = json.load (file)

                print ("Loaded   your  existing   expenses")

            except Exception as e :

                # If something  goes  wrong , we'll  start  with  empty  list

                print (f"Note :  Starting fresh  -  { e }")

                self.my_expense_list = [ ]

        else:
            self.my_expense_list = [ ]
    



    def save_expenses(self) :

        """Save  expenses to JSON file  - I used inden t=2 to make it  readable """

        with open (self.data_file, 'w') as file :

            json.dump (self.my_expense_list, file, indent=2)


    
    def add_expense(self) :


        """I learned  about input validation   the hard way
        Now  I always check if inputs are valid before processing """

        print("\n"   + "="*40  )

        print("ADD  NEW  EXPENSE")

        print ( "="*40 )


        
        # My validation    approach - prevents  crashe s from bad inp ut

        try:

            amount_input  = input("How much did you   spend? ₹")

            amount = float (amount_input)


            
            # I added   this check after testing with negative numbers


            if amount <= 0 :

                print(" Amount should be positive!")

                return
            

            
            # Show categories with numbers for  easy selection


            print("\n  Where did you spend this money?")

            for i, category in   enumerate(self.spending_types,  1) :

                print(f"{i}. {category}")
            
            # Get category choice with validation 





            try:

                choice_input  = input("\n  Choose category (1-6):  ")

                choice =   int(choice_input)


                if 1 <=   choice <= 6 :

                    selected_category = self.spending_types  [choice - 1]

                else:  



                    print(" Please choose a number between 1-6!")

                    return
                
                 
                
            except ValueError :

               
               
                print("Please enter a valid number!")

                return
            
            
            # Get description   -   handle empty input




            description = input("What was this for? "). strip()

            if not description :




                description = "Miscellaneous expense"


            
            # Expense dictionary




            new_expense =  {
                'amount': amount, 

                'category': selected_category,


                'description': description,


                'date': datetime.now().strftime("%Y-%m-%d")

            }

            
            self.my_expense_list.append (new_expense)

            self.save_expenses ()

            print(f" Added: {selected_category}    - ₹ {amount:.2f}")


            
        except ValueError:




            print("Please enter a valid number for amount!")
    
    def view_expenses(self):


        """This is my   approach to displaying expenses
        I wanted it to be easy to read with clear formatting"""


        if len(self.my_expense_list) == 0:  # Instead of 'if not self.expenses'

            print("\n   No expenses to show yet!")

            return
        


        # I added this counter manually to show numbering


        expense_count = 1

        running_total =  0.0
        
        print("\n" + "="*50 )

        print("YOUR EXPENSE HISTORY")

        print("="*50)


        
        for expense in self.my_expense_list:

            # My custom formatting - took some trial and error to get right


            print(f"{expense_count}. {expense['date']} | {expense['category']:12} | ₹{expense['amount']:7.2f} | {expense['description']}")

            running_total += expense['amount']

            expense_count += 1  # Manual increment
        

        print("="*50)

        print(f"YOUR TOTAL SPENDING: ₹{running_total:.2f}")
    
    def view_by_category(self):


        """I added this feature to see where my money   goes each month
        It helps me understand my spending patterns"""


        if len(self.my_expense_list) == 0 :

            print("\n  No expenses found!")

            return
        
        
        ## Using dictionary to group by category

        category_totals = {  }

        for expense in self.my_expense_list:

            current_category = expense['category']


            if current_category in category_totals :


                category_totals[current_category] += expense['amount']

            else :

                category_totals[current_category] = expense['amount']

        
        print("\n" + "="*40)

        print("WHERE YOUR MONEY WENT")

        print("="*40)


        
        grand_total = 0 


        for category, amount in category_totals.items() :

            print(f"  {category}: ₹{amount:.2f}")

            grand_total += amount
        
        print("-" * 40)


        print(f"  TOTAL: ₹{grand_total:.2f}")

    
    def backup_data(self):


        """I added this to create backup files
        This was extra but I thought it would be useful"""



        backup_name = f"expenses_backup_{datetime.now().strftime('%Y%m%d_%H%M')}.json"

        with open(backup_name, 'w')  as backup_file :


            json.dump(self.my_expense_list, backup_file, indent=2)

        print(f"Backup created: {backup_name}")

    
    def show_menu(self):

        """I designed this menu to be user-friendly
        The emojis make it more   e ngaging for daily use"""

        print("\n" + "="*45)

        print("  MY PERSONAL EXPENSE TRACKER ")

        print( "="*45 )  



        print("1.Add  New Expense")

        print("2.View My Expenses ") 

        print("3.See Where My Money  Goes")

        print("4.Backup  Data")

        print("5. Exit")



        print("="*45)


    
    def run(self):

        """Main program loop   - this is wh ere everyth ing starts"""

        print(" Welcome to My  Personal Expense Tracker!")

        print("All amounts in Indian Rupees (INR)")

        print("Your data is automatically saved !  " )


        
        # This was my debugging code during development


        ## Uncomment to see raw data structure

        ### print("DEBUG: Current expenses:", self.my_expense_list)
        


        while True :

            self.show_menu()

            user_choice = input("What would you like to do? (1-5): ").strip()

            
            if user_choice == '1':


                self.add_expense()

            elif user_choice == '2':


                self.view_expenses()

            elif user_choice == '3' :

                self.view_by_category()

            elif user_choice == '4':

                self.backup_data()

            elif user_choice == '5':



                print("\n Thanks for using My Expense Tracker!")

                print("Your data has been saved!")

                break



            else:

                print("Please enter a number between 1-5!")



# My first attempt at date handling - kept for reference

## expense_date = input("Enter date (YYYY-MM-DD): ")

### if not expense_date :

####     expense_date = datetime.now (). strftime("%Y- %m-%d")

#####    Run the program



if __name__ == "__main__"  :

    my_tracker = ExpenseTracker  ()

    my_tracker.run ()



       

       