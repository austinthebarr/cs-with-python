# Find the lowest payment to pay off credit card balance
#balance = 320000; annualInterestRate = 0.2

def cal(balance, annualInterestRate, payment):
   i = 1
   while i <= 12:
        balance = balance - payment
        monthly = (annualInterestRate/12.0) * balance
        balance = balance + monthly
        i += 1
   return balance


def bi(balance, annualInterestRate):
    monthlyIntrestRate = (annualInterestRate/12.0) 
    startBal = balance
    low = balance / 12
    high = balance * (1 + monthlyIntrestRate)**12 /12.0 
    while True:
   
        payment = (low + high) / 2.0
       
        balance = cal(balance, annualInterestRate, payment)
        if balance <= -0.12:
            high = payment  
            balance = startBal 
            
        elif balance > 0:
            low = payment
            balance = startBal 
        else:
            break 
    print('Lowest Payment:', round(payment,2))

