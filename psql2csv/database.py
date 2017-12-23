
class DataBase(object):
    psql = None

    def __init__(self, driver):
        self.psql = driver

    def execute(self, statement):
        cur = self.psql.cursor()
        cur.execute(statement)
        return cur

    def fetchall(self, statement):
        cur = self.psql.cursor()
        cur.execute(statement)
        res = cur.fetchall()
        cur.close()
        return res

