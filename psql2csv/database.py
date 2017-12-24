
class DataBase(object):
    """

    A class to store the psql connection

    Parameters
    ----------
    driver: connection
        The psql connection
    """

    psql = None

    def __init__(self, driver):
        self.psql = driver

    def execute(self, statement):
        """

        Executes statement without having to do all the cursor stuff
        
        Parameters
        ----------
        statement: str
            The statement to execute

        Returns
        -------
        cursor:
            The cursor that needs to be closed
        """

        cur = self.psql.cursor()
        cur.execute(statement)
        return cur

    def fetchall(self, statement):
        """

        Executes a fetchall for the statement
        
        Parameters
        ----------
        statement: str
            The statement to execute

        Returns
        -------
        list:
            A list of tuples, each representing a row of data
        """

        cur = self.psql.cursor()
        cur.execute(statement)
        res = cur.fetchall()
        cur.close()
        return res

