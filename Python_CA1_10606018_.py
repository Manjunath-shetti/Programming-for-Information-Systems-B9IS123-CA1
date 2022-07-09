import unittest
class Employee:
    def __init__(self, staff_Id, last_name, first_name,Reg_hours, hourly_rate, OT_multiple, Tax_credit, Standard_band):
        self.staff_Id = staff_Id
        self.last_name = last_name
        self.first_name = first_name
        self.Reg_hours = Reg_hours
        self.hourly_rate = hourly_rate
        self.OT_multiple = OT_multiple
        self.Tax_credit = Tax_credit
        self.Standard_band = Standard_band

    def computePayment(self, worked_hours, Date):


        # if standard tax rate is 20% then 20/100=0.2  [Hence, standard_pay = 0.2]
        # if higher tax rate is 40% then 40/100=0.4 [Hence, higerTaxRate = 0.4]
        # if higher tax rate is 4% then 4/100=0.04 [Hence, PRSIrate = 0.04]


        overtime_hours, regularpay, overtime_pay, Overtime_Rate, grossPay, standard_pay, standardTax, netPay = 0, 0, 0, 0, 0, 0, 0, 0
        standardTaxRate, higherRatePay, higherTax, higherTaxRate, totalTax, netTax, PRSIrate, netdeduction = 0.2, 0, 0, 0.4, 0, 0, 0.04, 0
        Employee_Details = {}


        if worked_hours > self.Reg_hours:
            overtime_hours = worked_hours - self.Reg_hours
        else:

            self.Reg_hours = worked_hours


        Overtime_Rate = self.OT_multiple * self.hourly_rate


        regularpay = self.Reg_hours * self.hourly_rate


        Overtime_pay = overtime_hours * Overtime_Rate


        grossPay = regularpay + Overtime_pay


        if grossPay > self.Standard_band:
            standardTax = standardTaxRate * self.Standard_band


            higherRatePay = grossPay - self.Standard_band
        else:
            standardTax = grossPay * standardTaxRate


        higerTax = higherTaxRate * higherRatePay


        totalTax = higerTax + standardTax


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

jg = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
pi = jg.computePayment(42, '31/10/2021')




