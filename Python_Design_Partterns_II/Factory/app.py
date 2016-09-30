from Python_Design_Partterns_II.Factory.connection_factory import ConnectionFactory

connection = ConnectionFactory.get_connection()
cursor = connection.cursor()

cursor.execute('SELECT * FROM cursos')

for each_linha in cursor:
    print(each_linha)

connection.close