#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:

import time
from typing import Dict


def toString(Dict):
    rs = ""
    for i in Dict.values():
        rs += str(i)
    return rs

def GetInput(Fname):
    rs = ""
    F = open(Fname)
    inp = F.read()
    flag = 0
    inp_satisfied = False #kiem tra =
    for i in range(0,len(inp)):
        if inp[i].isalpha():
            rs += inp[i]
        else: 
            if inp[i] == "=":
                inp_satisfied = True
                rs+= '='
            elif inp[i] == '(':
                if i > 0 and inp[i-1] == '-':
                    flag = True
                continue
            elif inp[i] == ')':
                flag = False
                continue
            elif inp[i] == '*':
                rs += '*'
            elif flag:
                if inp[i] == '+':
                    rs += '-'
                else:
                    if inp[i] == '-':
                        rs += '+'
            else:
                rs += inp[i]
  
    F.close() 
    if inp_satisfied:
        return rs
    else:
        return None
              
    

def InitInput(data):
    for i in data:
        if i.isalpha():
            start.update({i: -1}) # khởi tạo giá trị ban đầu
    
    operator=list() #List các dấu + -
    operator.append('+')
    
    for i in data:
        if i == '+' or i == '-':
            operator.append(i) #Add các phép toán vào list
    
    #Tiếp theo là xử lý cắt tỉa chuỗi
    data = data.replace('+', ' ')
    data = data.replace('-', ' ')
    tmp = data.split('=') 
    result = tmp[1] #Chuỗi kết quả sau dấu =
    operand = tmp[0].split(' ')  #Chuỗi các số hạng
    
    MaxLenOpe = 0
    for i in range(len(operand)):
        MaxLenOpe = max(len(operand[i]),MaxLenOpe) # tìm số hạng có độ dài lớn nhất     
    MAX = max(len(result), MaxLenOpe) # So với cả kết quả
   
    for i in range(0, MAX):
        impact.append(dict())
        Col.append(list())
        
    # Thêm các kí tự của các toán hạng vào các Col tương ứng
    for i in range(len(operand)):
        opr = operand[i]   # Lấy ra từng số hạng
        for j in range(len(opr)):
            # Đánh dấu index ngược lại vì giải từ phải sang
            idx = len(opr) - j - 1

            # Xử lí khi kí tự chưa được thêm vào dict
            if not opr[j] in impact[idx]:
                if operator[i] == '+':
                    posi = 1
                    nega = 0
                else:
                    posi = 0
                    nega = 1

                Col[idx].append(opr[j])
                impact[idx].update({opr[j]: (posi, nega)})
            else:
                # Ngược lại, xử lí khi kí tự đã được thêm vào dict
                # Chỉ cần update tuple value của kí tự (key) được thêm vào dựa vào toán tử liền trước
                posi = impact[idx][opr[j]][0]
                nega = impact[idx][opr[j]][1]

                if operator[i] == '+':
                    posi = posi + 1
                else:
                    nega = nega + 1

                impact[idx].update({opr[j]: (posi, nega)})

    #Thêm từng cột của phép tính vào Col
    for i in range(len(result)):
        c = result[len(result)-i-1]
        if c not in Col[i]:
            Col[i].append(c)
            impact[i].update({c: (0, 1)})
        else:
            posi = impact[i][c][0]
            nega = impact[i][c][1] + 1
            impact[i].update({c: (posi, nega)})
    
def InitInputMultiplication(data):
    for i in data:
        if i.isalpha():
            start.update({i: -1}) # khởi tạo giá trị ban đầu
    
    data = data.replace('*', ' ')
    temp = data.split('=')  
    global result
    result = temp[1]
    result = result[::-1] #Đảo ngược kết quả

    #Tiếp theo là xử lý cắt tỉa chuỗi
    operands = temp[0].split(' ')  #Tách các toán hạng   
    MaxLenOpe = 0
    for i in range(len(operands)):
        operands[i] = operands[i][::-1] # Đảo ngược từng toán hạng để xử lý
        MaxLenOpe = max(len(operands[i]),MaxLenOpe) # tìm số hạng có độ dài lớn nhất     

    for i in range(0, len(result)):
        Col.append(list())
        impact.append(dict())

    #Duyệt từng phàn tử (chữ số) của từng toán hạng
    for i in range(0, len(operands[0])):
        for j in range(0, len(operands[1])):
            id = i + j # Tính toán ID của cột cho các ký tự hiện tại
            char1 = operands[0][i] # Lấy lần lượt các chữ số toán hạng thứ nhất operands[0]
            char2 = operands[1][j] # Lấy lần lượt các chữ số toán hạng thứ hai operands[1]

            # Thêm các chữ số vào các cột tương ứng 
            if char1 not in Col[id]:
                Col[id].append(char1)
            if char2 not in Col[id]:
                Col[id].append(char2)

            if char1 not in impact[id]:# Nếu char1 không có trong impact[id], thêm char1 làm khóa và đặt impact của char2 là 1
                impact[id].update({char1: {char2: 1}})
            else:
                if char2 not in impact[id][char1]: # Nếu char1 đã có trong impact[id] nhưng char2 chưa, thêm char2 với impact là 1
                    impact[id][char1].update({char2: 1})
                else: # Nếu cả char1 và char2 đều có trong impact[id], tăng impact của char2 lên 1
                    temp = impact[id][char1][char2] + 1
                    impact[id][char1].update({char2: temp})

    # Thêm các kí tự (node) của result vào các Col tương ứng
    for i in range(0, len(result)):
        if result[i] not in Col[i]:
            Col[i].append(result[i])
    
