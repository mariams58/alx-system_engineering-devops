#ssh configuration file using puppet manifest file

fileline { 'no password authentication':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true
}

fileline { 'identity file switch':
  ensure  => present,
  path    => 'etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true
}
