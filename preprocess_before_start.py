# #!/bin/bash
#
# # Remove the app.json file
# rm -rf snapshot/app.json
#
# # MySQL commands
# mysql <<EOF
# DROP DATABASE IF EXISTS llm_account;
# DROP DATABASE IF EXISTS llm_game0001;
#
# CREATE DATABASE llm_game0001 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
#
# CREATE DATABASE llm_account DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
# EOF
#
from utils.mysql import Mysql
from app import App
from config import Config
import importlib, os




abs_path = os.path.dirname(os.path.realpath(__file__))

config = Config(os.path.join(abs_path, 'config', 'app.json'))
app = App()
db = Mysql(
    app,
    config.get_db_host('account'),
    config.get_db_port('account'),
    config.get_db_user('account'),
    config.get_db_pwd('account'),
    config.get_db_name('account'),
)
print(db.execute("DROP DATABASE IF EXISTS llm_account"))
print(db.execute("DROP DATABASE IF EXISTS llm_game0001"))
print(db.execute("CREATE DATABASE llm_game0001 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"))
print(db.execute("CREATE DATABASE llm_account DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"))
print(db.fetchall("SHOW DATABASES;"))
os.system("rm -rf snapshot/app.json")