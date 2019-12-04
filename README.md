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

### Running the `client.py` file

#### Example
`python client.py put cat64ms.00105 sample.txt`