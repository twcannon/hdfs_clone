# hdfs_clone
HDFS Clone for CSIS 604 at CofC

## Setup

### Install Requirements

`pip install -r requirements.txt`



## System Configuration

### Deploying Nodes
On each machine that you would like to operate as a node, cd to the project directory and run `python node.py`.  
This will activate that machine as a node. The default listening port is 8888.  

### Deploying Master
On line 18 on `master.py`, you must insert the id numbers, ip addresses, and port numbers of the nodes that you have activated like so: `id:ip_address:port`. the id number is simply for keeping track of the nodes.  


## System Use

### Running the `client.py` File

The main functions of the system are `put` and `get`. Below, we describe how to use the system to store and retrieve files on the system. A sample file `cat64ms.00105` is included. In the examples below, it is saved and retrieved in the system as `sample.txt`.  

#### Put
##### Example `put` Call
`python client.py put cat64ms.00105 sample.txt`

#### Get
##### Example `get` Call
`python client.py get sample.txt`