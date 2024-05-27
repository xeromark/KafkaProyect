Info extraida de: https://github.com/Naikelin/async-events-kafka/tree/main/1%20-%20Setups%20and%20basics/3%20-%20Basics
kafka-python: https://kafka-python.readthedocs.io/en/master/usage.html#kafkaconsumer


Para levantar los requerimientos de python en docker:

docker build -t dockerfile .

Comandos de docker:

docker run --name kafka bitnami/kafka:latest		// correr kafka
docker compose up
docker exec -it Kafka bash      

docker rmi -f $(docker images -q)       //Borrar todos las imagenes


Comandos de Kafka:

kafka-topics.sh --bootstrap-server Kafka:9092 --create --topic pedidos  
kafka-topics.sh --describe --bootstrap-server Kafka:9092 --topic pedidos    // Describir topico
kafka-topics.sh --list --bootstrap-server Kafka:9092                    //lista de topicos
kafka-consumer-groups.sh --bootstrap-server Kafka:9092 --list   //Lista de grupos

kafka-console-consumer.sh --bootstrap-server Kafka:9092 --topic pedidos  //crear consumer con canal en pedidos
kafka-console-producer.sh --bootstrap-server Kafka:9092 --topic pedidos  //crear producer con canal en pedidos

kafka-topics.sh --bootstrap-server localhost:9092 --alter --topic pedidos --config retention.bytes=50

