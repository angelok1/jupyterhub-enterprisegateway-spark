ssh -i ".ssh/datastax.pem" ubuntu@ec2-18-233-93-145.compute-1.amazonaws.com

sudo apt update
sudo apt upgrade

sudo apt install openjdk-8-jdk
sudo apt install python3-pip

wget http://ftp.naz.com/apache/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz

sudo tar -xvf spark-2.4.0-bin-hadoop2.7.tgz -C /opt

sudo ln -s /opt/spark-2.4.0-bin-hadoop2.7 /opt/spark
sudo ln -s /usr/bin/python3 /usr/bin/python

#out jupyter data dir (kernels)
sudo mkdir /usr/local/share/jupyter
sudo mkdir /usr/local/share/jupyter/kernels

sudo vim /etc/environment

SPARK_HOME=/opt/spark
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
PYSPARK_PYTHON=python3
KG_LIST_KERNELS=True
JUPYTER_DATA_DIR=/usr/local/share/jupyter
PATH="$SPARK_HOME/bin:$JAVA_HOME:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

source /etc/environment

test with pyspark (exit())

sudo apt install jupyter-core
sudo apt install jupyter

pip3 install jupyter
pip3 install notebook


jupyter --version
jupyter kernelspec list

copy over spark_python_standalone to sudo mkdir /usr/local/share/jupyter/kernels

sudo chmod +x /usr/local/share/jupyter/kernels/spark_python_standalone/bin/run.sh

jupyter kernelspec list should show: spark_python_standalone    /usr/local/share/jupyter/kernels/spark_python_standalone

sudo apt-get install gcc python-dev libkrb5-dev
pip3 install pywinrm[kerberos]
pip3 install --upgrade jupyter_enterprise_gateway

jupyter enterprisegateway --ip=0.0.0.0 --port_retries=0