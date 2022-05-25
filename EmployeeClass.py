class Employee:
 def __init__(self, eid, ename, eloc, esal ):
  self.eid = eid
  self.ename = ename
  self.eloc = eloc
  self.esal = esal

 def GetEmployee(self):
  print("Employee with the id as " + str(self.eid) + " and name as " + self.ename + " is working from " + self.eloc + " and has a salary of INR." + str(self.esal))
