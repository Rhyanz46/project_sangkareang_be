sudo apt install virtualenv
virtualenv -p python3 env
. env/bin/activate
pip install -r req.txt
export FLASK_APP=app.py
export FLASK_ENV=development
flask new
sudo python3 create_supervisor_conf.py
sudo supervisorctl reread
sudo service supervisor restart
echo "wait for 10 second"
sleep 10s
sudo supervisorctl status