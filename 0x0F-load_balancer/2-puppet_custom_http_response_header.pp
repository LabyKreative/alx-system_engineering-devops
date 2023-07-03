# a Puppet script that it configures a brand new Ubuntu machine to the requirements asked in this task

exec {'update_package_list':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

exec { 'header_display':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx service':
  provider => shell,
  command  => 'sudo service nginx restart',
}
