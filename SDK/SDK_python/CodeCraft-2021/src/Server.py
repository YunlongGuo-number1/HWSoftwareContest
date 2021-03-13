# Copyright 2021 Gyl, Lbf, Lyb. All Rights Reserved.
import config
import VirtualMachine


# ====================================================================
# there should be a vector maintain a map containing the info of virtual machine
# and the space they used
# ====================================================================

# TODO i didn't check the size.
class NodeVector():
    # 节点容器是对象是属于服务器对象的一部分，一个服务器对象拥有两个节点，
    # 初始化服务器实例时，应当同时初始化服务器中的两个节点
    # 初始化一个节点需要输入两个维度的容量大小（cpu, memory）
    # 输入格式如下
    # size = {config.CORE: 32, config.MEMORY: 64}
    # vector_a = NodeVector(size)
    def __init__(self, size: config.specification_dict, server_num: config.server_number):
        self._size = size
        self._avaliable_space = size
        self._vm_id_list = []
        self._server_num = server_num

    # 获取可用的CPU核心数
    def get_avaliable_cpu(self)->config.cpu_core:
        return self._avaliable_space[config.CORE]

    # 获取可用的内存
    def get_avaliable_mem(self)->config.memory_capacity:
        return self._avaliable_space[config.MEMORY]
    
    # 尝试进行虚拟机迁移，此处需要输入一个虚拟机实例，通过检查虚拟机实例的节点部署规则和所需内存，核心数，来
    def migrate_vm(self, vm: VirtualMachine):
        #TODO didn't check the upper bound of the avaliable_space.
        if vm.get_id() in self._vm_id_list:
            # delete the id of virtual machine.
            vm_index = self._vm_id_list.index(vm.get_id())
            del self._vm_id_list[vm_index]
            # free the core and memory.
            self._avaliable_space[config.CORE] += vm.get_avaliable_cpu()
            self._avaliable_space[config.MEMORY] += vm.get_avaliable_mem()
        
    # call this method to check the capacity of cpu and memory.
    def check_capacity(self, vm: VirtualMachine)->bool:
            cpu_required = vm.get_cpu_required()
            mem_required = vm.get_mem_required()
            if self._avaliable_space[config.CORE] != 0 and \
               self._avaliable_space[config.MEMORY] != 0 and  \
               self._avaliable_space[config.CORE] >= cpu_required and \
               self._avaliable_space[config.MEMORY] >= mem_required:
                return True
            else:
                print("no space available!")
                return False

    # this method should be the only interface which allow managers to insert vm.
    # and after inverting, _avaliable_space should be updated.
    # 尝试进行虚拟机部署，此处需要输入一个虚拟机实例，通过检查虚拟机实例的节点部署规则和所需内存，核心数，来在服务器节点中部署虚拟机
    def insert_vm(self, vm: VirtualMachine):
        if self.check_capacity(vm):
            self._vm_id_list.append(vm.get_id)
            self._avaliable_space[config.CORE] -= vm.get_cpu_required()
            self._avaliable_space[config.MEMORY] -= vm.get_mem_required()
        else:
            print('fail to insert vm')
            


# ====================================================================
# we need to declare a class Server to represent that in real life.
# the serial number, cost, 
# specification which contains Memory capacity 
# and Number of CPU core,
#  and the vectors of two nodes should be defined clearly in the class.
# in addition, the status of Power is necessary for us
# ====================================================================

class Server():
    def __init__(self, serial_number: config.server_number, 
                 specification: config.specification_dict, 
                 cost: config.cost_dict, 
                 power_status: config.is_on, 
                 model: config.model_type):

        self._server_number = serial_number
        self._spec = {config.CORE: specification[config.CORE],
                 config.MEMORY: specification[config.MEMORY]}
        self._cost = {config.HARDWARE_COST, cost[config.HARDWARE_COST],
                 config.SOFTWARE_COST, cost[config.SOFTWARE_COST]}
        self._power_status = power_status

        self._model = model
        #initialize the node A.
        self._node = {
                 
        }
    # member var.