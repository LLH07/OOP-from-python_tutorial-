# 我們可以用 special methods 來做 operator overloading。而 Special(dunder) methods 都是以 ' __ ' 來表示。
# 舉例一: __repr__() 是用在 debugging。它可以讓你在 print(某 class 的 instance) 時不那麼 ambiguous。[str() 是讓 code readable] (請看 https://www.youtube.com/watch?v=5cvM-crlDvg)
# 看第 15 行。
class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def __repr__(self): # 讀作 dunder repr method。
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self): # 讀作 dunder str method。
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay



emp_1 = Employee('Kobe', 'Bryant', 50000)
emp_2 = Employee('Lebron', 'James', 60000)

print(emp_1) 

print(emp_1.__repr__()) # 印出 Employee('Kobe', 'Bryant', 50000)
print(emp_1.__str__()) # 印出 Kobe Bryant - Kobe.Bryant@email.com

# 與上兩個 print() 相同。
print(repr(emp_1))
print(str(emp_1))
'''
    印出 <__main__.Employee object at 0x022964F0>。這是很 ambiguous 的，應該改成簡單一點的表示方法。 
    我在這裡遇到一個問題: 當我 def __repr__(self) 並 pass 時，出現錯誤: TypeError: __str__ returned non-string (type NoneType)。但當我 comment out 後就錯誤就解除了。
    當定義完 __repr__() 後再執行一次，此時就會印出: Employee('Kobe', 'Bryant', 50000) string。你可以直接複製，製造出 emp_1 的真實樣貌。
'''

# 現在講所學與 operator overloading 作連結:
print(1 + 2) # 印出 3。
print(int.__add__(1, 2)) # 事實上，上一行在作的是這件事。仔細看，跟上面的 emp1.__repr__() 格式很像。[都是 class.dunder method]

# 在第 21 行新增自定義的加法:
print(emp_1 + emp_2) # 印出 110000

# 更多資訊: https://docs.python.org/3/reference/datamodel.html#special-method-names


