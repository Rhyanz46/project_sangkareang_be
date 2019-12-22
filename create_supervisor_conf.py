import os

folder_supervisor = "/etc/supervisor/conf.d"
config = '[program:be_sangkareang]' \
         '\ndirectory={}' \
         '\ncommand={}/env/bin/gunicorn -w 4 wsgi:app -b localhost:9000' \
         '\nautostart=true' \
         '\nautorestart=true\n'.format(os.getcwd(), os.getcwd())

if os.path.isdir(folder_supervisor):
    f = open(folder_supervisor + "/be_sangkareang.conf", "w")
    f.write(config)
    f.close()
