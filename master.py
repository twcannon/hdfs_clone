import rpyc
import pickle
import uuid
import os
import signal
import sys

from rpyc.utils.server import ThreadedServer


def int_handler(signal, frame):
    pickle.dump((MasterServer.file_table,MasterServer.block_mapping),open('file_server.img','wb'))
    sys.exit(0)

def get_config():
    MasterServer.block_size = 10
    MasterServer.dup = 1
    nodes = ['1:153.9.254.197:8888']
    print("\nStarting master with:")
    print("block_size: "+str(MasterServer.block_size))
    print("duplication number: "+str(MasterServer.dup))
    print("number of nodes: "+str(len(nodes)))
    print("\n-------------------------------")
    # nodes saved in format numerical_id:host:port
    for m in nodes:
        id,host,port=m.split(":")
        MasterServer.nodes[id]=(host,port)

    if os.path.isfile('file_server.img'):
        MasterServer.file_table,MasterServer.block_mapping = pickle.load(open('file_server.img','rb'))

class MasterServer(rpyc.Service):
    file_table = {}
    block_mapping = {}
    nodes = {}

    block_size = 0
    dup = 0

    def read(self,fname):
        mapping = self.__class__.file_table[fname]
        return mapping

    def write(self,dest,size):
        self.__class__.file_table[dest]=[]
        num_blocks = self.calc_num_blocks(size)
        blocks = self.alloc_blocks(dest,num_blocks)
        return blocks

    def get_file_table_entry(self,fname):
        if fname in self.__class__.file_table:
            return self.__class__.file_table[fname]
        else:
            return None

    def get_block_size(self):
        return self.__class__.block_size

    def get_nodes(self):
        return self.__class__.nodes

    def get_num_blocks(self,size):
        return int(math.ceil(float(size)/self.__class__.block_size))

    def allocate(self,dest,num_blocks):
        blocks = []
        for i in range(0,num):
            block_uuid = uuid.uuid1()
            nodes_ids = random.sample(self.__class__.nodes.keys(),self.__class__.dup)
            blocks.append((block_uuid,nodes_ids))
            self.__class__.file_table[dest].append((block_uuid,nodes_ids))
        return blocks


if __name__ == "__main__":
      get_config()
      signal.signal(signal.SIGINT,int_handler)
      thread = ThreadedServer(MasterServer, port = 2131)
      thread.start()