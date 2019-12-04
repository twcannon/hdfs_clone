import rpyc
import sys
import os



def send_to_node(block_uuid,data,nodes):
    print("sending: " + str(block_uuid) + str(nodes))
    node=nodes[0]
    nodes=nodes[1:]
    host,port=node
    
    conn=rpyc.connect(host,port=port)
    node = conn.root.Minion()
    node.put(block_uuid,data,nodes)



def read_from_node(block_uuid,node):
    host,port = node
    conn=rpyc.connect(host,port=port)
    node = conn.root.Minion()
    return node.get(block_uuid)


def get(master,fname):
    file_table = master.get_file_table_entry(fname)
    if not file_table:
        LOG.info("404: file not found")
        return

    for block in file_table:
        for m in [master.get_nodes()[_] for _ in block[1]]:
          data = read_from_node(block[0],m)
          if data:
            sys.stdout.write(data)
            break
        else:
            LOG.info("No blocks found. Possibly a corrupt file")



def put(master,source,dest):
    size = os.path.getsize(source)
    blocks = master.write(dest,size)
    with open(source) as f:
        for b in blocks:
            data = f.read(master.get_block_size())
            block_uuid=b[0]
            nodes = [master.get_nodes()[_] for _ in b[1]]
            send_to_node(block_uuid,data,nodes)


def main(args):
  conn=rpyc.connect("localhost",port=2131)
  master=conn.root.Master()
  
  if args[0] == "get":
    get(master,args[1])
  elif args[0] == "put":
    put(master,args[1],args[2])
  else:
    print("possible options:")
    print("'put source_file dest_file'")
    print("'get file'")


if __name__ == "__main__":
  main(sys.argv[1:])
