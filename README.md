# Django-AngularJs-Fibonacci Series Generator using Django-restframework - AWS ngnix configuration

#### Create ubuntu instance - add http and https rules in the configurationgroups

#### Setting up the instance
```
sudo apt-get install python-pip
```
```
pip install virtualenvwrapper
```
```
source .local/bin/virtualenvwrapper.sh
```

```
export WORKON_HOME=~/.virtualenvs
```

```
source .bashrc
```

```
mkvirtualenv myenv
```


#### Setting up the project:


```
Git-clone the project;
```


To continue with necessary installations  
```
cd project directorty
```

```
pip install -r requirements.txt;
```

#### I have done the wsgi setup and ssl for extra credits

#### Setting up wsgi server in AWS(gunicorn):

```
pip install nginx;
```

add the web-configuration at /etc/nginx/sites-enabled/nginx.conf;

server {
    # the port your site will be served on

    listen      80;

    # the domain name it will serve for

    server_name .domain.tld yourIp;   # substitute by your FQDN and machine's IP address

    charset     utf-8;

    #Max upload size

    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {
        alias /var/www/path/to/your/project/media;      # your Django project's media files
    }


    location /static {
        alias /var/www/path/to/your/project/static;     # your Django project's static files
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}


delete the default config file in this directory;
```
pip install gunicorn;
```
```
sudo /etc/init.d/nginx start;
```

update settings.py available hosts with aws public:ip ;

```
gunicorn --bind 0.0.0.0:8000 nameofyourapp.wsgi in the project directory;
```

#### Https-setup
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/cert.key -out /etc/nginx/cert.crt;
```

update the nginx.conf;
from the reference below and give the certificate path /etc/nginx/cert.crt

```
sudo /etc/init.d/nginx reload/restart;
```

```
gunicorn --bind 0.0.0.0:8000 nameofyourapp.wsgi in the project directory;
```


reference
https://thepracticalsysadmin.com/nginx-self-signed-cert/


HOW TO USE IT?

Click on the website Link

Click on 'ADVANCED' and then click on 'Proceed to 18.221.142.31 (unsafe)'

Give input between 1-20

Click on Calculate button or enter

The application will display the fibonocci series till nth number.

(Extra-Credits)- Application runs on wsgi(gunicorn) server and Https -self-certified

