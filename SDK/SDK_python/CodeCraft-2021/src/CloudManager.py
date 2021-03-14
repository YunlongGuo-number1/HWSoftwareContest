from DataLoad import DataLoad
from Server import Server
from VirtualMachine import VirtualMachine
import config
class CloudManager():
    #调度
    # TODO 初始化，读取DataLoad对象，并获取服务器，虚拟机，用户请求等信息。
    def __init__(self, path):
        dataload = DataLoad()
        self._server_type_dict_info = dataload.get_server_type_list_info()
        self._vm_type_dict_info = dataload.get_vm_type_list_info()
        self._vm_request = dataload.get_vm_request()
        self._server_not_used = [] # 服务器对象列表
        self._server_used = []  # 服务器对象列表
        self._vm_setted_dict = {} # {虚拟机ID： [虚拟机对象, 服务器对象]}


    # TODO 创建服务器对象列表，虚拟机对象列表, 作为成员变量，初始化还得改
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
        # key是虚拟机ID，value是[虚拟机对象， 服务器对象]
        if delVmId in self._vm_setted_dict.keys():
            vm, server = self._vm_setted_dict[delVmId]
            server.delete_vm_from_nodes(vm)
            # 如果服务器没有内存使用，则移到未使用列表中
            if server.get_all_memory() == server.get_avaliable_mem():
                self._server_used.remove(server)
                self._server_not_used.append(server)
        else: print("删除错误，没有对应ID的虚拟机")
     
    
    # TODO 部署
    def addHandle(self, addVmType, addVmId):
        vmCPU, vmMem, vmNodeype = self._vm_type_dict_info[addVmType]
        vm = VirtualMachine(addVmId, vmCPU, vmMem, vmNodeype, addVmType)
        # 优先从在运行状态的服务器选择
        if self._server_used:
            filterList = self.filterSubject(vm, self._server_used)
            bestServer = self.loadRateServerSort(filterList)
            bestServer.deploy_vm(vm)

        # 其次从在非运行状态的服务器选择
        elif self._server_not_used:
            filterList = self.filterSubject(vm, self._server_not_used)
            bestServer = self.priceRateSort(filterList)
            bestServer.deploy_vm(vm)
            # 移动服务器
            self._server_used.append(bestServer)
            self._server_not_used.remove(bestServer)

        # 最后从在可购买的服务器选择
        else:
            filterList = self.filterSubject(vm, self._server_available)
            bestServer = self.buyServerSotr(filterList)
            bestServer.deploy_vm(vm)
            # 移动服务器
            self._server_used.append(bestServer)

    
    # TODO 筛选服务器列表，返回可装下虚拟机的
    def filterSubject(self, vm , originList):
        filterList = []
        for server in originList:
            if server.check_capacity(vm): filterList.append(server)
        return filterList

    # 对在运行的服务器列表根据负载率进行排序
    def loadRateServerSort(self, filterList):
        res = filterList[0]
        loadRate = 0
        for i in range(len(filterList)):
            temp = (filterList[i].get_all_cpu() + filterList[i].get_all_memory()) / (filterList[i].get_avaliable_cpu() + filterList[i].get_avaliable_mem()) 
            if loadRate < temp: 
                loadRate = temp
                res = filterList[i]
        return res
    # 对未运行的服务器根据（价格+耗能）/（内存+CPU）进行排序
    def priceRateSort(self, serverList):
        res = serverList[0]
        priceRate = 0
        for i in range(len(serverList)):
            temp = (serverList[i].get_hardware_cost() + serverList[i].get_software_cost()) / (serverList[i].get_all_cpu() + serverList[i].get_all_memory())
            if priceRate > temp: 
                priceRate = temp
                res = serverList[i]
        return res

    # 对可购买的服务器根据（价格）/（内存+CPU）进行排序
    def buyServerSort(self, serverList):
        res = serverList[0]
        priceRate = 0
        for i in range(len(serverList)):
            temp = serverList[i].get_hardware_cost() / (serverList[i].get_all_cpu() + serverList[i].get_all_memory())
            if priceRate > temp: 
                priceRate = temp
                res = serverList[i]
        return res

    # TODO 打印输出