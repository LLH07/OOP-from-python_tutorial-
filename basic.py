'''
data: 在 class 內稱為 attribute。
function: 在 class 內稱為 method。

每個 class 裡的 method，都必須加上一個 instance 最為 argument，傳統上我們用
self。

在 python，__init__ method 可以想成是 constructor。
有區分所謂的 instance variable，class variable。
'''

# 下面的觀念是基石:

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Cena', 50000) # 創造 instance variable。

print(emp_1.fullName()) # fullName 是一個 method，要記得加括號。
print(Employee.fullName(emp_1))

'''
    兩者都會印出 John Cena，下面的 print 解釋為何每個 class 的 method，
    都要加入 self 參數，否則會跳出錯誤訊息。
    比如我寫: 
        def fullName():
            return '{} {}'.format(first, last)
        emp_1 = Employee('Lebron', 'James', 2000000)
        print(emp_1.fullName()) 
    這樣會得出: TypeError: fullName() takes 0 positional arguments but 1 was given
    因為第 33 行在我創造 emp_1 時，會自動被傳入到其 class 的 method。但在第 31 行我不
    給 method 任何參數。
'''