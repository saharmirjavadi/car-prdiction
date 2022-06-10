import mysql.connector
from sklearn import tree
from sklearn import preprocessing


# connection to database

cnx = mysql.connector.connect(user='root', 
                              password='1996', 
                              host='127.0.0.1', 
                              database='car_info', 
                              auth_plugin='mysql_native_password')
cursor = cnx.cursor()


# fetch data
cursor.execute('SELECT name, place, output, year, price FROM cars')
cars_list = []
for (name, place, output, year, price) in cursor:
    cars_list.append([name, place, output, year, price])


# change string to number
trans_list = []
for i in cars_list:
    machine = preprocessing.LabelEncoder()
    machine = machine.fit(i)
    trans_list.append(machine.transform(i))

x = []
y = []

for i in trans_list:
    x.append(i[0:4])

for i in cars_list:
    y.append(i[4])


myMachine = tree.DecisionTreeClassifier()
myMachine = myMachine.fit(x, y)

model = input('enter your car model\nfor example :X4 :').strip()
place = input('enter your place to persian\nfor example :تهران :').strip()
output = input('enter car output\nfor example :14,000 :').strip()
year = input('enter production year\nfor example :2013 :').strip()
car_details = [model, place, output, year]
reverse = preprocessing.LabelEncoder()
reverse = reverse.fit(car_details)
car_details = reverse.transform(car_details)
new_data = [car_details]
answer = myMachine.predict(new_data)
print('your car worth {} tomans'.format(answer[0]))


cursor.close()
cnx.close()
