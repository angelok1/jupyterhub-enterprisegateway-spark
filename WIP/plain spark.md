plain spark

ssh -i .ssh/datastax.pem ubuntu@ec2-18-209-213-144.compute-1.amazonaws.com

sudo apt-get update

sudo apt-get install openjdk-8-jdk

sudo apt-get install scala

sudo apt-get install git

wget http://ftp.naz.com/apache/spark/spark-2.3.2/spark-2.3.2-bin-hadoop2.7.tgz

tar -xvf spark-2.3.2-bin-hadoop2.7.tgz

sudo mv spark-2.3.2-bin-hadoop2.7 /usr/local/spark

sudo apt install python2.7 python-pip


--on spark master or any DSE node

wget http://mirrors.sonic.net/apache/incubator/livy/0.5.0-incubating/livy-0.5.0-incubating-bin.zip

sudo apt-get install unzip

unzip livy-0.5.0-incubating-bin.zip 

sudo vim /etc/environment

SPARK_HOME=/usr/local/spark
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
PATH="$SPARK_HOME/bin:$JAVA_HOME:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"

mkdir livy-0.5.0-incubating-bin/logs

livy-0.5.0-incubating-bin/bin/livy-server start


--end server



--begin jupyterhub server

ssh -i .ssh/datastax.pem ubuntu@ec2-34-207-80-211.compute-1.amazonaws.com

sudo apt-get update

sudo apt-get install openjdk-8-jdk

wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh

bash Anaconda3-5.3.0-Linux-x86_64.sh

source /home/ubuntu/anaconda3/etc/profile.d/conda.sh

conda install -c conda-forge jupyterhub

conda install notebook

conda install -c anaconda jupyter 

sudo apt-get install libkrb5-dev

sudo -H pip install sparkmagic


--conda install -c conda-forge sparkmagic 

pip show sparkmagic

cd /home/ubuntu/.local/lib/python2.7/site-packages

sudo jupyter-kernelspec install sparkmagic/kernels/sparkkernel
sudo jupyter-kernelspec install sparkmagic/kernels/pysparkkernel
sudo jupyter-kernelspec install sparkmagic/kernels/pyspark3kernel
sudo jupyter-kernelspec install sparkmagic/kernels/sparkrkernel

jupyter serverextension enable --py sparkmagic

--sudo apt install jupyter-core

conda install -c anaconda ipywidgets

conda install -c anaconda widgetsnbextension 

conda install -c conda-forge jupyter_nbextensions_configurator

sudo jupyter nbextension enable --py widgetsnbextension --sys-prefix

pip install mleap

start jupyterhub:
sudo jupyterhub
