#!/usr/bin/env bash
#Bash script to set up my web server

#Install nginx only if not installed
if ! dpkg -s nginx > /dev/null; then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi


#Create a directory with parents as needed
sudo mkdir -p '/data/web_static/releases/test/'
sudo mkdir -p '/data/web_static/shared/'


#Create Fake html file for testing
#printf "Hello Web Static\n" | sudo tee '/data/web_static/releases/test/index.html' > /dev/null
printf "<html>\n\t<head>\n\t</head>\n\t\t<body>\n\t\t\tHolberton School\n\t\t</body>\n</html>\n" | sudo tee '/data/web_static/releases/test/index.html' > /dev/null

#Create a symbolic link to a the test folder
sudo ln -sf '/data/web_static/releases/test/' '/data/web_static/current'

#Change ownership of the directory Recursively to user and group ubunt
sudo chown -R ubuntu:ubuntu '/data'

#Change the nginx.conf file and add server block
OLD_HTTP="http {"
NEW_HTTP="http {\n\tserver {\n\t\tlocation \/hbnb_static {\n\t\t\talias \/data\/web_static\/current\/;\n\t\t\t}\n\t}"

#Replace the old http with new server header
sudo sed -i "s/$OLD_HTTP/$NEW_HTTP/" /etc/nginx/nginx.conf

#Replace sites-available if present
sudo sed -i 's/include \/etc\/nginx\/sites-enabled\*/#include \/etc\/nginx\/sites-enabled/' /etc/nginx/nginx.conf

#Restart nginx command
sudo service nginx restart
