# 這章節比較混亂，可重複看: https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6

# 借用之前的 Employee class:

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + '@email.com' # 在創建好 email property 後就不需要了。
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @fullname.setter # 你要動的 method.setter
    def fullname(self, name): # 注意: setter method 的名字必須跟你要動的 method 名問吻合。
        first, last = name.split(' ')
        self.first = first
        self.last = last
    # 定義完後執行第 36 行，就成功了。

    @fullname.deleter # 你要動的 method.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('Kobe', 'Bryant', 50000) # 給定員工參數

emp_1.first = 'Gigi' 
'''
    如果我們對 instance 的 attribute(first) 做修改。email attribute 並不會改變(仍印出 Kobe.Bryant@email.com)
    一個解決方法是創一個類似 fullname() 的 method，用來正確回傳 email。但這樣做必須在之前的 code 都加一個 ()，很麻煩。
    Property 可以讓我們定義一個 attribute like a method。
    語法詳看第 12 行。
'''
'''
    那如果今天我想對 class 裡的 method 做修改[將 method 當作是 attribute]，則可以用 setter
    語法詳看第 16 行。
'''

'''
    進一步，想要再刪除 instance，做清洗的動作，可以用 deleter。
    語法詳看第 26 行。
'''
emp_1.fullname = 'Lebron James'

print(emp_1.first)
print(emp_1.fullname) # 在還沒加 fullname setter 前，是要加括號的(他仍被 treat 為 method)
print(emp_1.email) # 加了 email property 後，印出 Gigi.Bryant@email.com [沒加會印出 Kobe.Bryant@email.com]

del emp_1.fullname # 印出 Delete Name!