# Kiểm tra assgin của subproblem có thỏa hay không
# Nếu thỏa thì trả về carry
# Ngược lại, None
def CheckAssign(Col=list(), assign=dict(), factor=dict(), preCarry=0):
    posi = 0
    nega = 0
    for char in Col:
        posi = posi + assign[char]*factor[char][0]
        nega = nega + assign[char]*factor[char][1]
    tmp1 = posi + preCarry
    tmp2 = nega
    
    if tmp2 < 0:
        return None

    temp = tmp1%10 - tmp2%10

    if (temp == 0):
        return int(tmp1/10)-int(tmp2/10)
    return None    

def CheckAssignMultiplication(Col=list(), assign=dict(), subRes = "", factor=dict(), preCarry=0):
    sum = 0    
    for char1 in Col:
        if char1 in factor:
            for item in factor[char1].items():
                char2 = item[0]
                value = item[1]
                sum += assign[char1]*assign[char2]*value # Tính toán giá trị cho mỗi cặp (char1, char2) và cộng vào sum

    sum += preCarry # cộng thêm phần nhớ (preCarry) vào sum 
    if sum % 10 == assign[subRes]: # Kiểm tra nếu giá trị sum chia hết cho 10 và bằng với giá trị chữ số ở cột tương ứng trong kết quả (assign[subRes])
        return int(sum/10) # Trả về phần carry của phép nhân
    return None
    
def SolveCol(idxSub, carry, idx, localState=dict()):
    if idx == len(Col[idxSub]):
        temp = CheckAssign(Col[idxSub], localState, impact[idxSub], carry)
        if temp != None:
            rs = Solve(idxSub+1, localState, temp)
            if rs != None:
                return rs
        return None

    #Giải từng cột
    char = Col[idxSub][idx]
    rs = dict()

    if localState[char] == -1:
        for num in range(10):
            if num not in localState.values():
                if char == Col[len(Col)-1][0] and num ==0: # điều kiện kiểm tra chữ sô đầu tiên trong kết quả khác 0 hay không
                    continue
                localState[char] = num # gán giá trị num cho từng chữ số
                rs = SolveCol(idxSub, carry, idx+1, localState) #giải cột tiếp theo
                if rs != None:
                    return rs
                localState[char] = -1# Nếu phép gán không thỏa mãn, đặt lại giá trị của char thành -1 để thử phép gán khác
    else:
        rs = SolveCol(idxSub, carry, idx+1, localState) #Nếu char đã được gán giá trị trước đó, tiếp tục giải cột tiếp theo
    return rs

def SolveColMultiplication(idxSub, carry, idx, localState=dict()):
    if idx == len(Col[idxSub]):
        temp = CheckAssignMultiplication(Col[idxSub], localState,result[idxSub], impact[idxSub], carry)
        if temp != None:
            rs = Solve(idxSub+1, localState, temp)
            if rs != None:
                return rs
        return None
    
    #Giải từng cột
    char = Col[idxSub][idx]
    rs = dict()
    if localState[char] == -1:
        for num in range(10):
            if num not in localState.values():
                if char == Col[len(Col)-1][0] and num ==0: # điều kiện kiểm tra chữ sô đầu tiên trong kết quả khác 0 hay không
                    continue
                localState[char] = num # gán giá trị num cho từng chữ số
                rs = SolveColMultiplication(idxSub, carry, idx+1, localState) #giải cột tiếp theo
                if rs != None:
                    return rs
                localState[char] = -1# Nếu phép gán không thỏa mãn, đặt lại giá trị của char thành -1 để thử phép gán khác
    else:
        rs = SolveColMultiplication(idxSub, carry, idx+1, localState) #Nếu char đã được gán giá trị trước đó, tiếp tục giải cột tiếp theo
    return rs

def Solve(idxSub, state, carry):
    if len(state) > 10:
        return None

    if idxSub == len(Col):
        if carry == 0:
            return state
        else:
            return None
    StateStr = toString(state)
    if StateStr in StateSpace:
        return None
        
    if flag == 1:
        rs = SolveColMultiplication(idxSub, carry, 0, state)
    else: 
        rs = SolveCol(idxSub, carry, 0, state)
    StateSpace.add(StateStr)
    return rs

Col = list()
impact = list()
start = dict()
StateSpace = set()

start_time = time.time() #start tracking running time
data = GetInput("input.txt")
flag = 0
for i in data:
    if i== "*":
        flag = 1
if flag == 0:
    InitInput(data)
else: 
    InitInputMultiplication(data)
rs = Solve(0, start, 0)
F = open("result.txt",'w')
if rs != None:
    for item in sorted(rs.items(), key = lambda x: x[0]):
        F.write(str(item[1]))
else:
    F.write("NO SOLUTION")
F.close()
end_time = time.time() 
elapsed_time = end_time - start_time

print(rs)
print(f"Running time: {elapsed_time:.4f} seconds")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




