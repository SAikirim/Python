from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        self.h_pocess        = None
        self.pid             = None
        self.debugger_active = False

    def load(self, path_to_exe):
        # dwCreation 플래그를 이용해 프로세스를 어떻게 생성할 것인지 판단한다.
        # 계산기의 GUI를 보고자 한다면 creation_flags를
        # CREATE_NEW_CONSOLE로 설정하면 된다.
        creation_flags = DEBUG_PROCESS

        # 구조체 인스턴스화
        startupinfo         = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        """ 다음의 두 옵션은 프로세스가 독립적인 창으로 실행되게 만들어준다.
        이는 STARTUPINFO struct 구조체의 설정 내용에 따라 디버거 프로세스에
        어떤 영향을 미치는지 보여준다."""
        startupinfo.dwFlags     = 0x1
        startupinfo.wShowWindow = 0x0

        ''' 다음에는 STARTUPINFO struct 구조체 자신의 크기를 나타내는 cb 변수 값을
        초기화한다.'''
        startupinfo.cb = sizeof(startupinfo)

        # python3 버전은 'kernel32.CreateProcessW()'를 사용
        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startupinfo),
                                   byref(process_information)):

            print("[*] We have successfully lanuched the process!")
            print("[*] PID: %d" % process_information.dwProcessId)
        else:
            print("[*] Error: 0x%08x." % kernel32.GetLastError())

    # 새로 생성한 프로세스의 핸들을 구한 후
    # 나중에 접근하기 위해 저장
    self.h_pocess = self.open_process(process_information.dwProcessId)

    def open_process(self, pid):
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        return h_process

    def attach(self, pid):
        self.h_pocess = self.pid_prosess(pid)

        # 프로세스에 대한 어태치를 시도한다.
        # 실패하면 호출 종료
        if kernel32.DebugActiveProsess(pid):
            self.debugger_active = True
            self.pid             = int(pid)
        else:
            print("[*] Unable to attach to the process.")