import pyodbc
from random import randint


def inicio():
    AltaTemperatura = -99
    BajaTemperatura = 99

    NombreCiudades = {"Madrid", "Barcelona", "Sevilla", "Malaga", "Cordoba", "Toledo", "Valencia", "Bilbao", "Salamanca",
                      "Palma", "Caceres", "Segovia", "Saragoça ", "Cuenca", "Alicante", "Las Palmas", "Avila", "Merida", "Granada", "Murcia"}
    ciudades = dict()
    for i in NombreCiudades:
        media_temperaturas = 0
        for j in range(0, 12):
            media_temperaturas += randint(-10, 40)
        ciudades[i] = media_temperaturas/12
        # Encontrar la(s) ciudad(es) con la temperatura media anual más alta
        if media_temperaturas/12 > AltaTemperatura:
            AltaTemperatura = media_temperaturas/12
        # Encontrar la(s) ciudad(es) con la temperatura media anual más baja
        if media_temperaturas/12 < BajaTemperatura:
            BajaTemperatura = media_temperaturas/12
    return ciudades


def connect():

    server = 'KEROTEMPEST\SQLEXPRESS'
    database = 'bikerentdb'
    username = 'developer'
    password = 'P4$$w0rd'

    # Conecction String
    driver = 'DRIVER={ODBC Driver 17 for SQL Server};'
    others = f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
    connection_string = '{}{}'.format(driver, others)
    con = pyodbc.connect(connection_string)
    cur = con.cursor()
    res = cur.execute("SELECT @@VERSION AS 'SQL Server Version Details'")
    for r in res:
        print(r[0])
    return (con, cur)


def insert(con, cur, city, temp):
    # read values to be inserted
    # create the Insert query
    sql = f"""INSERT INTO Ciudades (Nombre, Temperatura) 
    VALUES ('{city}','{temp}')"""

    # create list of values typed from user to insert in customer table
    # Execute query with values
    # Do the insert
    cur.execute(sql)
    # commit the transaction
    con.commit()
    # commit for permanent storage in database
    con.commit()
    # display success message
    print(cur.rowcount, "Record inserted.")


def insertStats(con, cur, MaxTempCity, MinTempCity, MaxTemp, MinTemp):
    # read values to be inserted
    # create the Insert query
    sql = f"""INSERT INTO Stats (MaxTempCity, MinTempCity, MaxTemp, MinTemp) 
    VALUES ('{MaxTempCity}','{MinTempCity}', '{MaxTemp}', '{MinTemp}')"""

    # create list of values typed from user to insert in customer table
    # Execute query with values
    # Do the insert
    cur.execute(sql)
    # commit the transaction
    con.commit()
    # commit for permanent storage in database
    con.commit()
    # display success message
    print(cur.rowcount, "Record inserted.")


def display(cur):
    # Execute SELECT statement
    cur.execute("SELECT * FROM Ciudades")
    # Fetch all records from table
    res = cur.fetchall()
    # print
    linea = '-'*80
    citydict = {}
    for x in res:
        citydict[x[1]] = x[2]
        # thisdict.update(f"ID: {x[0]} name {x[1]} temp {x[2]}")
    return citydict


def truncate(con, cur):
    # Create Truncate Query
    sql = (f"TRUNCATE TABLE Ciudades")
    # execute Truncate query
    cur.execute(sql)
    # commit changes to DB
    con.commit()
    # display success message
    print(cur.rowcount, "Records truncated.")


def stats(cityDict):
    AltaTemperatura = -99
    BajaTemperatura = 99
    CityAltaTemperatura = ""
    CityBajaTemperatura = ""

    for k, v, in cityDict.items():
        # Encontrar la(s) ciudad(es) con la temperatura media anual más alta
        if v > AltaTemperatura:
            AltaTemperatura = v
            CityAltaTemperatura = k
        # Encontrar la(s) ciudad(es) con la temperatura media anual más baja
        if v < BajaTemperatura:
            BajaTemperatura = v
            CityBajaTemperatura = k
    return (CityAltaTemperatura, AltaTemperatura, CityBajaTemperatura, BajaTemperatura)


con, cur = connect()

while True:
    # menu options
    print("1. Delete all data, generate new data and store it")
    print("2. Show the info from Ciudades")
    print("3. Insert Stats in Database")
    print("4. EXIT")
    # ask user to enter what he wants to do
    try:
        ch = int(input("Enter Your choice:"))
        # call relevant fucntions defined above
        if (ch == 1):
            truncate(con, cur)
            Inicio = inicio()
            for k, v in Inicio.items():
                insert(con, cur, k, v)
            print("Data generated")

        if (ch == 2):
            ciudadDiccionario = display(cur)
            if not ciudadDiccionario:
                ciudadDiccionario = inicio()
                for k, v in ciudadDiccionario.items():
                    insert(con, cur, k, v)
                print("Data doesn't exist. Generating new data")
            print(ciudadDiccionario)
            CityAltaTemperatura, AltaTemperatura, CityBajaTemperatura, BajaTemperatura = stats(
                ciudadDiccionario)
            print(
                f"La ciudad con la temperatura más alta es: {CityAltaTemperatura}{AltaTemperatura}")
            print(
                f"La ciudad con la temperatura más baja es: {CityBajaTemperatura}{BajaTemperatura}")

        if (ch == 3):
            ciudadDiccionario = display(cur)
            if not ciudadDiccionario:
                ciudadDiccionario = inicio()
                for k, v in ciudadDiccionario.items():
                    insert(con, cur, k, v)
                print("Data doesn't exist. Generating new data")
            CityAltaTemperatura, AltaTemperatura, CityBajaTemperatura, BajaTemperatura = stats(
                ciudadDiccionario)
            insertStats(con, cur, CityAltaTemperatura,
                        CityBajaTemperatura, AltaTemperatura, BajaTemperatura)

        if (ch == 4):
            break
    except:
        print('Entre una selección válida')
