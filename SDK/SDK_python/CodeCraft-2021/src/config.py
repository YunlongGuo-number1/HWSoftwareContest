# Copyright 2021 Gyl, Lbf, Lyb. All Rights Reserved.

# ====================================================================
# in this files we define some data type as the concept we could read easily
# ====================================================================

from enum import Enum, unique


# is_on is to mark if the server's power is set to ON.
is_on = bool 

# these types below are about to define the specification of a server.
memory_capacity = int
cpu_core = int
MEMORY = 'memory_capacity'
CORE = 'cpu_core'
specification_dict = dict
model_type = str
INVALID_MODEL = 'NULl'
SERVER_MODEL_NAME = str



# these types below are about to define the cost of a server.
hardware_cost = int
software_cost = int
HARDWARE_COST = 'hardware_cost'
SOFTWARE_COST = 'software_cost'
cost_dict = dict

# serial number of servers.
server_number = int
SERVER_NUMBER = "server_number"
NODE_NAME = "node_name"

# node and vector
node_name = str
A = 'A'
B = 'B'
INVALID_NODE = 'NULL'
INVALID_SERVER_NUM = -1

vector_size = int


# virtual machine users purchase
vm_type = str
INVALID_POSITION = {SERVER_NUMBER: INVALID_SERVER_NUM,
                    NODE_NAME: INVALID_NODE}
server_number_index = 0
node_index = 1
MODEL_NAME = "model_name"
model_name = str


ID = int
INVALID_ID = -1


# check capacity
@unique
class node_mode(Enum):
    invalid_mode = -1
    single_mode = 0
    double_mode = 1

# power status
@unique
class POWER(Enum):
    ON = 0
    OFF = 1