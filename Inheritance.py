# 借用 Employee 這個 class:

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # Employee.nums_of_emp += 1
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount )

# 現在我想要創 developer, manager 這兩個 class。我們發現這兩種人都是用 Employee 這個 class，因此要借用 Employee:
    # 當你創建一個從別的 class inheriate 來的 class，當要取得此 class 的內容時，Python 會先在目前 class 找，如果沒找到，則會到你 inheriate 來的 class 找。
    # 可以用 help() 來看繼承的狀況。
class Developer(Employee): # 括弧內的 Employee 表示 Developer 是從 Employee inheriate 來的。
    raise_amt = 1.10 # 即使你在 Developer class 更改了 raise_amt，原本 Employee class 的 raise_amt 仍不會變。

    def __init__(self, first, last, pay, prog_lang):
    
        super().__init__(first, last, pay)
        ''' 
            如果我們想在 Developer 初始化中多增加使用的語言(但 first, last, pay 是一樣的)，可以用如上寫法。
            邏輯是讓 Employee 的 __init__ 去 handle 一樣的 arguments。
            也可以寫: Employee.__init__(self, first, last, pay)
        '''
        self.prog_lang = prog_lang

# 創建 Manager class，其包含一個 employees list。
class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def show_emp(self):
        for e in self.employees:
            print(e)
# 第 33 在 init 時，把 employees 設為 None，而不是空的 list。這是因為 list 是 immutable(不可變的)。



print(help(Developer))
dev_1 = Developer('Blair', 'Lin', 50000, 'Python')
print(dev_1.prog_lang)

mgr_1 = Manager('Kobe', 'Bryant', 25000, [])
mgr_1.add_emp('Corey Shafer')
mgr_1.add_emp('Tony Blair')
mgr_1.remove_emp('Corey Shafer')
mgr_1.show_emp()

# isinstance() 與 issubclass()
print(isinstance(mgr_1, Employee)) # 印出 True。因為 mgr_1 是 Employee 的一個 instance。
print(issubclass(Manager, Developer)) # 印出 False。因為 Manager 並不是 Developer 的 sub class。
print(issubclass(Developer, Employee)) # 印出 True。因為 Developer 是 Employee 的 sub class。

 


