o = ['000', '001', '010', '011', '100', '101', '110', '111']
digits = map(int, input())
result = ''
for d in digits:
    result += o[d]
print('0') if result == '000' else print(result.lstrip('0'))
