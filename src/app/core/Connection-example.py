import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector\
                      .connect(host='localhost',
                               database='db_praktikum_pbo_mahasiswa',
                               user='root',
                               password='')
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Berhasil Terhubung deng core ", db_info)
        cursor = connection.cursor()
        cursor.execute("select * from mahasiswa")
        record = cursor.fetchone()
        print("You're connected to db: ", record)
except Error as e:
    print("Koneksi Error : tidak bisa terkoneksi dengan core mysql ", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Koneksi core ditutup")