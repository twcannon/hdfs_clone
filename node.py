import rpyc
import os
import uuid

from rpyc.utils.server import ThreadedServer

TEMP_DIR="/tmp/noce/"

class NodeService(rpyc.Service):
    blocks = {}

    # def put(self,block_uuid,data,noces):
    #     ## open and write the block
    #         self.send(block_uuid,data,noces)


    # def get(self,block_uuid):
    #     return f.read()   

    # def send(self,block_uuid,data,noces):
    #     ## here we need to send the put 
    #     ## data to the appropriate nodes

    # def delete_block(self,uuid):
    #     ## here we need to delete the block

if __name__ == "__main__":
    if not os.path.isdir(TEMP_DIR): os.mkdir(TEMP_DIR)
    thread = ThreadedServer(NodeService, port = 8888)
    thread.start()