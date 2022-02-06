import argparse

#create parser
parser=argparse.ArgumentParser()
#add arguements
parser.add_argument("--number1",type=int,help="number1")
parser.add_argument("--number2",type=int,help="number2")
parser.add_argument("--operation",type=str,help="type of operation you want to execute")
#execute
args=parser.parse_args()
#function
def addition(number1,number2):
    print(number1+number2)
def subraction(number1,number2):
    print(number1-number2)
def multiplication(number1,number2):
    print(number1*number2)
def division(number1,number2):
    print(number1/number2)    
#calling function
if args.operation=="+":
    addition(args.number1,args.number2)
elif args.operation=="-":
    subraction(args.number1,args.number2)
elif args.operation=="*":
    multiplication(args.number1,args.number2)
elif args.operation=="/":
    division(args.number1,args.number2)                

