# Final Sprint Code
# Authors: Joshua Hayward, Tre Bullock, Alex Dalton, Cole Hickey, Abigayle O'Connell, Tristan Baily
# Date: 2022-12-21

import datetime
# List Selection prints, user will input number on the left.
print(" ")
print("   Hab Taxi Service")
print("   Company Service System")
print("   1. Enter a New Employee")
print("   2. Enter Company Revenues")
print("   3. Enter Company Expenses")
print("   4. Track Car Rentals")
print("   5. Record Employee Payment")
print("   6. Print Company Profit Listing")
print("   7. Print Driver Financial Listing")
print("   8. Driver Ratings")
print("   9. Quit")

while True:
    Choice = int(input("Please enter one of the numbered options above (1-9): "))
    if Choice < 1:
        print("Please enter a number that is on the list.")
    elif Choice > 9:
        print("Please enter a number that is on the list.")
    else:
        break

    f = open("Defaults.dat", "r")
    TransactNum = int(f.readline())
    NextDriverNum = int(f.readline())
    MonthlyStandFee = float(f.readline())
    DailyRentalFee = float(f.readline())
    WeeklyRentalFee = float(f.readline())
    HST_RATE = float(f.readline())
    f.close()

def NewEmplo():
    f = open("Defaults.dat", "r")
    TransactNum = int(f.readline())
    NextDriverNum = int(f.readline())
    MonthlyStandFee = float(f.readline())
    DailyRentalFee = float(f.readline())
    WeeklyRentalFee = float(f.readline())
    HST_RATE = float(f.readline())
    f.close()


    while True:
        # Inputs
        EmployFName = input("Enter The First Name of the Employee: ")
        EmployLName = input("Enter The Last Name of the Employee: ")
        EmployAdd = input("Enter the Current Address of the Employee (ex. 13 BillyBob str St. Johns): ")
        EmployPhoneNum = input("Enter the Employees Current Phone Number (XXX-XXX-XXXX): ")
        DriverLicNum = input("Enter the Employees Driver Licence Number: ")
        DriverLicNumExpDate = input("Enter the Expiry Date for the Employees Driver Licence Number(YYYY-MM-DD): ")
        InsurePoliComp = input("Enter the Employees insurance Policy Company: ")
        PolicyNum = input("Enter the Company Policy Number: ")

        # Calculations
        BalanceDue = 0
        RentalFee = 0
        RentTime = 0
        while True:
            EmpCarStatus = input("Enter Y if the employee owns a Vehicle, enter N if not: ").upper()
            if EmpCarStatus == "Y":
                if EmpCarStatus == "Y":
                    BalanceDue = MonthlyStandFee
                    break
                break

            else:
                RentTime = int(input("Enter how long you will be renting a car for (1-7): "))
                if EmpCarStatus != "Y":
                    BalanceDue = RentalFee * RentTime
                    break
                break
        while True:
            if RentTime != 7:
                RentalFee = RentTime * DailyRentalFee
            else:

                RentalFee = 300
            break
        BalanceDue = RentalFee + BalanceDue

        # Additions
        f = open("NewEmployees.dat", "a")

        f.write("{}, ".format(NextDriverNum))
        f.write("{}, ".format(EmployFName))
        f.write("{}, ".format(EmployLName))
        f.write("{}, ".format(EmployAdd))
        f.write("{}, ".format(EmployPhoneNum))
        f.write("{}, ".format(DriverLicNum))
        f.write("{}, ".format(DriverLicNumExpDate))
        f.write("{}, ".format(InsurePoliComp))
        f.write("{}, ".format(PolicyNum))
        f.write("{}, ".format(EmpCarStatus))
        f.write("{}\n ".format(str(BalanceDue)))

        print()
        print("Data saved.")

        NextDriverNum += 1
        # Write Backs
        f = open("Defaults.dat", "w")

        f.write("{}\n ".format(str(TransactNum)))
        f.write("{}\n ".format(str(NextDriverNum)))
        f.write("{}\n ".format(str(MonthlyStandFee)))
        f.write("{}\n ".format(str(DailyRentalFee)))
        f.write("{}\n ".format(str(WeeklyRentalFee)))
        f.write("{}\n ".format(str(HST_RATE)))

        f.close()


        End = input("Press any key to enter another employee, type END to finish the program: ").upper()
        if End == "END":
            break

def Reviews():
    RatingID = input("Thank you for choosing to leave a review, please enter the NumberID for the driver that you wish to comment on: ")
    print("1. Very Poorly")
    print("2. Below Average")
    print("3. Average")
    print("4. Above Average")
    print("5. Great")
    RateChoice = int(input("Please pick a number below that would describe your experience: "))
    if RateChoice == 1:
        RateChoice = "Very Poor"
    if RateChoice == 2:
        RateChoice = "Below Average"
    if RateChoice == 3:
        RateChoice = "Average"
    if RateChoice == 4:
        RateChoice = "Above Average"
    if RateChoice == 5:
        RateChoice = "Great"

    ReviewComment = input("If you would like to leave any comments about your experience please feel free: ")
    print("Thank you for the feedback!")

    f = open("Reviews.dat", "a")
    f.write("{}, ".format(str(RatingID)))
    f.write("{}, ".format((RateChoice)))
    f.write("{}\n ".format((ReviewComment)))
    f.close()

def ProfitList():
    CompanyName = "HAB Taxi Services"
    CompAddress = "276 Elizabeth Avenue, St. John's NL"
    Spacer = "==============================================="
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    ProfitHeader = 'Profit Listings'

    # Operating Expenses
    print(" ")
    print("Habs Taxi Service")
    print("276 Elizabeth Avenue")
    print("St. John's, NL")
    print(date_time)
    print("="*66)
    print("Profit Listing")
    print("view: Annual Data")
    print("="*66)
    print("Period Ending:               MM-DD-YYYY      MM-DD-YYYY")
    print("Total Revenue:               XXXXXXX.XX      XXXXXXX.XX")
    print("Cost of Revenue:             XXXXXX.XX       XXXXXX.XX")
    print("="*66)
    print("Operating Expenses")
    print("     Driver Salary           $#######.##     $#######.##")
    print("     Vehicle Maintenance     $#######.##     $#######.##")
    print("     Fuel                    $#######.##     $#######.##")
    print("Insurance                    $#######.##     $#######.##")
    print("Others                       $#######.##     $#######.##")
    print("Total Operating Expenses     $#######.##     $#######.##")
    print("="*66)
    print("Operating Profit/Loss")
    print("Vehicle Rentals              XXXXXXXXXX.XX   XXXXXXXXXX.XX")
    print("Cab Services                 XXXXXXXXX.XX    XXXXXXXXX.XX")
    print("="*66)
    print("Net Income                   XXXXXXXXXXXXXX.XX   XXXXXXXXXXXXXX.XX")
    print("="*66)


if Choice == 1:
    NewEmplo()

if Choice == 6:
    ProfitList()

if Choice == 8:
    Reviews()