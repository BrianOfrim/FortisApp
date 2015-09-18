from django.db import models

# Create your models here.
class EnterPanel(models.Model):
	panelLocations = ['Assembly Table','Framing Table','Sheathing Table'
	,'ABV Table','South Wall','R1','R2','R3','R4','R5','R6','R7','R8','RS1'
	,'RS2','RS3','T002','T006','T007','T007','T008','T016','T021','Overflow 1'
	,'Overflow 2','Overflow 3','Overflow 4','Overflow 5','Overflow 6','Overflow 7'
	,'Overflow 8','Overflow 9','Overflow 10','Site']

	panelName = models.CharField(null = False,max_length = 120)
	shipment = models.CharField(max_length = 2,choices = [(str(x),str(x)) for x in range(1,32)])
	panelLocation = models.CharField(max_length = 15, choices = [(i,i) for i in panelLocations])
	panelSublocation = models.CharField(max_length = 2, choices = [(str(i),str(i)) for i in range (1,13)], blank = True,default = "  ") 
	generalNotes  = models.CharField(null = True, max_length = 200)
	crewInfo = models.CharField(null = True, max_length = 200)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	def __str__(self):
		return self.panelName


class PageOptions(models.Model):
	pageNames = ['office', 'worker' ]
	pageChoice = models.CharField(max_length = 20, choices = [(str(i),str(i)) for i in pageNames])




