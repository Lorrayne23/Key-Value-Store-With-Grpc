### Key-Value store in memory using gRPC
This work shows a use of the gRPC protocol to allow the client to add a key and a value, fetch a key and view all keys on the server.

The project was developed in the python programming language.

#### Main actions key-value :

- put(key, value)

- get(key) : value

- getAllKeys() : Key[]



#### Requirements :
- Python 2.7, or Python 3.4 or higher.

- Install gRPC :


##### Install gRPC tools in the terminal :
```
$ pip install grpcio
$ pip install grpcio-tools
```

#### Operating instruction :
##### From the terminal, run the server:
```
$ python server.py
```
 
##### After the client :

```
$ python client.py
```

