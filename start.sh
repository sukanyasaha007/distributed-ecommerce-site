docker run --rm -d -e MYSQL_ROOT_PASSWORD=pass -p 3325:3306 --name mysql1 mysql:5
docker run --rm -d -e MYSQL_ROOT_PASSWORD=pass -p 3326:3306 --name mysql2 mysql:5
docker run --rm -d -e MYSQL_ROOT_PASSWORD=pass -p 3327:3306 --name mysql3 mysql:5
docker run --rm -d -e MYSQL_ROOT_PASSWORD=pass -p 3328:3306 --name mysql4 mysql:5
docker run --rm -d -e MYSQL_ROOT_PASSWORD=pass -p 3329:3306 --name mysql5 mysql:5

docker run --name=flask -dt -v $(pwd):/app -p 5000:5000 python
#docker exec -it flask bash
cd grpc-server
docker run --name=grpc -dt -v $(pwd):/app -p 50051:50051 python
#docker exec -it grpc bash
