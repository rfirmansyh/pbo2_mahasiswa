import mysql.connector
from mysql.connector import Error as MysqlError

class Database:
    def __init__(self):
        self.db = None
        self.stmt = None
        try:
            self.db = mysql.connector\
                      .connect(host='localhost',
                               database='db_praktikum_pbo_mahasiswa',
                               user='root',
                               password='')
            if self.db.is_connected():
                db_info = self.db.get_server_info()
                print("Berhasil Terhubung deng core ", db_info)
                self.stmt = self.db.cursor()
                self.stmt.execute("select database();")
                record = self.fetch()
                # print("You're connected to core: ", record)
        except MysqlError as error:
            print("Koneksi Error : tidak bisa terkoneksi dengan core mysql ", error)

    def set_query(self, string_query, params = None):
        self.stmt.execute(string_query, params)
        return self

    def execute(self):
        self.db.commit()
        return self

    def fetch(self):
        return self.stmt.fetchone()

    def fetchall(self):
        return self.stmt.fetchall()

    def get_tablecolumn(self, tableName = ""):
        self.set_query("SELECT * FROM %s LIMIT 1;"%(tableName))
        self.fetch()
        return [i[0] for i in self.stmt.description]

    def get_rowcount(self):
        return self.stmt.rowcount

    def closeconn(self):
        if self.db.is_connected():
            self.execute.close()
            self.db.close()
            print("Koneksi core ditutup")

# instance class database
# db = Database();
# val = ("182410102056", "Denta", "Teknologi Informasi")
# if ( db.set_query("INSERT INTO mahasiswa (nim, nama, prodi) VALUES (%s, %s, %s)", val)\
#         .execute()\
#         .get_rowcount() > 0 ):
#     print("Ada data yang ditambahkan")


#
# # tes lihat semua data : CRUD (Read)
# db.set_query(string_query="select * from mahasiswa")
# print(db.get_tablecolumn())
# print("Hasil :", db.fetchall())
#
# # tes tambah data : CRUD (Create)
# val = ("182410102080", "Gilang", "Teknologi Informasi")
# print(db.set_query("INSERT INTO mahasiswa (nim, nama, prodi) VALUES (%s, %s, %s)", val)\
#         .execute()\
#         .get_rowcount())
# db.execute()
# db.get_rowcount()
