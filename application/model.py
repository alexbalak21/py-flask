from flaskext.mysql import MySQL
from app import app

mysql = MySQL()
mysql.init_app(app)


def test_conn():
    try:
        connect = mysql.connect()
        connect.cursor()
        return 'Success'
    except:
        return 'Failed'


def test_create():
    try:
        connect = mysql.connect()
        cursor = connect.cursor()
        qry = """INSERT INTO notes (content) VALUES (%s);"""
        note = 'Note Production Working'
        cursor.execute(qry, (note,))
        connect.commit()
        connect.close()
        return 'Added to db'
    except:
        return 'Failed to add to db.'
