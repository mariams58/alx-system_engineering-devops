# This is file createsa file using puppet
file { '/tmp/school':
        group   => 'www-data',
        owner   => 'www-data',
        content => 'I love Puppet',
        mode    => '0744',
}
