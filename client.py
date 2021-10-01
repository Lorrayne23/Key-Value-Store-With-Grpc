from __future__ import print_function
import kv_pb2
import kv_pb2_grpc
import grpc



args = {}

class ConfigError(Exception):
    pass

# ask a user a key and show the value
def getKey(stub):
    get_key = int(input(f'''\n  
    Input a key :\n Key:'''))

    response = stub.get(kv_pb2.Key(key=get_key))

    if response.defined:
        print(" '%s' = '%s'" % (get_key, response.value))
    else:
        print(" '%s': key not defined "% get_key)


# add key-value defined´s in user input
def putKeyValue(stub):
    put_key = int(input('''\n  
        Type a key  :\n
        Key :'''))

    put_value = int(input('''\n  
            Type a value :\n
            Value:'''))

    add_key_value = kv_pb2.NewKeyValue(key=put_key ,value = put_value)
    stub.put(add_key_value)
    print("key-value successfully added .")

# all keys in the server
def getKeys(stub):
    response = stub.getAllKeys(kv_pb2.Void())
    print("----------------------")
    print("List of keys :")
    for key in response.keys:
         print(key)

    print("----------------------")


# menu with options for user
def run():
    with grpc.insecure_channel('localhost:9988') as channel:
        def main_menu():
            stub = kv_pb2_grpc.KVStub(channel)
            op = int(input('''\n
                  MENU 
            --------------------
            1- Get key\n
            2- Put key-value\n
            3- All keys\n
            0- Close\n
            --------------------
            Your option :'''))
            print(op)
            if op == 1:
                getKey(stub=stub)
            elif op == 2:
                putKeyValue(stub=stub)
            elif  op == 3 :
                getKeys(stub=stub)
            elif op == 0:
                exit()
            else:
                print("Invalid option.Choose one of the list gaved.\n")
                main_menu()

        while True:
            try:
                main_menu()
            except ValueError:
                print("Input a number of the list gaved.\n")

if __name__ == '__main__':
    run()














