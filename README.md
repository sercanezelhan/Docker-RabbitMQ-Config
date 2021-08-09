# Docker-RabbitMQ-Config

Rabbitmq has removed some environments for docker with its latest update.
The list is in the link below.     
https://hub.docker.com/_/rabbitmq     
A sample docker application for Rabbitmq configuration and passwords.

rabbit_password_hashing_sha256.py = Python code that SHA256 hash the password with salting.
(This program; it is only used to hash the password and give the hashed password to the password_hash field in definitions.json..!)

rabbitmq.conf = config file where RabbitMQ configurations are determined.

definitions.json = json file specifying users, roles and configurations.

docker-compose up -d --build

RabbitMQ UI = http://localhost:18005
Users = root:root 
      = admin:admin
