# Copyright 2021 Gyl, Lbf, Lyb. All Rights Reserved.

# ====================================================================
# we need to declare a class Server to represent that in real life.
# the serial number, cost, 
# specification which contains Memory capacity 
# and Number of CPU core,
#  and the vectors of two nodes should be defined clearly in the class.
# in addition, the status of Power is necessary for us
# ====================================================================

import config
class Server():
    def __init__(self, serial_number: config.server_number, 
                 specification: config.specification_dict, 
                 cost: config.cost_dict, 
                 power_status: config.is_on):

        _server_number = serial_number
        _spec = {config.CORE: specification[config.CORE],
                 config.MEMORY: specification[config.MEMORY]}
        _cost = {config.HARDWARE_COST, cost[config.HARDWARE_COST],
                 config.SOFTWARE_COST, cost[config.SOFTWARE_COST]}
        _power_status = power_status
        
    # member var.