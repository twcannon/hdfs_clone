import rpyc
import os
import uuid

from rpyc.utils.server import ThreadedServer

TEMP_DIR="/tmp/noce/"

class NodeService(rpyc.Service):
    blocks = {}

    def put(self,block_uuid,data,nodes):
        with open(DATA_DIR+str(block_uuid),'w') as f:
            f.write(data)
        if len(nodes)>0:
            self.forward(block_uuid,data,nodes)


    def get(self,block_uuid):
        block_addr=DATA_DIR+str(block_uuid)
        if not os.path.isfile(block_addr):
            return None
        with open(block_addr) as f:
            return f.read()   

    def send(self,block_uuid,data,nodes):
        print("8888: forwaring to:")
        print(block_uuid, nodes)
        node=nodes[0]
        nodes=nodes[1:]
        host,port=node
        conn=rpyc.connect(host,port=port)
        node = conn.root.Minion()
        node.put(block_uuid,data,nodes)

    # def delete_block(self,uuid):
    #     ## here we need to delete the block

if __name__ == "__main__":
    if not os.path.isdir(TEMP_DIR): os.mkdir(TEMP_DIR)
    thread = ThreadedServer(NodeService, port = 8888)
    thread.start()