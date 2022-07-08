
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

    def computepayment(self, worked_hours, Date):


        # if standard tax rate is 20% then 20/100=0.2  [Hence, standard_pay = 0.2]
        # if higher tax rate is 40% then 40/100=0.4 [Hence, higerTaxRate = 0.4]
        # if higher tax rate is 4% then 4/100=0.04 [Hence, PRSIrate = 0.04]


        overtime_hours, regularpay, overtime_pay, Overtime_Rate, grossPay, standard_pay, standardTax, netPay = 0, 0, 0, 0, 0, 0, 0, 0
        standardTaxRate, higherRatePay, higherTax, higherTaxRate, totalTax, netTax, PRSIrate, netdeduction = 0.2, 0, 0, 0.4, 0, 0, 0.04, 0
        Employee_Details = {}


        if worked_hours >self.Reg_hours:
            overtime_hours = worked_hours - self.Reg_hours
        else:
            self.Reg_hours = worked_hours


        overtime_Rate = self.OT_multiple * self.hourly_rate

        regularpay = self.Reg_hours * self.hourly_rate

        overtime_pay = overtime_hours * overtime_Rate

        grossPay = regularpay + overtime_pay


        if grossPay > self.Standard_band:
            standardTax = standardTaxRate * self.Standard_band

            higherRatePay = grossPay- self.Standard_band

        else:
            standardTax= grossPay * standardTaxRate



            #higher tax
            higherTax = higherTaxRate * standardTax

            totalTax = higherTax + higherRatePay

    #if totaltax > taxcredit nettax would be totaltx+ tax credit
        if (totalTax > self.Tax_credit):
            netTax = totalTax - self.Tax_credit
        else:
            netTax = totalTax


           #PRSI
        PRSI = PRSIrate * grossPay


        #net deductiom

        netdeduction = netTax + PRSI

        netPay= grossPay - netdeduction


