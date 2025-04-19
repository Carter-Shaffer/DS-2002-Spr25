#!/bin/bash

/usr/bin/apt update -y
/usr/bin/apt upgrade -y

/usr/bin/apt install -y python3 python3-pip git nginx

/usr/bin/systemctl enable nginx
/usr/bin/systemctl start nginx