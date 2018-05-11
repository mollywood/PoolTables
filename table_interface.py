from pool_table import PoolTable
import datetime

class TableInterface:

    def __init__(self):
        pass

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

    def view_all(self):
        print('-----Pool Tables-----')
        for p in pool_tables:
            print(p.number)
            print(p.status)
        print('---------------------')

    def reserve_table(self):
        start_choice = int(input("Enter the pool table that you would like to reserve: "))
        pool_table = pool_tables[start_choice - 1]
        if pool_table.status = "Occupied":
            print(f"Pool Table {pool_table.table_num} is currently occupied.")
        else:
            pool_table.status = "Occupied"
            pool_table.start_time = datetime.datetime.now()

    def end_reservation(self):
        end_choice = int(input("Enter the pool table whose reservation you would like to end: "))
        pool_table = pool_tables[end_choice - 1]
        if pool_table.status = "Available":
            print(f"Pool Table {pool_table.table_num} is available. Check your table number.")
        else:
            pool_table.status = "Available"
            pool_table.end_time = datetime.datetime.now()
            total_time = end_time - start_time

    
