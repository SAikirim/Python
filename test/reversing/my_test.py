import my_debugger

debugger = my_debugger.debugger()

# python3 버전은 UTF-8로 문자열 사용, 'debugger.load("C:\\WINDOWS\\system32\\calc.exe")'
debugger.load(b"C:\\WINDOWS\\system32\\calc.exe")