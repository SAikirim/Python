from ctypes import *

# ctypes 형태의 타입을 마이크로소프트의 타입으로 매핑
WORD = c_ushort             # 16bit unsigned integer
DWORD = c_ulong             # 32bit unsigned integer
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p

# 상수
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010

# CreateProsessA() 함수를 위한 구조체
class STARTUPINFO(Structure):
    _fields_ = [
        ("cb",          DWORD),
        ("lpReserved",  LPTSTR),
        ("lpDesktop",   LPTSTR),
        ("lpTitle",     LPTSTR),
        ("dwX",         DWORD),
        ("dwY",         DWORD),
        ("dwXSize",     DWORD),
        ("dwYSize",     DWORD),
        ("dwXCountChars",     DWORD),
        ("dwYCountChars",     DWORD),
        ("dwFillAttribute",     DWORD),
        ("dwFlags",     DWORD),
        ("wShowWindow",     WORD),
        ("cbReserved2",     WORD),
        ("lpReserved2",     LPBYTE),
        ("hStdInput",     HANDLE),
        ("hStdOutput",     HANDLE),
        ("hStdError",     HANDLE),
    ]

class PROCESS_INFORMATION(Structure):
    _fields_ = [
        ("hProcess",        HANDLE),
        ("hThread",         HANDLE),
        ("dwProcessId",     DWORD),
        ("dwThreadId",      DWORD),
    ]