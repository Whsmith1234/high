import mysql.connector
from faker import Faker
fake = Faker()

print(fake.name())
mydb = mysql.connector.connect(
      host="wpra.mysql.pythonanywhere-services.com",
      user="wpra",
      password="#######",
      database="wpra$default"
    )
cur = mydb.cursor()
cur.execute("DELETE FROM Users");
for x in range(100):
    sql = "INSERT INTO Users (name, imageURL) VALUES (%s, %s)"
    val = (fake.name(), "https://randomuser.me/api/portraits/women/"+str(x)+".jpg")
    cur.execute(sql, val)
    mydb.commit()
    #sql = "SELECT * FROM STOCKS WHERE STOCK_NAME=%s"
    #cur.execute(sql, ("ab",))
