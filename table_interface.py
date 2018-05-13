from pool_table import PoolTable
import datetime
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pickle

class TableInterface:

    def __init__(self):
        self.table_data = []
        self.run = True
        self.pool_tables = []
        self.create_tables()
        self.options()

    def create_tables(self):
        for table_num in range(1, 13):
            pool_table = PoolTable(table_num)
            self.pool_tables.append(pool_table)

# allows the user to interface with the program
    def options(self):
        while self.run == True:
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
        for pool_table in self.pool_tables:
            print(pool_table.table_num)
            print(pool_table.status)
            if pool_table.status == "Occupied":
                print(f"Start time: {pool_table.start_time}")
                pool_table.time_now = datetime.datetime.now()
                pool_table.time_elapsed = pool_table.time_now - pool_table.start_time
                print(f"Time elapsed: {pool_table.time_elapsed}")
        print('---------------------')

# allows the user to reserve a table and begins the timer
    def reserve_table(self):
        start_choice = int(input("Enter the pool table that you would like to reserve: "))
        pool_table = self.pool_tables[start_choice - 1]
        if pool_table.status == "Occupied":
            print(f"Pool Table {pool_table.table_num} is currently occupied.")
        else:
            pool_table.status = "Occupied"
            pool_table.start_time = datetime.datetime.now()
            print(f"You have successfully reserved table {pool_table.table_num}.")
            print("Enjoy your game!")


# allows the user to choose to end the reservation and calculates the total time
    def end_reservation(self):
        end_choice = int(input("Enter the pool table whose reservation you would like to end: "))
        pool_table = self.pool_tables[end_choice - 1]
        if pool_table.status == "Available":
            print(f"Pool Table {pool_table.table_num} is still available. Check your table number.")
        else:
            pool_table.status = "Available"
            pool_table.end_time = datetime.datetime.now()
            pool_table.total_time = pool_table.end_time - pool_table.start_time

            new_data = {
                "Table" : str(pool_table.table_num),
                "Start time": str(pool_table.start_time),
                "End time": str(pool_table.end_time),
                "Total time": str(pool_table.total_time)
            }

            self.table_data.append(new_data)

            for data_dict in self.table_data:
                for k, v in data_dict.items():
                    print(k + ": " + v)


            #with open("table_log.json", "w") as write_file:
            #    json.dump(pool_table.table_data, write_file)



    def email_log(self):
            date_today = datetime.datetime.today()
            msg = MIMEMultipart()
            msg['From'] = "uofhpoolhall@gmail.com"
            msg['To'] = "uofhpoolhall@gmail.com"
            password = "mypassword"
            msg['Subject'] = "U of H Pool Hall Daily Log"


            text = (f"Here is the U of H Pool Hall Daily Log for {date_today}")
            msg.attach(MIMEText(text, 'html'))


            #filename = "table_log.json"
            #with open(filename) as data_file:
            #    data = json.load(data_file)
            #print(json.dumps(data))

            attachment = MIMEText(json.dumps(data))
            attachment.add_header('Content-Disposition', 'attachment', filename="table_log.json")
            msg.attach(attachment)

            print(msg)

#            server = smtplib.SMTP("smtp.gmail.com", 587)
#            server.starttls()
#            server.login(msg['From'], password)
#            server.sendmail(msg['From'], msg['To'], msg.as_string())
#            server.quit()



# quits the program
    def quit(self):
        #self.email_log()
        print("Goodbye")
        self.run = False
