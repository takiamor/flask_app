from api_test  import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test_api'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)