# Installs the Nginx package
package { 'nginx':
  ensure => installed,
}

# Updates the package lists
exec { 'apt-update':
  command => 'apt-get -y update',
  path    => ['/usr/bin', '/bin'],
  refreshonly => true,
}

# Sets up the custom "Hello World!" index page
file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  require => Package['nginx'],
}

# Adds a rewrite rule for /redirect_me
file { '/etc/nginx/sites-available/default':
  content => template('my_module/nginx_config.erb'),
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Starts the Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
