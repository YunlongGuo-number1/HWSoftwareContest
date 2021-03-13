import DataLoad
import Server
class CloudManager():
    #调度
    # TODO 初始化，读取DataLoad对象，并获取服务器，虚拟机，用户请求等信息。
    def __init__(self, path):
        dataload = DataLoad(path)
        self._server_type_list_info = dataload.get_server_type_list_info()
        self._vm_type_list_info = dataload.get_vm_type_list_info()
        self._vm_request = dataload.get_vm_request()

    # TODO 创建服务器对象列表，虚拟机对象列表， 请求列表 作为成员变量
    def creatSubjectList():
        self.server_subject = []
        for server_type in self._server_type_list_info:
            self.server_subject.append(Server(server_type[0], ))

    # TODO 进行调度


    # TODO 迁移


    # TODO 删除
    
    
    # TODO 部署


    # TODO 打印输出