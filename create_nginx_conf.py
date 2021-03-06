import os

folder_nginx = "/etc/nginx/sites-available"
config = 'server {' \
         '\n\tlisten\t5000;' \
         '\n\tserver_name localhost;' \
         '\n\tlocation / {' \
         '\n\t\tproxy_pass http://localhost:9000;' \
         '\n\t}' \
         '\n}\n'

if os.path.isdir(folder_nginx):
    try:
        nginx_result = folder_nginx + "/default"
        f = open(nginx_result, "w")
        f.write(config)
        f.close()
        print("success to write " + nginx_result)
    except:
        print("error to write " + nginx_result)
else:
    print("nginx for this service is not running")
    print("make sure you nginx is installed...!!!")
