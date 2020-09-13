'''
    在 classVariable.py 中，我們使用 instance variable 跟 class variable。
    那當然就會有:
    1.  一般的 method  (自動傳入 instance argument，我們通常給他 self 這個名字)  
    2.  class method   (自動傳入 class argument，我們通常給他 cls 這個名字)
    3.  static method  (不自動傳入 argument，要的話自己加)。 舉例看第 34 行。
'''
''' 
    借用 classVariable.py 的 code。
    在第 11 行，我們果想更改 raise_amount，可以直接改，或是使用 class method，
    詳看第 24 行。
'''

class Employee:
    nums_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.nums_of_emp += 1
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount )
    @classmethod # 關鍵字
    def set_raise_amount(cls, amount): # cls 參數功能跟 self 很像。self 代表對 class 的 instance 做動作。cls 代表對整個 class 做動作。
        cls.raise_amount = amount # 將 class 的(在目前它叫做 cls) raise_amount 設為 amount。
    @classmethod 
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # 記得要 return 轉換完的 class object。
    @staticmethod
    def is_workday(day): # day 是我們自己定義的 argument。
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True

Employee.set_raise_amount(1.05)
print(Employee.raise_amount) # 印出 1.05。

# 有人會將 class method 最為替代的 constructor:
# 比如現在員工的資料用以下方式表達，你的任務是將它放在 Employee 這個 class:
emp_str_1 = 'John-Doe-70000'
# 你可以這樣做:
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.first) # 印出 John
# 但如果有很多個，這樣做很沒效率，解決方法在第 31 行。
    
emp_str_2 = 'John-Cena-200000'
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.last) # 印出 Cena。

import datetime
myDate = datetime.date(2020, 8, 21)
print(Employee.is_workday(myDate))