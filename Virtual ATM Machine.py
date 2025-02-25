balance = 5000  
print("\n🏧 Welcome to the Virtual ATM!\n")

while True:
    print("\nChoose an option:")
    print("1-> Check Balance")
    print("2-> Withdraw Money")
    print("3-> Deposit Money")
    print("4-> Exit")
    
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        print(f"\n💰 Your current balance is: Rs.{balance}")

    elif choice == 2:
        amount = int(input("\nEnter amount to withdraw: Rs."))
        if amount > balance:
            print("\n⚠️ Insufficient balance! Withdrawal failed.")
        else:
            balance -= amount
            print(f"\n✅ Withdrawal successful! Remaining balance: Rs.{balance}")
    
    elif choice == 3:
        amount = int(input("\nEnter amount to deposit: Rs."))
        balance += amount
        print(f"\n✅ Deposit successful! New balance: Rs.{balance}")
    
    elif choice == 4:
        print("\n🔴 Thank you for using the Virtual ATM! Goodbye!\n")
        break  
    
    else:
        print("\n❌ Invalid choice! Please enter a number between 1-4.")




        