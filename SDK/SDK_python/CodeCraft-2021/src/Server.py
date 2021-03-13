# Copyright 2021 Gyl, Lbf, Lyb. All Rights Reserved.
import config
from VirtualMachine import VirtualMachine
from config import POWER
from config import node_name
from config import node_mode

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
    def __init__(self, node: config.node_name,size: config.specification_dict, server_num: config.server_number):
        self._size = size
        self._avaliable_space = size
        # TODO maybe a list is not efficient enough.
        self._vm_id_list = []
        self._server_num = server_num
        self._node_name = node

    # 获取可用的CPU核心数
    def get_avaliable_cpu(self)->config.cpu_core:
        return self._avaliable_space[config.CORE]

    # 获取可用的内存
    def get_avaliable_mem(self)->config.memory_capacity:
        return self._avaliable_space[config.MEMORY]
    
    # 尝试进行虚拟机删除
    def delete_vm(self, vm: VirtualMachine):
        #TODO didn't check the upper bound of the avaliable_space.
        if vm.get_id() in self._vm_id_list:
            # delete the id of virtual machine.
            vm_index = self._vm_id_list.index(vm.get_id())
            del self._vm_id_list[vm_index]
            # free the core and memory.
            self._avaliable_space[config.CORE] += vm.get_avaliable_cpu()
            self._avaliable_space[config.MEMORY] += vm.get_avaliable_mem()
            # 删除虚拟机的硬件环境（服务器编号，节点）
            vm.delete_location()
            
        
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
    def insert_vm(self, vm: VirtualMachine)->bool:
        if self.check_capacity(vm):
            self._vm_id_list.append(vm.get_id)
            self._avaliable_space[config.CORE] -= vm.get_cpu_required()
            self._avaliable_space[config.MEMORY] -= vm.get_mem_required()
            # 配置虚拟机的硬件环境（服务器编号，节点）
            vm.set_location(self._server_num, self._node_name)
            return True
        else:
            print('fail to insert vm')
            return False
    
    def find_vm_list(self, id: config.ID):
        return id in self._vm_id_list
            


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
                 power_status: config.is_on):

        self._server_number = serial_number
        self._spec = {
                 config.MODEL_NAME: specification[config.MODEL_NAME],
                 config.CORE: specification[config.CORE],
                 config.MEMORY: specification[config.MEMORY]}
        self._cost = {config.HARDWARE_COST, cost[config.HARDWARE_COST],
                      config.SOFTWARE_COST, cost[config.SOFTWARE_COST]}
        self._power_status = power_status
        #initialize the node A, B
        self._nodes = {
            config.A: NodeVector(config.A, {config.CORE: self._spec[config.CORE] /2, 
                                             config.MEMORY: self._spec[config.MEMORY]/ 2},
                                             self._server_number),
            config.B: NodeVector(config.B, {config.CORE: self._spec[config.CORE] /2, 
                                             config.MEMORY: self._spec[config.MEMORY]/ 2},
                                             self._server_number)
        }
                                             
    # TODO 设置电源的接口
    def set_power_status(self, status: POWER):
        self._power_status = status

    # 部署虚拟机的接口
    def deploy_vm(self, vm: VirtualMachine, node: node_name = ''):
        vm_node = vm.get_node_mode()
        # 如果虚拟机为双节点部署，则不需要用node_name这个参数, 不清楚这样会不会影响效率
        if vm_node == node_mode.double_mode and node_name == node_mode.invalid_mode:
                if self._nodes[config.A].insert_vm(vm) and self._nodes[config.B].insert_vm(vm) :
                    return True
                else: return False
        elif vm_node == node_mode.single_mode and node_name != '':
                if self._nodes[node_name].insert_vm(vm):
                    return True
                else:
                    return False
        return False
                
            
        # TODO 迁移虚拟机的上层接口
    

    # TODO 删除虚拟机的上层接口
    def delete_vm_from_nodes(self, vm: VirtualMachine):
        if self._nodes['A'].find_vm_list(vm.get_id()):
            self._nodes['A'].delete_vm(vm)
            return None
        elif self._nodes['B'].find_vm_list(vm.get_id()):
            pass


        # TODO 添加虚拟机的上层接口
    # member var.