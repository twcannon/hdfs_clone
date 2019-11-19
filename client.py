import rpyc
import sys


def send_to_node(block_uuid,data,nodes):


def read_from_node(block_uuid,node):


def get(master,fname):
  print('get works')


def put(master,source,dest):
  print('put works')


def main(args):
  con=rpyc.connect("localhost",port=2131)
  master=con.root.Master()
  
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
