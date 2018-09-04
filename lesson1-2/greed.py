#coding = utf-8

## 数据结构
class Cargo(object):
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price
        self.status = 0
    
    def __str__(self):
        return "(%d, %d, %d)" % (self.weight, self.price, self.status)
    def __repr__(self):
        return "(%d, %d, %d)" % (self.weight, self.price, self.status)
    
class Package(object):
    def __init__(self, cargos, totalC):
        self.cargo_list = cargos[:]
        self.totalC = totalC
    def __str__(self):
        return "%s" % self.cargo_list
    def __repr__(self):
        return "%s" % self.cargo_list
    
## 物品价值最高
def func_price(cargos):
    index = -1
    mp = 0
    for i in range(len(cargos)):
        if cargos[i].status == 0 and cargos[i].price > mp:
            mp = cargos[i].price
            index = i
    return index

## 物品重量最轻
def func_weight(cargos):
    index = -1
    mw = 0
    for i in range(len(cargos)):
        if mw == 0 and cargos[i].status==0:
            mw = cargos[i].weight
            index = i
        if cargos[i].status == 0 and cargos[i].weight < mw:
            mw = cargos[i].weight
            index = i
    return index

## 价值密度比
def func_density(cargos):
    index = -1
    mv = 0.0
    for i in range(len(cargos)):
        density = cargos[i].price/cargos[i].weight
        if cargos[i].status ==0 and density > mv:
            mv = density
            index = i
    return index


def greedyAlgo(package, func_policy):
    inx_list = []
    ntc = 0
    
    while True:
        idx = func_policy(package.cargo_list)
        if idx == -1:
            break
        if ntc + package.cargo_list[idx].weight <= package.totalC:
            print("select item:", idx)
            package.cargo_list[idx].status = 1
            ntc += package.cargo_list[idx].weight
        else:
            package.cargo_list[idx].status = 2
    print(package)
    
if __name__ == '__main__':
    
    # 初始化物品，包裹
    wi= [35, 30, 60, 50, 40, 10, 25]
    pi= [10, 40, 30, 50, 35, 40, 30]
    items_zip = zip(wi, pi)
    
    item_list = []
    for c in items_zip:
        item_list.append(Cargo(*c))
    pack = Package(item_list, 150)
    
    # 选取一种挑选规则方法
    greedyAlgo(pack, func_weight)
    