def operacion(num1,num2,oper):
    if oper=="+":
        resultado=num1+num2
    elif oper=="-":
        resultado=num1-num2
    elif oper=="*":
        resultado=num1*num2
    elif oper=="/":
        resultado=num1/num2
    return resultado
def main():
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    oper=input("Ingrese la operacion (+, -, *, /): ")
    cuenta=operacion(num1,num2,oper)
    print(num1,oper,num2,"=",cuenta)
main()