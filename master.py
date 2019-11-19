import rpyc
import pickle

from rpyc.utils.server import ThreadedServer

def int_handler(signal, frame):
    pickle.dump((MasterServer.file_table,MasterServer.block_mapping),open('file_server.img','wb'))
    sys.exit(0)

def get_config():
    MasterServer.block_size = 10
    MasterServer.dup = 2
    nodes = [os.environ['NODE1'],os.environ['NODE2']]
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

    # def read(self,fname):
    #       return mapping

    # def write(self,dest,size):
    #     return blocks

    # def get_file_table_entry(self,fname):
    #     return None

    # def get_block_size(self):
    #     return self.__class__.block_size

    # def get_nodes(self):
    #     return self.__class__.nodes

    # def get_num_blocks(self,size):
    #     return int(math.ceil(float(size)/self.__class__.block_size))

    # def allocate(self,dest,num_blocks):
    #     return blocks


if __name__ == "__main__":
      get_config()
      signal.signal(signal.SIGINT,int_handler)
      thread = ThreadedServer(MasterServer, port = 2131)
      thread.start()