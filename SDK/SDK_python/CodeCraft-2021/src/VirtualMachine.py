# Copyright 2021 Gyl, Lbf, Lyb. All Rights Reserved.
import config

# ====================================================================
# we need to declare a class VirtualMachine to represent that in real life
# the ID, specification which contains name, cpu required and memory required
# and the node mode, current location (server), Mode should be declared clearly
# ====================================================================


class VirtualMachine():
    # 初始化函数用来初始化一个虚拟机实例，需要用户输入虚拟机id,虚拟机规格（内存，核心数），节点部署模式（node_mode）,型号（model）
    def __init__(self, id: config.ID, 
                 specification: config.specification_dict, 
                 node_mode: config.node_mode,
                 model: config.model_name):
        self._id = id
        self._spec = {
                config.MODEL_NAME: model,
                config.CORE: specification[config.CORE],
                config.MEMORY: specification[config.MEMORY]
        }
        # TODO maybe when we initialize a vm, the current location could be left out.
        # TODO maybe there are some logical problems.
        self._current_position = config.INVALID_POSITION
        self._node_mode = node_mode

    # 获得所有CPU核心数
    def get_all_cpu_core(self)->config.cpu_core:
        return self._spec[config.CORE]

    # 获得所有内存
    def get_all_memory(self)->config.memory_capacity:
        return self._spec[config.MEMORY]

    # 获取该虚拟机对象的规格，包含核心数和所需内存
    def get_spec(self)->config.specification_dict:
        return self._spec

    # 获取节点模式，如双节点或单节点
    def get_node_mode(self)->config.node_mode:
        return self._node_mode

    # 获取虚拟机对象的id
    def get_id(self)->config.ID:
        return self._id

    # 根据节点模式，返回对应的CPU核心数需求
    def get_cpu_required(self)->config.cpu_core:
        cpu_required = self._spec[config.CORE] if self._node_mode == config.node_mode.double_mode else self._spec[config.CORE] / 2
        return cpu_required

    # 根据节点模式，返回对应的内存需求
    def get_mem_required(self)->config.memory_capacity:
        mem_required = self._spec[config.MEMORY] if self._node_mode == config.node_mode.double_mode else self._spec[config.MEMORY] / 2
        return mem_required

    # 在一个虚拟机实例被部署到服务器节点上时，应当设置虚拟机实例的当前部署位置
    # 在迁移时，也应当调用该接口来重置虚拟机部署位置
    def set_location(self, server_num: config.server_number, node: config.node_name):
        self._current_position = {config.SERVER_NUMBER: server_num,
                                  config.NODE_NAME: node}
                                  
    def delete_location(self):
        self._current_position = config.INVALID_POSITION
