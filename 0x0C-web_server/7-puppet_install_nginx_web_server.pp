#install Nginx in a server and configure it
exec {'configure':
  provider => shell,
  command  => 'sudo apt-get -y update; sudo apt-get install nginx;
  echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html;
  sudo sed -i "s/server_name _ ;/server_name_;\n\t
  rewrite ^\/redirect_me rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default; sudo service nginx start',

}
