# Kafka Stock Streamer

Produces stock data to a Kafka topic allowing it to be consumed by an app. Data 
points are grabbed for each day the stock market is open for the specified stock 
symbol between the start and end dates specified.

The producer pushes stock data to a topic, and the consumer reads this stock data, 
printing the data to the console. This can be expanded upon for more functionality 
in another application.

## Configuration

```
kafka:  
    server: Kafka Server  
    topic: Kafka topic to produce to / consume from  
stock:  
    symbol: Stock symbol to use  
    start_date: Start date in the format YYYY-MM-DD  
    end_date: End date in  the format YYYY-MM-DD  
data:  
    encoding: Data encoding, should be UTF-8  
```

## Data Format

Each data point represents 1 day

{'Open': Opening price, 'High': Max price, 'Low': Min price, 'Close': Closing price, 'Adj Close': Adjusted closing price, 'Volume': Volume}

## Sample Usage

```bash
docker-compose up -d
./producer.py
./consumer.py
```

## Sources

* Docker compose sourced from [Obsidian Dynamics Kafdrop repo](https://github.com/obsidiandynamics/kafdrop/blob/master/docker-compose/kafka-kafdrop/docker-compose.yaml)

