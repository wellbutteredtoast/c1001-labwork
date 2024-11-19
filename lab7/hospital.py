class HospitalEmp():
    ## Construct a hospital employee object with information for last name,
    #  first name, and year hired as instance vars: __lName, __fName, __hireYear
    #  @param lName the last name of the employee
    #  @param fName the first name of the employee
    #  @param hYear the year that the employee was hired
    def __init__(self, lName, fName, hireYear):
        self.__lName = lName
        self.__fName = fName
        self.__hireYear = hireYear

        
    ## Accessor method to return the name of the employee as lastname, firstname
    #  @return the last, first name of the employee
    def getEmployeeName(self):
        return str(self.__lName + " " + self.__fName)
  
    ## Accessor method to return the employee's hire year
    #  @return the hire year of the employee    
    def getYearHired(self):
        return self.__hireYear

    ## Method to get a string representation of the hospital employee
    #  @return a string containing the details of the hospital employee
    def __repr__(self) :
        return "\n" + type(self).__name__ + " Name: " + self.getEmployeeName() +  "\nHired: " + str(self.__hireYear) 
 

class Doctor(HospitalEmp):
    PAY_PER_APPT = 20  # class variable for pay per appointment

    ## Construct a doctor object with last name, first name and year hired, as 
    #  well as additional instance vars for base yearly salary and number of 
    #  appointments in a year as: __baseSal, __numAppt
    #  @param lName is the last name of the doctor
    #  @param fName is the first name of the doctor
    #  @param hYear the year that the doctor was hired
    #  @param baseSal is the base yearly salary of the doctor
    #  @param numAppt is the number of appointments for the doctor in a year
    def __init__(self, lName, fName, hireYear, baseSal, numAppt):
        super().__init__(lName, fName, hireYear)
        self.__baseSal = baseSal
        self.__numAppt = numAppt
       
    ## Method to get a string representation of the doctor
    #  @return a string containing the details of the doctor
    def __repr__(self) :
        return super().__repr__() + "\nYearly Salary: $" + str(self.getYrlySalary())


    ## Accessor method to compute the yearly salary for the doctor
    #   @return the doctor's yearly salary
    def getYrlySalary(self):
        return self.__baseSal + self.__numAppt * Doctor.PAY_PER_APPT


class Nurse(HospitalEmp):
    ## Construct a nurse object with last name, first name and year hired, as 
    #  well as additonal instance variables for hours worked and hourly 
    #  pay as: __hrsWorked, __hrlyPay
    #  @param lName is the last name of the nurse
    #  @param fName is the first name of the nurse
    #  @param hYear the year that the nurse was hired
    #  @param hWorked is the hours worked by the nurse in a year
    #  @param hrlyPay is the hourly pay of the nurse
    def __init__(self, lName, fName, yearHired, hrsWorked, hrPay):
        super().__init__(lName, fName, yearHired)
        self.__hrsWorked = hrsWorked
        self.__hrlyPay = hrPay

    ## Method to get a string representation of the nurse
    #  @return a string containing the details of the nurse including
    #  the name, hire year, and yearly salary
    def __repr__(self):
        return super().__repr__() + f"\nHours Worked: {self.__hrsWorked}hr\nYearly Salary: {self.getYearlySalary()}$"


    ## Mutator method (addHours) to add hours to the hours worked by the nurse
    #  @param extraHours is the additional hours worked by the nurse
    def addHours(self, extraHours: int) -> None:
        self.__hrsWorked += extraHours


    ## Accessor method to compute the yearly salary for the nurse
    #  @return the yearly salary for the nurse as the number of hours
    #  worked times the hourly pay
    def getYearlySalary(self):
        return round((self.__hrsWorked * self.__hrlyPay), 4)



class Surgeon(Doctor) :
    PAY_PER_SURGERY = 100  # class variable for pay per surgery

    ## Construct a surgeon object with last name, first name, year hired, 
    #  base yearly salary, number of appointments in a year, as well as 
    #  additional instance vars for number of surgeries in a year 
    #  as: __numSurgery
    #  @param lName is the last name of the surgeon
    #  @param fName is the first name of the surgeon
    #  @param hYear the year that the surgeon was hired
    #  @param baseSal is the base yearly salary of the surgeon
    #  @param numAppt is the number of appointments for the surgeon in a year
    #  @param numSurg is the number of surgeries for the surgeon in a year
    def __init__(self, lName, fName, hireYear, baseSal, numAppt, numSurg):
        super().__init__( lName, fName, hireYear, baseSal, numAppt)
        self.__numSurg = numSurg

    ## Accessor method to compute the yearly salary for the surgeon
    #   @return the surgeon's yearly salary
    def getYrlySalary(self):
        return (self._Doctor__baseSal + self._Doctor__numAppt * Doctor.PAY_PER_APPT) + (self.PAY_PER_SURGERY * self.__numSurg)



def main():
    e1 = HospitalEmp("Smith","Joe",1998)
    d1 = Doctor("Jones","Mia",2015,100000,5000)
    n1 = Nurse("Sing","Reese",2010,1820,25.5)
    s1 = Surgeon("Knife","Mack",2009,120000,1000,350)
    print(e1)
    print(d1)
    print(n1)
    print(s1)
    n1.addHours(50)
    print("\n**After 50 hours added for nurse:")
    print(n1)

main()
