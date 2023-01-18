import MySQLdb
from infra.mUser import MUser


class DB():

    def __init__(self):
        # Connect
        self.conn = MySQLdb.connect(
            user='root',
            passwd='nicyu00001',
            host='localhost',
            db='sample',
            charset='utf8'
        )

    def select(self, id: str) -> MUser():
        # Select
        with self.conn.cursor() as cursor:

            sql = "SELECT * FROM m_user where user_id = '%s'" % id
            print(sql)
            cursor.execute(sql)

            muser = MUser()
            for rows in cursor:
                muser.user_id = rows[0]
                muser.password = rows[1]
                muser.user_name = rows[2]
                muser.birthday = rows[3]
                muser.age = rows[4]

            return muser


if __name__ == "__main__":
    db = DB()

    db.select(11111)
