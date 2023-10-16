Task: 0. Block all incoming traffic :

install the ufw firewall and setup a few rules on web-01.
applied to web-01
Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
22 (SSH)
443 (HTTPS SSL)
80 (HTTP)

Task 1. Port forwarding
Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.
