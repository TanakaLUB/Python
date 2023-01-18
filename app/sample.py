

import MySQLdb


class DBConection():

    def __init__(self):
        # Connect
        self.conn = MySQLdb.connect(
            user='root',
            passwd='nicyu00001',
            host='localhost',
            db='sample',
            charset='utf8'
        )

    def select(self):
        # Select
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM m_user")

        for rows in cursor:
            for row in rows:
                print(row)

        self.conn.close
