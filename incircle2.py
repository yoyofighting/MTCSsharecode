from xlrd import open_workbook
import xlrd as xd
import pandas as pd
from pylab import *
from time import time


class Org:
    def __init__(self, x, y, p_id, cur_id, cur_name, children_list = []):
        self.x = x
        self.y = y
        self.p_id = p_id
        self.cur_id = cur_id
        self.cur_name = cur_name
        self.children_list = children_list

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_p_id(self):
        return self.p_id

    def get_cur_id(self):
        return self.cur_id
    
    def get_cur_name(self):
        return self.cur_name

    def get_children_list(self):
        return self.children_list

    def set_x(self,my_x):
        self.x = my_x

    def set_y(self,my_y):
        self.y = my_y

    def set_p_id(self,my_p_id):
        self.p_id = my_p_id

    def set_cur_id(self,my_cur_id):
        self.cur_id = my_cur_id

    def set_cur_name(self,my_cur_name):
        self.cur_name = my_cur_name

    def set_children_list(self,my_children_list = []):
        self.children_list= my_children_list

    def to_string(self):
        return "cur_id is : " + str(self.cur_id) + " | and the cur_name is : " + str(self.cur_name) + " and " \
                "the length of children's node is :" + str(len(self.children_list))

org_node_list = []
for src in initdata:
    org_node = Org(src[0],src[1],src[2],src[3],src[4])
    org_node_list.append(org_node)


def construct_tree(root_list:Org):
    list_len = len(root_list)
    out_start = 0
    while out_start < list_len:
        node = root_list[out_start]
        tmp_children_list = []
        inner_start = 0
        while inner_start < list_len:
            node1 = root_list[inner_start]
            if node.get_cur_id() == node1.get_p_id() and node1.get_cur_id() != node1.get_p_id()  :
                tmp_children_list.append(root_list[inner_start])
            inner_start += 1
        root_list[out_start].set_children_list(tmp_children_list)
        out_start += 1

    return root_list


def get_node_from_value(node_id, node_list : Org =[]):
    if len(node_list) == 0 :
        return
    else:
        for node in node_list:
            if node.get_cur_id() == node_id:
                return node
            else:
                continue
        return None


def display_node(ele:Org,space_num = 0 ):
    print("\t" * space_num +"" + ele.get_cur_name())
    if len(ele.get_children_list()) == 0 :
        return
    else:
        space_num += 1
        for ch_ele in ele.get_children_list():
            display_node(ch_ele,space_num)


def get_children_node(ele:Org, children_node_list = []):
    if len(ele.get_children_list()) == 0 :
        return
    else:
        for ch_ele in ele.get_children_list():
            children_node_list.append(ch_ele)
            get_children_node(ch_ele,children_node_list)
    return children_node_list


def getlenth():
    get_children_node(ele)
    return len(children_node_list)


def getwji(children_node_list=[]):
    if children_node_list != None:
        aaa = len(children_node_list)
    else:
        aaa = 0
    return aaa


childset = []
for index in range(i):
    index = index + 1
    a = V[index][3]
    org_node_list = []
    children_node_list=[]   
    for src in initdata:
        org_node = Org(src[0],src[1],src[2],src[3],src[4])
        org_node_list.append(org_node)
    res_tree = construct_tree(org_node_list)
    node_res = get_node_from_value(a,res_tree) 
    children_node_list = get_children_node(node_res, children_node_list)
    print(children_node_list)
    aaa = getwji(children_node_list)
    childset.append(aaa)
print("The children set of inner-ring nodes:")
print(childset)

# The weight of the children
WJI = []
for index in range(i):
    wji = childset[index] / len(V)
    WJI.append(wji)
print("The weight of the children:")
print(WJI)

# The energy consumption rate
R = []
for index in range(len(V)):
    index = index + 1
    roui = rec * V[index][5] + tra * V[index][6] + sen * V[index][7]
    R.append(roui)
print("The energy consumption rate:")
print(R)

# Sorted by the joint priority
H = []
Dmax= D[-1]
for index in range(i):      
    Eresi = Emax - R[index] * t
    if Eresi > 0.5 * Emax:
        hi = (WJI[index] + WSI[index]) * ((Dmax - D[index]) / Dmax)
    hi = (WJI[index] + WSI[index]) * ((Emax - Eresi) / Emax)
    H.append(hi)
H.sort()
print("The set of the space or time priority:")
print(H)

# The charging cycle    
Rmax = max(R)
for index in range(i):
    T = (Emax - Emin) / (Rmax * (1 - Rmax / Uc))
print("The charging cycle:")
print("%.2f" % T)

# The charging time of each inner-ring nodes
Tset = []
for index in range(i):
    Ti = T * R[index] / Uc
    Tset.append(Ti)
print("The set of the charging time of each inner-ring nodes:")
print(Tset)

# The charging failure rate of the inner ring:
idead = 0
for index in range(i):
    if Emax - (T - Tset[index]) * R[index] < Emin:
        idead += 1
print("The number of the dead nodes in the inner ring:")
print(idead)
ideadrate = idead / i
print("The charging failure rate of the inner ring:")
print(ideadrate)

# The energy efficiency of the inner ring:
for index in range(i):
    Tchar += Tset[index]
    Qchar += Qchari
ieita = (Tchar * Uc)/(Tchar * Uc + TOTAL[-2] * Um)
print("The energy efficiency of the inner ring:")
print(ieita)

# The task delay of the inner ring:
idelay = TOTAL[-2] / Vm



