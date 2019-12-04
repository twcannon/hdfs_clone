import rpyc
import uuid
import os

from rpyc.utils.server import ThreadedServer

port = 8888

DATA_DIR="/tmp/node/"

print("\nRunning node on port: "+str(port))
print("\n----------------------------")

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
 
    def forward(self,block_uuid,data,nodes):
        print(str(port)+": forwaring to:")
        print(block_uuid, nodes)
        node=nodes[0]
        nodes=nodes[1:]
        host,port=node

        conn=rpyc.connect(host,port=port)
        node = conn.root.Minion()
        node.put(block_uuid,data,nodes)


if __name__ == "__main__":
    if not os.path.isdir(DATA_DIR): os.mkdir(DATA_DIR)
    thread = ThreadedServer(NodeService, port = 8888)
    thread.start()