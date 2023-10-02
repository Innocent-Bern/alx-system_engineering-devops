# make changes to configuration file

include stdlib

file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	PasswordAuthenication no',
  replace => true,
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	IdentityFile ~/.ssh/school',
  replace => true,
}
