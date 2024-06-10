# Creates a custom hader in an nginx server
#install Nginx in a server and configure it
exec {'configure':
  provider => shell,
  user     => 'root',
  command  => 'sudo apt-get -y update',
}

# Install Nginx
package {'nginx':
  ensure => installed,
}

# Custom header
file_line {'add_header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Serverd-By $hostname;'
  require => Package['nginx'],
  notify  => Service['nginx'],
}

#start service
service {'nginx':
  ensure    => 'running',
  enable    => true,
  require   => Package['nginx'],
  subscribe => File_line['add_header'],
}
