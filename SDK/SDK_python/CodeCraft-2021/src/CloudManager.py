from DataLoad import DataLoad
from Server import Server
from VirtualMachine import VirtualMachine
class CloudManager():
    #调度
    # TODO 初始化，读取DataLoad对象，并获取服务器，虚拟机，用户请求等信息。
    def __init__(self, path):
        dataload = DataLoad()
        self._server_type_list_info = dataload.get_server_type_list_info()
        self._vm_type_list_info = dataload.get_vm_type_list_info()
        self._vm_request = dataload.get_vm_request()
        self._server_buyed = [] # 服务器对象列表
        self._server_used = []  # 服务器对象列表
        self._vm_setted_list = [] # 虚拟机对象列表


    # TODO 创建服务器对象列表，虚拟机对象列表, 作为成员变量
    def creatSubjectList(self):
        self._server_available = []
        self._vm_available = []
        for server_type in self._server_type_list_info:
            self._server_available.append(Server(server_type[0], server_type[1], server_type[2], server_type[3]))
        for vm_type in self._vm_type_list_info:
            self._vm_available.append(VirtualMachine(vm_type[0], vm_type[1], vm_type[2], vm_type[3]))

    def requestHandle(self):
        for oneDayRequest in self._vm_request:
            if oneDayRequest[0] == 'add':
                self.addHandle(oneDayRequest[1], oneDayRequest[2])
            else:
                self.delHandle(oneDayRequest[1])
    # TODO 进行调度


    # TODO 迁移


    # TODO 删除
    def delHandle(self, delVmId):
        for vm in self._vm_setted_list:
            if delVmId == vm.get_id():
                current_position = vm.get_current_position()
                for server in self._server_used:
                    if server.get_server_num() == current_position[config.SERVER_NUMBER]:
                        server.delete_vm_from_nodes(vm)
    

    
    
    # TODO 部署
    def addHandle(self, addVmType, addVmId):
        pass
    


    # TODO 打印输出