# Install and configure an Nginx server using Puppet instead of Bash

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/LabyKreative permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
