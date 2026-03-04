try:
    with open('F:\python_demo\文件读写和异常处理\致橡树.txt', 'r') as f:
        content = f.read() # 读取文件内容
        print(content) # 打印文件内容
except FileNotFoundError:
    print("文件未找到，请检查文件路径是否正确。")
except IOError:
    print("文件读取错误，请检查文件是否损坏。")
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
f.close() # 关闭文件