# Name Data Annotation
 

### Build and start the containers

``docker-compose up --build``

### If your want to rebuild the containers

```
# Remove any existing containers and images
docker-compose down --rmi all

# Build and start the containers
docker-compose up --build

```

```python
CREATE DATABASE namedb;
CREATE USER noyon WITH PASSWORD '1234';
GRANT ALL PRIVILEGES ON DATABASE namedb TO noyon;
```