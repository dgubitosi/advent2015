
import sys

totalBytes = 0
totalChars = 0

with open(sys.argv[1]) as f:
    for line in f:
        code = line.strip()
        bytes = len(code)
        chars = bytes
        if code[0] == '"': chars -= 1
        if code[-1] == '"': chars -= 1
        start = 0
        while start < len(code):
            index = code.find('\\', start)
            if index < 0: break
            index += 1
            start = index
            c = code[index]
            if c == '\\':
                chars -= 1
                start += 1
            if c == '"':
                chars -= 1
            if c == 'x':
                chars -= 3
        print(code, bytes, chars)
        totalBytes += bytes
        totalChars += chars
print(totalBytes)
print(totalChars)
print(totalBytes - totalChars)
