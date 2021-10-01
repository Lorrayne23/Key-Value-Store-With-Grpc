from concurrent import futures
import grpc
import kv_pb2
import kv_pb2_grpc


fake_db ={
      1:{

      }
}


class KV(kv_pb2_grpc.KVServicer):
    def get(self , request , context):
        key = request.key                 # user request key
        if key in fake_db.keys():

            key_value = fake_db.get(key)
            v = kv_pb2.Value(value=key_value,defined=True)
            return v
        else:
            return kv_pb2.Value(value=None,defined=False)

    # PUT key-value
    def put(self, request, context):
        key = int(request.key)
        value = request.value
        fake_db[key] = value
        return kv_pb2.Void()


     # GET all keys in the server
    def getAllKeys(self, request, context):
        return kv_pb2.StoredKeys(keys=fake_db.keys())



server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
kv_pb2_grpc.add_KVServicer_to_server(KV(), server)
server.add_insecure_port('localhost:9988')
server.start()
print(" Listening on 9988")
server.wait_for_termination()




