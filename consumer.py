from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
import clickhouse_connect

session = False

from kafka import KafkaConsumer
from json import loads, dumps

Base = declarative_base()
# class NewTable(Base):
#     __tablename__ = 'ecomdata'
    
#     InvoiceNo = Column(Integer, primary_key=True)
#     StockCode = Column(int)
#     Description = Column(String)
#     Quantity = Column(int)
#     InvoiceDate = Column(Date)
#     UnitPrice = Column(float)
#     CustomerID = Column(int)
#     country = Column(String)


try:
    consumer = KafkaConsumer('mage-hack',
                             bootstrap_servers=['localhost:9092'],
                             value_deserializer=lambda x: loads(x.decode('utf-8')))
except Exception as e:
    print("An error occurred while initializing the Kafka consumer:", e)
    consumer = None


try:
    # conn_str = 'clickhouse://default:@c6ply0su3g.eu-west-1.aws.clickhouse.cloud/default?password=zHaWx7r_74kS9&user=default'
    # engine = create_engine(conn_str)
    # session = sessionmaker(bind=engine)()
    client = clickhouse_connect.get_client(host='c6ply0su3g.eu-west-1.aws.clickhouse.cloud', port=8443, username='default', password='zHaWx7r_74kS9')


    # NewTable.__table__.create(engine)
    client.command('''CREATE TABLE IF NOT EXISTS ecomdata (
                                                Id int,
						                        InvoiceNo String , 
                                                StockCode String,
                                                Description text,
                                                Quantity int,
                                                InvoiceDate timestamp,
                                                UnitPrice float,
                                                CustomerID String,
                                                country text,
                                                PRIMARY KEY (Id)
                                                );''')
    # client.commit()
    session = True
except Exception as e:
    print("An error occurred while initializing the ClickHouse session or creating the keyspace or table:", e)
    session = None


if consumer and session:
    message_id = 0
    for message in consumer:
        if (message.value):
            try:
                message_id += 1
                new_data = {'Id': message_id}
                new_data.update(message.value)
                
                final_data = new_data
                # print(final_data)
                query = f'''
                Insert into ecomdata (Id, InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, country)
                values({final_data.get('Id')}, '{final_data.get('InvoiceNo')}', '{final_data.get('StockCode')}', '{str(final_data.get('Description')).replace("'",'')}', {final_data.get('Quantity')}, '{final_data.get('InvoiceDate')}', {final_data.get('UnitPrice')}, '{final_data.get('CustomerID')}', '{final_data.get('country')}')
                '''
                client.command(query)
                # print(message_id)
                
            except Exception as e:
                print("An error occurred while inserting data into ClickHouse:", e)