instructions2

ssh -i ".ssh/datastax.pem" ubuntu@ec2-52-90-36-117.compute-1.amazonaws.com

sudo apt update
sudo apt-get install nodejs
sudo apt-get install npm

sudo npm install -g configurable-http-proxy

sudo apt install python3-pip

#python3 -m pip install jupyterhub
sudo -H pip3 install jupyterhub
#python3 -m pip install --upgrade notebook
sudo -H pip3 install notebook
#python3 -m pip install nb2kg
sudo -H pip3 install nb2kg

jupyterhub -h
configurable-http-proxy -h





sudo vim /etc/environment

KG_URL=http://172.31.75.79:8888
#KG_HTTP_USER=guest
#KG_HTTP_PASS=guest-password
KG_REQUEST_TIMEOUT=30
VALIDATE_KG_CERT=no
#KERNEL_USERNAME=${KG_HTTP_USER}
JUPYTER_CONFIG_DIR=/etc/jupyter
#PATH="/home/ubuntu/anaconda3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"

source /etc/environment

sudo adduser hubadmin

sudo mkdir /etc/jupyter
sudo vim /etc/jupyter/jupyterhub_config.py (or touch)

sudo vim /etc/jupyter/jupyter_notebook_config.py

sudo jupyter serverextension enable --py nb2kg --sys-prefix
jupyter serverextension list

sudo KG_URL=http://172.31.75.79:8888 jupyterhub -f /etc/jupyter/jupyterhub_config.py --debug

sudo vim /usr/local/lib/python3.6/dist-packages/nb2kg/managers.py


so the KG
sudo adduser hubadmin


--ports in use: ss -plnt