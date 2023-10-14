0x11. What happens when you type google.com in your browser and press Enter
Post cover:

DNS request
TCP/IP
Firewall
HTTPS/SSL
Load-balancer
Web server
Application server
Database

The blog post explains that DNS resolves www.google.com to another hostname or IP address, the request is reaching the server IP on port HTTPS 443, the traffic is encrypted using HTTPS/SSL certificate

The request is answered by a web server serving the page, the request is distributed by the load-balancer to a web server

the request is passing through the firewall that accepts traffic onport TCP/443
the application server will generate the page and queries the database to gather necessary data