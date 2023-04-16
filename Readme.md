
# Mage Hackathon

Hi, Team This is Prashanth below are the sections describe the flow.

I have Used These set of Tools

 -> SQL (OLAP) : ClickHouse (Since ClickHouse Provides 30 Days Free Trail)

 -> Ingestion : Apache-Kafka

 -> Visualization : Apache-SuperSet

I have Picked Sample Data of E-commerce Customer Data From Kaggle('https://www.kaggle.com/datasets/carrie1/ecommerce-data?resource=download')

I am using this Data as Real-Time data. I am Ingesting this data to Kafka Topic as as Producer.

I am Consuming the same data from Kafka Topic and exporting to ClickHouse. Currently I am not making any set of Transformations. If we want any set of Transformations we can add one layer and Transform and export data to ClickHouse.

## Visualization:

SuperSet Allows to Connect to ClickHouse I have created Visualizations in SuperSet Heads can look at the dashboard and make neccesary decisions.



## Current Architecture

![](https://github.com/Iamprashanth-1/hack/blob/main/images/arch.png)

## Actual Architecture

![](https://github.com/Iamprashanth-1/hack/blob/main/images/real-arch.png)



## Installation

Clone The Git Repo using git Clone

Install all the requirements using below command

```bash
pip install -r requirements.txt
```
Install Kafka From this URL ('https://kafka.apache.org/quickstart)


## Deployment

To Run This Project Follow below steps

Start The Zookeeper
```bash
  bin/zookeeper-server-start.sh config/zookeeper.properties 
```

Start the Kafka Server
```bash
  bin/kafka-server-start.sh config/server.properties 
```

If You haven't created a topic use below command
```bash
  bin/kafka-topics.sh --create --topic mage-hack --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1

```

Then run the Producer
```bash
  python3 producer.py
```

Then run the Consumer
```bash
  python3 consumer.py
```
