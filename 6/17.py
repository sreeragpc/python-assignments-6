""" Write a menu driven program to do the basic mathematical operations such as addition, subtraction, multiplication and division (hint: use if else ladder or switch)
Program should have 4 functions named addition(), subtraction(), multiplication() and division()
Should create a class object and call the appropriate function as user prefers in the main function
"""
print("Select any one of the function\n"
      "1-addition\n"
      "2-substraction\n"
      "3-multiplication\n"
      "4-division")
choice=int(input("select an operation:"))
print("enter 2 numbers")
num1=int(input("enter number 1 = "))
num2=int(input("enter number 2 = "))
class operations:
      def addition(self,k,m):
            self.k=k
            self.m=m
            result=k+m
            return result
      def substraction(self,k,m):
            self.k = k
            self.m = m
            result=k-m
            return result
      def multiplication(self,k,m):
            self.k = k
            self.m = m
            result=k*m
            return result
      def division(self,k,m):
            self.k = k
            self.m = m
            result=k+m
            return result

x=operations()
if choice==1:
      a=x.addition(num1,num2)
      print("result = "+str(a))
elif choice==2:
      a = x.substraction(num1,num2)
      print("result = " + str(a))
elif choice==3:
      a = x.multiplication(num1,num2)
      print("result = " + str(a))
elif choice==4:
      a = x.division(num1,num2)
      print("result = " + str(a))
else:
      print("you have choosen an invalid operation")

