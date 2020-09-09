from pymysql import install_as_MySQLdb

from scripts.orm import patch_model

install_as_MySQLdb()
patch_model()

