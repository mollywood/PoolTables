from pool_table import PoolTable
import datetime

class TableInterface:

    def __init__(self):
        self.options()

# allows the user to interface with the program
    def options(self):
        user_selection = int(input("1 view tables | 2 reserve a table | 3 end a reservation | 4 exit"))

        if user_selection == 1:
            self.view_all()
        if user_selection == 2:
            self.reserve_table()
        if user_selection == 3:
            self.end_reservation()
        if user_selection == 4:
            self.quit()

# gives the user the ability to view all of the tables
    def view_all(self):
        print('-----Pool Tables-----')
        for p in pool_tables:
            print(p.number)
            print(p.status)
        print('---------------------')

# allows the user to reserve a table and begins the timer
    def reserve_table(self):
        start_choice = int(input("Enter the pool table that you would like to reserve: "))
        pool_table = pool_tables[start_choice - 1]
        if pool_table.status == "Occupied":
            print(f"Pool Table {pool_table.table_num} is currently occupied.")
        else:
            pool_table.status = "Occupied"
            pool_table.start_time = datetime.datetime.now()

# allows the user to choose to end the reservation and calculates the total time
    def end_reservation(self):
        end_choice = int(input("Enter the pool table whose reservation you would like to end: "))
        pool_table = pool_tables[end_choice - 1]
        if pool_table.status == "Available":
            print(f"Pool Table {pool_table.table_num} is available. Check your table number.")
        else:
            pool_table.status = "Available"
            pool_table.end_time = datetime.datetime.now()
            pool_table.total_time = pool_table.end_time - pool_table.start_time
            print(f"You used {[pool_table.table_num]} from {pool_table.start_time} to {pool_table.end_time}. The total time was {pool_table.total_time}")

# quits the program
    def quit(self):
        print("Goodbye")
