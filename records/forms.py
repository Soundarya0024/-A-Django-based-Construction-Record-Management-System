from django import forms
from .models import Project, Worker, Material, WorkerAttendance

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['project', 'worker_name', 'worker_type', 'contact', 'weekly_wage', 'payment_status']
        
class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = WorkerAttendance
        fields = ['worker', 'date', 'members_count', 'status', 'remarks']

    # daily_wage is not editable; calculated automatically
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally, you can set placeholders or bootstrap classes
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
