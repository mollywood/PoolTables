class PoolTable:

    def __init__(self):
        self.table_num = table_num
        occupied_status = False

    def __repr__(self):
        return (f"\n {self.table_num}=>  Status: {self.status}, Start time: {self.start_time}, End time: {self.end_time}, Total time: {self.total_time}")

    def create_tables(self):
        pool_tables = []
        for index in range(1, 13):
            pool_table = PoolTable(index)
            pool_tables.append(pool_table)

    #def show_available(self):
    #    while occupied_status == False:
    #        available_tables.append(self.table)
    #    print(available_tables)

    #def reserve_table(self):
    #    self.start_time = start_time
    #    self.end_time = end_time
    #    self.total_time = total_time
    #    while occupied_status == True:
    #        occupied_tables.append(self.table)
    #        start_time = datetime.datetime.now()
    #    else:
    #        end_time = datetime.datetime.now()
    #        total_time = end_time - start_time
