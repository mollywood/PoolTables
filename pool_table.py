class PoolTable:
    def __init__(self, table_num):
        self.status = "Available"
        self.table_num = table_num
        


    def __repr__(self):
        return (f"\n {self.table_num}=>  Status: {self.status}")
