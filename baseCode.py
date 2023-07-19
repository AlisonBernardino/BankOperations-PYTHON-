mainMenu = """

Welcome to the PrimePython Bank system v1.0

Please, select your desired operation: 

[W] = Withdraw
[D] = Deposit
[R] = Account report
[X] = Exit

"""

report = ""
accountBalance = 0
withdrawals_quantity = 0
deposits_quantity = 0
total_withdrawn_amount = 0
total_deposited_amount = 0
withdrawal_operations_limit = 3
withdrawal_operations_limit_index = 3
deposit_operations_limit = 5
deposit_operations_limit_index = 5
WITHDRAWAL_OPERATION_VALUE_LIMIT = 500
DEPOSIT_OPERATION_VALUE_LIMIT = 10000
total_daily_withdrawal_value_limit = 1500
total_daily_deposit_value_limit = 50000

while True:

    desiredOperation = input(mainMenu)

    if desiredOperation == "D":
        if deposit_operations_limit == 0:
            print("You have reached the daily deposit operations limit! Please, try again in 24h")
            break
        else:
            print("You have selected the DEPOSIT operation")
            depositValue = float(input("Please, insert the desired deposit amount: "))
        if depositValue > DEPOSIT_OPERATION_VALUE_LIMIT or depositValue <= 0:
            print("Invalid value! Please, insert a value between US$ 5,00 and US$ 10.000,00")
            break
        else:
            accountBalance += depositValue
            deposits_quantity += 1
            deposit_operations_limit -= 1
            total_deposited_amount += depositValue
            total_daily_deposit_value_limit -= depositValue
            print("Deposit operation success!")
            print(f"Deposit value: {depositValue:.2f}")
            print(f"Current balance: {accountBalance:.2f}")
            report += f"\n Deposit {deposits_quantity}: US${depositValue:.2f}"

    elif desiredOperation == "W":
        if withdrawal_operations_limit == 0:
            print("You reached the daily withdrawal operations limit! Please, try again in 24h")
            break
        else:
            print("You have selected the WITHDRAWAL operation")
            withdrawalValue = float(input("Please, insert the desired withdrawal amount: "))
        if withdrawalValue > WITHDRAWAL_OPERATION_VALUE_LIMIT or withdrawalValue <= 0:
            print("Invalid value! Please, insert a value between US$5,00 and US$500,00")
            break
        else:
            if accountBalance == 0 or withdrawalValue > accountBalance:
                print("Insufficient funds! Please, check your current balance and try again.")
                break
            accountBalance -= withdrawalValue
            withdrawals_quantity += 1
            withdrawal_operations_limit -= 1
            total_withdrawn_amount += withdrawalValue
            total_daily_withdrawal_value_limit -= withdrawalValue
            print("Withdrawal operation success!")
            print(f"Withdrawn value: US${withdrawalValue:.2f}")
            print(f"Current balance: US${accountBalance:.2f}")
            report += f"\n Withdrawal {withdrawals_quantity}: US${withdrawalValue:.2f}"

    elif desiredOperation == "R":
        print("You have selected the REPORT emission operation")
        print("============ OPERATIONS DETAILS ===============")
        print(report)
        print("============== TOTAL VALUES ===================")
        print("========== WITHDRAWAL operations ==============")
        print(f"Current account balance: US$ {accountBalance:.2f}")
        print("Performed withdrawal operations = ", withdrawals_quantity, "/", withdrawal_operations_limit_index)
        print(f"Total withdrawn value = US$ {total_withdrawn_amount:.2f}")
        print(f"Remaining withdrawal limit = US$ {total_daily_withdrawal_value_limit:.2f}")
        print("========== DEPOSIT operations =================")
        print("Performed deposit operations = ", deposits_quantity, "/", deposit_operations_limit_index)
        print(f"Total deposited value = US$ {total_deposited_amount:.2f}")
        print(f"Remaining deposit limit = US$ {total_daily_deposit_value_limit:.2f}")

    elif desiredOperation == "X":
        print("You have selected to EXIT the system. Ending your current session.")
        break

    else:
        print("Invalid operation! Please, select a valid option accordingly to the menu options to continue.")