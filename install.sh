sudo apt install virtualenv
virtualenv -p python3 env
. env/bin/activate
pip install -r req.txt
touch .env
echo 'DATABASE_HOST="your_localhost"
DATABASE_USER="your_user"
DATABASE_PASSWORD="your_pass"
DATABASE_NAME="your_dbname"' > .env
export FLASK_APP=app.py
export FLASK_ENV=development
flask new