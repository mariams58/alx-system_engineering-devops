# Fixes the incorect php extention file name

exec { 'fix-apache':
  command => 'cp /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  path    => '/usr/local/bin/:/bin/'
}
