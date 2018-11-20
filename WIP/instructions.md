instructions

ssh -i ".ssh/datastax.pem" ubuntu@ec2-18-234-76-191.compute-1.amazonaws.com

sudo apt update
sudo apt upgrade

sudo apt install openjdk-8-jdk

--install python and pip
sudo apt install python3-pip

/symlink python
sudo ln -s /usr/bin/python3 /usr/bin/python

--sudo apt-get install python-pip python-dev build-essential 

(spark 2.2+)
pip3 install pyspark


--set SPARK_HOME = ~/.local/lib/python2.7/site-packages/pyspark
sudo vim /etc/environment


SPARK_HOME=~/.local/lib/python3.6/site-packages/pyspark
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
PYSPARK_PYTHON=python3
KG_LIST_KERNELS=True
PATH="/home/ubuntu/.local/bin:/home/ubuntu/anaconda3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:$SPARK_HOME/bin:$JAVA_HOME"

source /etc/environment

sudo vim ~/.bashrc

test with pyspark (exit())


wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh

bash Anaconda3-5.3.0-Linux-x86_64.sh

source /home/ubuntu/anaconda3/etc/profile.d/conda.sh

sudo apt-get install gcc python-dev libkrb5-dev
pip3 install pywinrm[kerberos]

pip3 install --upgrade jupyter_enterprise_gateway


EG_REMOTE_HOSTS=ec2-18-234-76-191.compute-1.amazonaws.com



sudo apt-get install gcc python-dev libkrb5-dev
pip install pywinrm[kerberos]

pip3 install --upgrade jupyter_enterprise_gateway




none of this may be needed----
wget https://github.com/jupyter/enterprise_gateway/releases/download/v1.0.0/jupyter_enterprise_gateway_kernelspecs-1.0.0.tar.gz

SCALA_KERNEL_DIR="$(jupyter kernelspec list | grep -w "python3" | awk '{print $2}')"

KERNELS_FOLDER="$(dirname "${SCALA_KERNEL_DIR}")"

tar -zxvf jupyter_enterprise_gateway_kernelspecs-1.0.0.tar.gz --strip 1 --directory $KERNELS_FOLDER/spark_python_yarn_client/ spark_python_yarn_client/

----end

--kernels are here /home/ubuntu/.local/share/jupyter/kernels/python3
--find them with this command $(jupyter kernelspec list | grep -w "python3" | awk '{print $2}')


replace kernel.json

start: jupyter enterprisegateway --ip=0.0.0.0 --port_retries=0







jupyterhub: (doing this with kubernetes: https://zero-to-jupyterhub.readthedocs.io/en/stable/)

ssh -i ".ssh/datastax.pem" ubuntu@ec2-52-207-215-99.compute-1.amazonaws.com


sudo apt update

--sudo apt install openjdk-8-jdk

wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh

bash Anaconda3-5.3.0-Linux-x86_64.sh

source ~/.bashrc (the script above changes it)
--source /home/ubuntu/anaconda3/etc/profile.d/conda.sh

conda install -c conda-forge jupyterhub

sudo apt-get install nodejs
sudo apt-get install npm


conda install notebook


to test:

jupyterhub -h
configurable-http-proxy -h

jupyter serverextension list (to validate that extensions are on and jupyter is installed)

pip install --upgrade pip

pip install nb2kg


jupyter serverextension enable --py nb2kg --sys-prefix

jupyter serverextension list (nb2kg should now be in the list)


--scp -i .ssh/datastax.pem ubuntu@ec2-52-207-215-99.compute-1.amazonaws.com:jupyterhub_config.py .

sudo vim /etc/environment

KG_URL=http://ec2-18-234-76-191.compute-1.amazonaws.com:8888
KG_HTTP_USER=guest
KG_HTTP_PASS=guest-password
KG_REQUEST_TIMEOUT=30
KERNEL_USERNAME=${KG_HTTP_USER}
JUPYTER_CONFIG_DIR=/etc/jupyter
PATH="/home/ubuntu/anaconda3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"

source /etc/environment


sudo npm install -g configurable-http-proxy


--now add the admin user
sudo adduser hubadmin

sudo mkdir /etc/jupyter
sudo vim /etc/jupyter/jupyterhub_config.py (or touch)

sudo /home/ubuntu/anaconda3/bin/jupyterhub -f /etc/jupyter/jupyterhub_config.py


jupyter notebook --generate-config

jupyter_notebook_config.py (add handlers)


#copy the kernels over to the system-wide area
sudo mkdir /usr/local/share/jupyter
sudo mkdir /usr/local/share/jupyter/kernels
sudo cp /home/ubuntu/anaconda3/share/jupyter/kernels/python3 /usr/local/share/jupyter/kernels -r


conda install -c conda-forge nbserverproxy 




--ln -s /usr/local/bin/configurable-http-proxy /usr/bin/configurable-http-proxy











export KG_URL=http://ec2-18-234-76-191.compute-1.amazonaws.com:8888
export KG_HTTP_USER=guest
export KG_HTTP_PASS=guest-password
export KG_REQUEST_TIMEOUT=30
export KERNEL_USERNAME=${KG_HTTP_USER}
sudo jupyterhub \
  --NotebookApp.session_manager_class=nb2kg.managers.SessionManager \
  --NotebookApp.kernel_manager_class=nb2kg.managers.RemoteKernelManager \
  --NotebookApp.kernel_spec_manager_class=nb2kg.managers.RemoteKernelSpecManager


--pip3 install ipython

wget https://github.com/jupyter/enterprise_gateway/releases/download/v1.0.0/jupyter_enterprise_gateway_kernelspecs-1.0.0.tar.gz

SCALA_KERNEL_DIR="$(jupyter kernelspec list | grep -w "spark_scala" | awk '{print $2}')"

KERNELS_FOLDER="$(dirname "${SCALA_KERNEL_DIR}")"

tar -zxvf jupyter_enterprise_gateway_kernelspecs-1.0.0.tar.gz --strip 1 --directory $KERNELS_FOLDER/spark_python_yarn_cluster/ spark_python_yarn_cluster/

tar -zxvf jupyter_enterprise_gateway_kernelspecs-1.0.0.tar.gz --strip 1 --directory $KERNELS_FOLDER/spark_python_yarn_client/ spark_python_yarn_client/
