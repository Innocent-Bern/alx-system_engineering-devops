# fix HTTP/1.0 500 Internal Server Error on Apache Server

exec {'replace':
    provider => shell,
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}