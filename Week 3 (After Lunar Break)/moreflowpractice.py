workingHours = float(input('Input working hours: '))
hourlyRate = float(input('Input the hourly rate: '))
if workingHours > 40:
    extraHours = workingHours - 40
    standardHours = (workingHours - extraHours)
    standardPay = standardHours * hourlyRate
    overtimePay = extraHours * (hourlyRate * 1.5)
    payAmount = standardPay + overtimePay
else:
    payAmount = workingHours * hourlyRate
print('$',payAmount)

# Now write this as an argument