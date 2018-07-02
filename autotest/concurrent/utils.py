import os
import subprocess
# os.system('netstat -ano | findstr 4723')
import time


class AppiumUtil:
    """
    appium服务工具类
    """

    @staticmethod
    def start_server(port):
        print('start_server... port=', port)
        command = 'appium -p {} > D:/appium-{}.log'.format(port, port)
        p = subprocess.Popen(command, shell=True)
        time.sleep(5)


class SystemUtil:
    """
    系统工具类
    """

    @staticmethod
    def is_unused_port(port):
        """
        判断是否为未使用的端口
        :param port: 端口
        :return: true:未使用; false:已使用
        """
        lines = SystemUtil.exec_cmd('netstat -ano | findstr {}'.format(port))
        return len(lines) == 0

    @staticmethod
    def get_unused_port(start_port, size):
        """
        获取未使用的端口号
        :param start_port: 开始端口
        :param size: 需要端口的个数
        :return: 未使用的端口列表
        """
        port_list = []
        while len(port_list) < size:
            if SystemUtil.is_unused_port(start_port):
                port_list.append(start_port)
            start_port += 1
        return port_list

    @staticmethod
    def exec_cmd(command):
        """
        执行命令，并返回执行后的信息
        :param command: 命令
        :return: 输出结果
        """
        return os.popen(command).readlines()

    @staticmethod
    def get_pid_by_port(port):
        """
        根据端口号获取对应的进程id
        :param port: 端口号
        :return: 进程id
        """
        lines = SystemUtil.exec_cmd('netstat -ano | findstr {}'.format(port))
        print('lines====', lines)
        for line in lines:
            split = line.split()
            for s in split:
                if s.endswith(':' + str(port)):
                    return split[len(split) - 1]
        return None

    @staticmethod
    def kill_with_pid(pid):
        """
        杀掉进程
        :param pid: 进程id
        """
        lines = SystemUtil.exec_cmd('taskkill /F /pid {} /T'.format(pid))
        print('kill_with_pid result=', lines)


class AdbUtil:
    """
    adb 命令操作工具类
    """

    @staticmethod
    def get_devices():
        """
        获取连接的设备列表
        :return: 设备id列表
        """
        devices = []
        lines = AdbUtil.exec_adb('devices')
        print('lines=', lines)
        for i in range(1, len(lines)):
            line = lines[i].strip()
            print('line=', line)
            if line != '':
                devices.append(line.split()[0])
        return devices

    @staticmethod
    def exec_adb(command):
        return SystemUtil.exec_cmd('adb {}'.format(command))


if __name__ == '__main__':
    # pid = SystemUtil.get_pid_by_port(4723)
    # print(pid)
    devices = AdbUtil.get_devices()
    print('devices=', devices)

    # s = '\n'
    # if s.strip():
    #     print('not empyt')
    # else:
    #     print('is empty')
