
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






## Deployment

To Run This Project Follow below steps

```bash
  ./start.sh
```


## Installation

Clone The Git Repo using git Clone

Install all the requirements using below command

```bash
pip install -r requirements.txt
```
Install Kafka From this URL ('https://kafka.apache.org/quickstart)

```bash
  npm install my-project
  cd my-project
```
    