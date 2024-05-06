#install Nginx in a server and configure it
exec {'configure':
  provider => shell,
  command  => 'sudo apt-get -y update; sudo apt-get -y install nginx',
}

file_line { 'red':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
