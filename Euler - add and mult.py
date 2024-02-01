def add(string1,string2):
    maxL = max(len(string1),len(string2))
    string1 = string1.rjust(maxL,'0')
    string2 = string2.rjust(maxL,'0')
    res = ''
    carry = 0
    for i in reversed(range(maxL)):
        curr = int(string1[i])+int(string2[i])+carry
        if i==0:
            res+=str(str(curr)[::-1])
            break
        res+=str(curr%10)
        if len(str(curr))==1:
            carry = 0
        else:
            carry = curr//10
    return res[::-1]

def mult(string1,string2):
    if len(string1)==1 and len(string2)==1:
        return str(int(string1)*int(string2))
    carry = '0'
    res = ''
    for char in string1[::-1]:
        curr = add(mult(string2,char),carry)
        res+= curr[-1]
        if len(curr)==1:
            carry = '0'
        else:
            carry = curr[:-1]
    if carry!='0':
        res+=carry[::-1]
    return(res[::-1])

res = '1'
for i in range(1,101):
    res = mult(res,str(i))
ans = 0
for char in res:
    ans+=int(char)
print(ans)