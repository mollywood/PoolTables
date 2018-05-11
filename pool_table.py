class PoolTable:

    def __init__(self):
        self.table_num = table_num
        status = "Available"
        pool_tables = []

    def __repr__(self):
        return (f"\n {self.table_num}=>  Status: {self.status}, Start time: {self.start_time}, End time: {self.end_time}, Total time: {self.total_time}")

    def create_tables(self):
        for index in range(1, 13):
            pool_table = PoolTable(index)
            pool_tables.append(pool_table)
