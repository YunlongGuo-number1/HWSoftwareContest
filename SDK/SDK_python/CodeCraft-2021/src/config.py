# Copyright 2021 Gyl, Lbf, Lyb. All Rights Reserved.

# ====================================================================
# in this files we define some data type as the concept we could read easily
# ====================================================================



# is_on is to mark if the server's power is set to ON.
is_on = bool 

# these types below are about to define the specification of a server.
memory_capacity = int
cpu_core = int
MEMORY = 'memory_capacity'
CORE = 'cpu_core'
specification_dict = dict


# these types below are about to define the cost of a server.
hardware_cost = int
software_cost = int
HARDWARE_COST = 'hardware_cost'
SOFTWARE_COST = 'software_cost'
cost_dict = dict

# serial number of servers.
server_number = int