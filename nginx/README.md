<!-- SSL - Certbot -->
https://mindsers.blog/post/https-using-nginx-certbot-docker/

<!-- Commands: -->
<!-- Dry run -->
sudo docker-compose run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ --dry-run -d moodalarm.com

<!-- Generate certificates -->
sudo docker-compose run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ -d moodalarm.com