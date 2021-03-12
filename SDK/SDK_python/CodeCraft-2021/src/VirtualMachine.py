# Copyright 2021 Gyl, Lbf, Lyb. All Rights Reserved.
import config

# ====================================================================
# we need to declare a class VirtualMachine to represent that in real life
# the ID, specification which contains name, cpu required and memory required
# and the node mode, current location (server), Mode should be declared clearly
# ====================================================================


class VirtualMachine():
    def __init__(self, id: config.ID, 
                 specification: config.specification_dict, 
                 mode: config.node_mode):
        self._id = id
        self._spec = {
                config.CORE: specification[config.CORE]
                config.MEMORY: specification[config.MEMORY]
        }
        # TODO maybe when we initialize a vm, the current location could be left out.
        # TODO maybe there are some logical problems.
        self._current_position = config.INVALID_POSITION
        self._mode = mode
    def get_all_cpu_core(self)->config.cpu_core:
        return self._spec[config.CORE]
    def get_all_memory(self)->config.memory_capacity:
        return self._spec[config.MEMORY]
    def get_spec(self)->config.specification_dict:
        return self._spec
    def get_node_mode(self)->config.node_mode:
        return self._mode
    def get_id(self)->config.ID:
        return self._id
    def get_cpu_required(self)->config.cpu_core:
        cpu_required = self._spec[config.CORE] if self._mode == double_mode else self._spec[config.CORE] / 2
        return cpu_required
    def get_mem_required(self)->config.memory_capacity:
        mem_required = self._spec[config.MEMORY] if self._mode == double_mode else self._spec[config.MEMORY] / 2
        return mem_required

    
