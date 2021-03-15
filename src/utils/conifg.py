host="localhost",
user="yourusername",
password="yourpassword",
database="mydatabase"

table_schema = "(Customer Name VARCHAR(255) PRIMARY KEY NOT NULL," \
               " Customer ID VARCHAR(8) NOT NULL," \
               " Customer Open Date DATE NOT NULL," \
               "Last Consulted Date DATE," \
               "Vaccination Type CHAR(8)," \
               "Doctor Consulted CHAR(255)," \
               "State CHAR(5)," \
               "Country CHAR(5)," \
               "Post Code INT," \
               "Date Of Birth DATE," \
               "ACTIVE CUSTOMER CHAR(1))"