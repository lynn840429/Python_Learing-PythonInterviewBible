str_in = "123456789"

# **方法一**：反向切片
def reverse_string1(content):
    return content[::-1]

print(reverse_string1(str_in))

# **方法二**：反转拼接
def reverse_string2(content):
    return ''.join(reversed(content))

print(reverse_string2(str_in))

# **方法三**：递归调用
def reverse_string3(content):
    if len(content) <= 1:
        return content
    return reverse_string3(content[1:]) + content[0]

print(reverse_string3(str_in))

# **方法四**：双端队列
from collections import deque

def reverse_string4(content):
    q = deque()
    q.extendleft(content)
    return ''.join(q)

print(reverse_string4(str_in))

# **方法五**：反向组装
from io import StringIO

def reverse_string5(content):
    buffer = StringIO()
    for i in range(len(content)-1, -1, -1):
        buffer.write(content[i])
    return buffer.getvalue()

print(reverse_string5(str_in))

# **方法六**：反转拼接
def reverse_string6(content):
    return ''.join([content[i] for i in range(len(content)-1, -1, -1)])

print(reverse_string6(str_in))

# **方法七**：半截交换
def reverse_string7(content):
    length, content= len(content), list(content)
    for i in range(length//2):
        content[i], content[length-1-i] = content[length-1-i], content[i]
    return ''.join(content)

print(reverse_string7(str_in))

# **方法八**：对位交换
def reverse_string8(content):
    length, content= len(content), list(content)
    for i, j in zip(range(length//2), range(length-1, length//2-1, -1)):
        content[i], content[j] = content[j], content[i]
    return ''.join(content)

print(reverse_string8(str_in))
