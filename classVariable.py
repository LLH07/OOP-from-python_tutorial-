# 在 basic.py 中介紹了 instance variable，這篇文章要介紹 class variable。
# 借用 Employee。現在假設有一些資料對所有員工都適用，比如調薪的比例，這時就可
# 以用 class variable(看第 5 行)。 
class Employee:
    nums_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.nums_of_emp += 1 # 一定要注意，不是 self.nums_of_emp，因為你是改整個 class，而不是個別的 instance。
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount ) # 當然可以直接打 1.04，但要修改就很麻煩。
        '''
            如果直接打 raise_amount，會出現 NameError: name 'raise_amount' is not defined
            因此要加 Employee.raise_amount 或 self.raise_amount。
            為何 instance 可以拿取 class 的資料? 這是因為當一個 instanace 嘗試取得其 class 的 attribute，他會先找自己是否有這個 atttribute，如果自己沒有
            他會去 class 找。
            因此若想在個別的 employee 給不同的調薪比例，應該用 self.raise_amount。
        '''

emp_1 = Employee('Jon', 'Cena', 200000)

'''
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay) # 印出 208000
print
'''


emp_1.raise_amount = 1.05 # 如果寫 Employee.raise_amount = 1.05，那全部都會變 1.05 了。
print(Employee.raise_amount) # 1.04
print(emp_1.raise_amount) # 1.05。因為 emp_1 這個 instance，在自己裡面就發現 raise_amount 這個 atttribute，其值是 1.05。

# 相對的，若 attribute 在所有 empolyee 都通用(比如公司的總人數)，則可以直接改 employee 的 class variable。詳看第 5 行及第 12 行。
print(Employee.nums_of_emp) # 印出 1。來自於第 25 行。
emp_2 = Employee('Tony', 'Blair', 30000)
print(Employee.nums_of_emp) # 印出 2。