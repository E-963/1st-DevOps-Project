# Intiallization

> Step 1: Clone the Repository: (<https://github.com/E-963/ToDoList-DEPI-Project/tree/main>)
> Step2: Bash Command for Creat a Virtual Environment

1. python -m venv venv
2. pip install virtualenv
3. source venv/bin/activate
4. sudo install pip
5. pip install flask
6. pip install gunicorn
7. pip install pytest

## HTML. INDEX

 Create Templates file

## Install requirements

 pip install -r requirements.txt

## Run App

python3  main.py

## Production

gunicorn wsgi

## **Testing**

pytest

## GITHUB commands

## - Run

  git config --global user.email "<you@example.com>"
  git config --global user.name "Your Name"
  to set your account's default identity.

## - for add updates to the repository

    git Add .

    git commit -m "comment"
    
    git push
    
    git pull
    
    git status   #for check the last status on repo.

*** docker_ec2_watchtower_demo

    Create an EC2 Instance (t3.medium, ubuntu image, firewalll allows http from anywhere)

    Login to the instance and install docker

    sudo apt update && sudo apt install docker.io
    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker
    # Logout and relogin to the machine
    docker run hello-world # test docker installation
    Run an application

    docker run -itd --name app_container -p80:8080 sh3b0/app_python
    Check the status of the app on http://<ec2_public_dns_name>

    Common Issue:

    AppArmor may prevent watchtower from sending a SIGTERM signal to the containers. Either make a configuration for apparmor (at /etc/apparmor.d/docker) that allows such capability, or uninstall apparmor if you don't need it.

    sudo apt-get purge --auto-remove apparmor
    Run a watchtower that watches the image every 30 seconds. If the image is private, additional volume -v $HOME/.docker/config.json:/config.json can be used to allow watchtower to login and monitor the image.

    docker run -d \
    --name watchtower \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower app_container --debug --interval 30
    Check watchtower logs

    docker logs -f watchtower
    Rebuild and publish the app

    docker build -t sh3b0/app_python .
    docker login
    docker push sh3b0/app_python --all-tags
    Recheck the status of the app
