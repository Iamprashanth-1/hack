#!/bin/bash
# Download and extract Apache Kafka
# wget https://downloads.apache.org/kafka/3.3.2/kafka_2.12-3.3.2.tgz
# tar -xvf kafka_2.12-3.3.2.tgz


# # Install Java
# sudo yum install java-1.8.0-openjdk
cd ..
cd temp
# Go to the extracted Kafka directory
cd kafka_2.13-3.2.1


# Configure Kafka to use the public IP of your EC2 instance
# sudo nano config/server.properties 
#-->> Change "ADVERTISED_LISTENERS" to the public IP of the EC2 instance


# Start ZooKeeper
bin/zookeeper-server-start.sh config/zookeeper.properties & 

sleep 5 &

bin/kafka-server-start.sh config/server.properties 


# python3 /home/revos/mage-hack/producer.py &

# python3 /home/revos/mage-hack/consumer.py 


# Create a topic named "mage-hack"
# bin/kafka-topics.sh --create --topic mage-hack --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1


