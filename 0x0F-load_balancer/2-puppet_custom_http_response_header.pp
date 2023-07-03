# a Puppet script that it configures a brand new Ubuntu machine to the requirements asked in this task

$nginx_package = 'nginx'

exec { 'update_package_lists':
  command => 'apt-get update',
  path    => '/usr/bin',
  refreshonly => true,
}

package { $nginx_package:
  ensure => installed,
  require => Exec['update_package_lists'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By \"$hostname\";
        root   /var/www/html;
        index  index.html index.htm;
    
        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4/;
        }
    
        error_page 404 /404.html;
        location /404 {
            root /var/www/html;
            internal;
        }
    }
  ",
  require => Package[$nginx_package],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package[$nginx_package],
}
