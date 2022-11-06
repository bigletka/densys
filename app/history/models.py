
from django.db import models
from core.models import User


class History(models.Model):
    """The history of the patient."""
    appointments = []
    treatments = []
    prescribed_drugs = []
    treatment_status = models.CharField(default='healthy', max_length=25)
    patient = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    
    


    def add_appointment_to_history(self, appointment):
        """Add appointment to history"""
        self.appointments.append(appointment)
        return self

    def add_treatment_to_history(self, treatment):
        """Add treatment to history"""
        self.treatments.append(treatment)
        return self

    def add_drugs(self, drugs):
        """Prescribed drugs adding"""
        self.prescribed_drugs.append(drugs)
        return self
    
    def change_status(self, status):
        """Changing the treatment status of the patient"""
        self.treatment_status = status
        return self
