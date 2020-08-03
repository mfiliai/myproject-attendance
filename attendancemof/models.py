from django.db import models

# Create your models here.

class Stafflist(models.Model):
	BAND = (
		('B', 'B'),
		('C', 'C'),
		('D', 'D'),
		('E', 'E'),
		('F', 'F'),
		('G', 'G'),
		('H', 'H'),
		('I', 'I'),
		('J', 'J'),
		('K', 'K'),
		('L', 'L'),
		('M', 'M'),
		('N', 'N'),
		('O', 'O'),
		('P', 'P'),
		('Q', 'Q'),
		('R', 'R'),
		('S', 'S'),

	)
	DIVISION = (
			('Corporate Services Division','Corporate Services Division'),
			('Office of the CEO', 'Office of the CEO'),
			('Office of the Minister', 'Office of the Minister'),
			('Information Technology and Communication Division', 'Information Technology and Communication Division'),
			('Finacial Framework Division', 'Finacial Framework Division'),
			('Procurement Division', 'Procurement Division'),
			('Treasury Division', 'Treasury Division'),
			('Budget Division', 'Budget Division'),
			('Aid and Projects Division', 'Aid and Projects Division'),
			('Economic and Fiscal Policy Division', 'Economic and Fiscal Policy Division'),
			('Resilience Division', 'Resilience Division'),
			('SUB EUA', 'SUB EUA'),
			('SUB VAVAU', 'SUB VAVAU'),
			('SUB HAAPAI', 'SUB HAAPAI'),
	)
	Code = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=200, null=True)
	Division = models.CharField(max_length=200, null=True, choices=DIVISION)
	Position = models.CharField(max_length=200, null=True)
	Band = models.CharField(max_length=20, null=True, choices=BAND)
	Date_Created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return (self.Name)

class AttendanceT20(Stafflist):


	ATTENDANCE = (
			('On Duty','On Duty'),
			('Late','Late'),
			('Casual Leave','Casual Leave'),
			('Annual Leave','Annual Leave'),
			('Sick Leave','Sick Leave'),
			('In Lieu','In Lieu'),
			('NOP','NOP'),
			('WOP','WOP'),
	)


	a_id = models.AutoField(default= '2',primary_key=True)
	AttendanceDate = models.DateField(null=True)
	Attendance = models.CharField(max_length=200, choices=ATTENDANCE, null=True)
	Time_In = models.TimeField(null=True)
	Remarks = models.CharField(null=True, max_length=500)



	def __str__(self):
		return (self.Attendance)


class TreasuryPurposes(AttendanceT20):
	t_id = models.AutoField( default= '1', primary_key=True)
	Time_Out = models.TimeField(null=True)
	Late_hours = models.TimeField(null=True)
	Overtime_In = models.TimeField(null=True)
	Overtime_Out = models.TimeField(null=True)
	Deduction_Hours = models.TimeField(null=True)

	def __str__(self):
		return (self.Time_Out)
