class PoolTable:

    def __init__(self):
        self.table_num = table_num
        status = "Available"
        pool_tables = []
        self.create_tables()

    def create_tables(self):
        for table_num in range(1, 13):
            pool_table = PoolTable(table_num)
            pool_tables.append(pool_table)

    def __repr__(self):
        return (f"\n {self.table_num}=>  Status: {self.status}")
