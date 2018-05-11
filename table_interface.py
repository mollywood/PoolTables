from pool_table import PoolTable

class TableInterface:

    def __init__(self):
        self.options()

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



#***    def reserve_table(self):
#        choice = int(input("Enter the pool table that you would like to reserve: "))
#        pool_table = pool_tables[choice - 1]
#        if pool_table.status =
#        print(pool_table.number)
