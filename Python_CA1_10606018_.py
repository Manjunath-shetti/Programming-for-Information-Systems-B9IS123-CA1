import unittest


#creating class- Employee
class Employee:
    def __init__(self, staff_Id, last_name, first_name,Reg_hours, hourly_rate, OT_multiple, Tax_credit, Standard_band):

        # initialising- data members of class Employee
        self.staff_Id = staff_Id
        self.last_name = last_name
        self.first_name = first_name
        self.Reg_hours = Reg_hours
        self.hourly_rate = hourly_rate
        self.OT_multiple = OT_multiple
        self.Tax_credit = Tax_credit
        self.Standard_band = Standard_band


    #creating Method omputepayment, further Passing the Parameters
    def computePayment(self, worked_hours, Date):

        # creating and initialising the variables
        # if standard tax rate is 20%
        # then 20/100=0.2  [Hence, standard_pay = 0.2]
        # if higher tax rate is 40%
        # then 40/100=0.4 [Hence, higherTaxRate = 0.4]
        # if higher tax rate is 4% then
        # 4/100=0.04 [Hence, PRSIrate = 0.04]


        overtime_hours, regularpay, overtime_pay, Overtime_Rate, grossPay, standard_pay, standardTax, netPay = 0, 0, 0, 0, 0, 0, 0, 0
        standardTaxRate, higherRatePay, higherTax, higherTaxRate, totalTax, netTax, PRSIrate, netdeduction = 0.2, 0, 0, 0.4, 0, 0, 0.04, 0


       #{}- Empty Ditionary for storing the Data
        Employee_Details = {}

        # if hours worked Exceeds regular hours then the variation between Regular hours and worked hours are stored in Overtime hours
        #else Regular hours will be equal to Worked hours
        if worked_hours > self.Reg_hours:
            overtime_hours = worked_hours - self.Reg_hours
        else:
             self.Reg_hours = worked_hours

        # over time rate is calculated by multiplying  OTMultiple and hourly rate
        Over_time_Rate = self.OT_multiple * self.hourly_rate

        #  regular hours are multiplied with  hourly rate and stored in regular pay
        regularpay = self.Reg_hours * self.hourly_rate

        # Over time hours is multiplied with Overtime rate and stored in Overtime_pay
        Overtime_pay = overtime_hours * Overtime_Rate

        #gross pay is obtained by adding Regularpay and Overtimepay
        grossPay = regularpay + Overtime_pay

        # if gross pay exceeds standard band then standard Tax will be 20% of  standard band else standardTax  will be 20% of grosspay

        if grossPay > self.Standard_band:
          standardTax = standardTaxRate * self.Standard_band

        #variation between Grosspay and standard band is higherRatePAy
          higherRatePay = grossPay - self.Standard_band
        else:
            standardTax = grossPay * standardTaxRate

       #Higher Tax is obtained by multiplying Higher Tax rate and Higher rate Pay
        higerTax = higherTaxRate * higherRatePay

        #Total Tax obtained by adding Higher Tax and Higher rate pay
        totalTax = higerTax + higherRatePay


    # if total Tax is greater than tax credit
    # then Net tax obtained by subtarating Totaltax - Tax redit
    # if not then net tax will be totaltax

        if (totalTax > self.Tax_credit):
            netTax = totalTax - self.Tax_credit
        else:
            netTax = totalTax

        # PRSI
        PRSI = PRSIrate * grossPay


        netdeduction = netTax + PRSI


        netPay = grossPay - netdeduction


        Employee_Details["name"] = self.last_name + " " + self.first_name
        Employee_Details["Date"] = Date
        Employee_Details['Regular Hours Worked'] = self.Reg_hours
        Employee_Details["Overtime Hours Worked"] = overtime_hours
        Employee_Details["Regular Rate"] = self.hourly_rate
        Employee_Details["Overtime Rate"] = Overtime_Rate
        Employee_Details["Regular Pay"] = regularpay
        Employee_Details["Overtime Pay"] = Overtime_pay
        Employee_Details["Gross Pay"] = grossPay
        Employee_Details["Standard Rate Pay"] = self.Standard_band
        Employee_Details["Higher Rate Pay"] = higherRatePay
        Employee_Details["Standard Tax"] = standardTax
        Employee_Details["Higher Tax"] = higherTax
        Employee_Details["Total Tax"] = (totalTax)
        Employee_Details["Tax Credit"] = self.Tax_credit
        Employee_Details["Net Tax"] = round(netTax, 2)
        Employee_Details["PRSI"] = PRSI
        Employee_Details["Net Deductions"] = round(netdeduction, 2)
        Employee_Details["Net Pay"] = round(netPay, 2)

        print(Employee_Details)

        return Employee_Details

# jg = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
# pi = jg.computePayment(42, '31/10/2021')


    class test_payment(unittest.TestCase):


        def Test_Net_Less_equal_Gross(self):
            net_pay = Employee(12345, 'Manjunath', 'shetti', 37, 16, 1.5, 72, 710)
            pi = net_pay.computePayment(42, '31/10/2021')
            self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])

        # overtime  pay can not be negative
        def overtime_pay_cannotbenegative(self):
            overPay = Employee(12345, 'Green ', 'shetti', 37, 16, 1.5, 72, 710)
            pi = overPay.computePayment(42, '31/10/2021')
            self.assertGreater(pi['Overtime Pay'], -1)



        # reg_hours = Employee(10606018, 'Manjunath', 'shetti', 37, 16, 1.5, 72, 710)
        # pi = reg_hours.computePayment(42, '31/10/2021')
        # self.assertLessEqual(pi['Regular Hours Worked'], pi["Regular Hours Worked"] + pi["Overtime Hours Worked"])

    #  higher tax cannot be negative
    def Higher_Tax_cannot_be_negative(self):
        high_tax = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = high_tax.computePayment(1, '31/10/2021')
        self.assertGreater(pi['Higher Tax'], -1)


#  test regular hours  cannot exeed than hours worked
    def test_regular_hours_cannot_exceed_hours_worked(self):
        reg_hours = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = reg_hours.computePayment(1, '31/10/2021')
        self.assertLessEqual(pi['Regular Hours Worked'], pi["Regular Hours Worked"] + pi["Overtime Hours Worked"])




