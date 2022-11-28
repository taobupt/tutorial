# ------------字符串切割--------------
# 按照逗号进行分割
line = 'abc,def,ghi,jklm'
words = line.split(',')
print(line+' 按照逗号进行分割的结果', words)
print('-------------------------------')

# 按照换行符进行分割
line = '''abc
def
ghi
jklm'''
words = line.split('\n')
print(line+' 按照换行符进行分割的结果', words)
print('-------------------------------')

# 按照分号进行分割
line = 'abc;def;ghi;jklm'
words = line.split(';')
print(line+' 按照分号进行分割的结果', words)
