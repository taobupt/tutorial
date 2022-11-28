# ------------字符串连接---------------
# 按照逗号进行连接
words = ['abc', 'def', 'ghi', 'jklm']
line = ','.join(words)
print(str(words) + ' 按照逗号进行连接的结果', line)

# 按照点号进行连接
words = ['data', 'csv']
line = '.'.join(words)
print(str(words) + ' 按照点号进行连接的结果', line)

# 按照分号进行连接
words = ['abc', 'def', 'ghi', 'jklm']
line = ';'.join(words)
print(str(words) + ' 按照分号进行连接的结果', line)