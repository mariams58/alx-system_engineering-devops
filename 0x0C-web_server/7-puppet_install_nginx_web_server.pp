#install Nginx in a server and configure it
exec {'configure':
  provider => shell,
  command  => 'sudo apt-get -y update',
}

# Install Nginx
package {'nginx':
  ensure => installed,
}

# Ensure hhtp listens at port 80
exec { 'allow_nginx_http':
  command => 'ufw allow "Nginx HTTP"',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => '/usr/sbin/ufw status | grep "Nginx HTTP"',
  require => Package['nginx'],
}

# Change www permission
exec { 'change permision':
  command => 'chmod -R 755 /var/www',
  path    => ['/usr/bin', '/usr/sbin'],
}

file_line { 'red':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
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
