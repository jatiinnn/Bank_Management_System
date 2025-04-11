import mysql.connector as a
from mysql.connector import Error

try:
    con = a.connect(
        host='localhost',
        port='3306',
        user='root',
        passwd='',
        database='college_project6'
    )

    # if con.is_connected():
        # print('yes')

    print('*' * 65)
    print(' ' * 25, end=' ')
    print('Bank Management System')
    print('*' * 65)

    cursor = con.cursor()

    def accdetails():
        try:
            name = input('Enter Your Name : ')
            accno = input('Set Your 10-Digits Account Number : ')
            dob = input('Enter Your Date Of Birth (YYYY-MM-DD) : ')
            add = input('Enter Your Address : ')
            phno = input('Enter Your Phone Number : ')
            openbal = int(input('Enter Account Opening Balance : '))
            tupple1 = (name, accno, dob, add, phno, openbal)
            tupple2 = (name, accno, openbal)

            acctable = 'INSERT INTO account_details VALUES(%s, %s, %s, %s, %s, %s)'
            amtable = 'INSERT INTO amount VALUES(%s, %s, %s)'
            cursor.execute(acctable, tupple1)
            cursor.execute(amtable, tupple2)
            con.commit()
            print('Congratulations!! \nYour Account opened Successfully')
        except Exception as e:
            print('Error:', e)
        main()

    def depositeamount():
        try:
            amount = int(input('Enter Amount : '))
            accno2 = input('Enter Your Account Number : ')
            cursor.execute('SELECT Balance FROM amount WHERE Account_Number=%s', (accno2,))
            output = cursor.fetchone()
            if output:
                new_balance = output[0] + amount
                cursor.execute('UPDATE amount SET Balance=%s WHERE Account_Number=%s', (new_balance, accno2))
                con.commit()
                print('Congratulations!! \nAmount deposited Successfully')
            else:
                print("Account not found.")
        except Exception as e:
            print('Error:', e)
        main()

    def withdrawamount():
        try:
            amount = int(input('Enter Amount : '))
            accno2 = input('Enter Your Account Number : ')
            cursor.execute('SELECT Balance FROM amount WHERE Account_Number=%s', (accno2,))
            output = cursor.fetchone()
            if output and output[0] >= amount:
                new_balance = output[0] - amount
                cursor.execute('UPDATE amount SET Balance=%s WHERE Account_Number=%s', (new_balance, accno2))
                con.commit()
                print('Amount withdrawn Successfully')
            elif output:
                print('Insufficient balance.')
            else:
                print('Account not found.')
        except Exception as e:
            print('Error:', e)
        main()

    def accountbalance():
        try:
            accno3 = input('Enter Your Account Number : ')
            cursor.execute('SELECT Balance FROM amount WHERE Account_Number=%s', (accno3,))
            output = cursor.fetchone()
            if output:
                print(f'Current Balance for Account {accno3} is: {output[0]}')
            else:
                print('Account not found.')
        except Exception as e:
            print('Error:', e)
        main()

    def customersdetails():
        try:
            accno4 = input('Enter Your Account Number : ')
            cursor.execute('SELECT * FROM account_details WHERE Account_Number=%s', (accno4,))
            output = cursor.fetchone()
            if output:
                fields = ['Name', 'Account Number', 'DOB', 'Address', 'Phone Number', 'Opening Balance']
                for label, val in zip(fields, output):
                    print(f"{label}: {val}")
            else:
                print('Account not found.')
        except Exception as e:
            print('Error:', e)
        main()

    def closeaccount():
        try:
            accno5 = input('Enter Your Account Number : ')
            cursor.execute('DELETE FROM account_details WHERE Account_Number=%s', (accno5,))
            cursor.execute('DELETE FROM amount WHERE Account_Number=%s', (accno5,))
            con.commit()
            print('Your Account Closed Successfully')
        except Exception as e:
            print('Error:', e)
        main()

    def main():
        try:
            print("""
 1. Open New Account 
 2. Deposit Amount 
 3. Withdraw Amount 
 4. Account Balance 
 5. Customer's Details 
 6. Close Account
            """)
            choice = input('Enter Task Number : ')
            if choice == '1':
                accdetails()
            elif choice == '2':
                depositeamount()
            elif choice == '3':
                withdrawamount()
            elif choice == '4':
                accountbalance()
            elif choice == '5':
                customersdetails()
            elif choice == '6':
                closeaccount()
            else:
                print('Invalid Task Number. Please try again.')
                main()
        except Exception as e:
            print('Unexpected error:', e)

    main()

except Error as e:
    print("Error while connecting to MySQL", e)
