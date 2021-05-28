import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
x = ''

def wrap_by_word(s, n):
    a = s.split()
    ret = ''
    for i in range(0, len(a), n):
        ret += ' '.join(a[i:i+n]) + '\n'
    return ret

with open(file1) as fin:
    for line in fin:
        x += line.replace('\n', ' ')
with open(file2, 'w') as fout:
    y = wrap_by_word(repr(x), int(sys.argv[3]))
    fout.write('"' + y.replace("'", "").replace(" ", '", "').replace("\n", '"\n"'))
