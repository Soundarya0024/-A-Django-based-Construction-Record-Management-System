from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Project, Worker, Material, WorkerAttendance, FIXED_WAGES
from .forms import AttendanceForm

# ---------------- Home ----------------
def home(request):
    return render(request, "records/home.html")

# ---------------- Projects ----------------
class ProjectListView(ListView):
    model = Project
    template_name = "records/project_list.html"
    context_object_name = "projects"

class ProjectCreateView(CreateView):
    model = Project
    fields = ["project_name", "location", "start_date", "end_date", "budget", "status", "image"]
    template_name = "records/project_form.html"
    success_url = reverse_lazy("project_list")

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ["project_name", "location", "start_date", "end_date", "budget", "status", "image"]
    template_name = "records/project_form.html"
    success_url = reverse_lazy("project_list")

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "records/confirm_delete.html"
    success_url = reverse_lazy("project_list")

# ---------------- Materials ----------------
class MaterialListView(ListView):
    model = Material
    template_name = "records/material_list.html"
    context_object_name = "materials"

class MaterialCreateView(CreateView):
    model = Material
    fields = ["project", "material_name", "quantity_purchased", "quantity_used", "quantity_sold", "supplier_name", "purchase_date", "cost"]
    template_name = "records/material_form.html"
    success_url = reverse_lazy("material_list")

class MaterialUpdateView(UpdateView):
    model = Material
    fields = ["project", "material_name", "quantity_purchased", "quantity_used", "quantity_sold", "supplier_name", "purchase_date", "cost"]
    template_name = "records/material_form.html"
    success_url = reverse_lazy("material_list")

class MaterialDeleteView(DeleteView):
    model = Material
    template_name = "records/confirm_delete.html"
    success_url = reverse_lazy("material_list")

# ---------------- Workers ----------------
class WorkerListView(ListView):
    model = Worker
    template_name = "records/worker_list.html"
    context_object_name = "workers"

class WorkerCreateView(CreateView):
    model = Worker
    fields = ["worker_name", "worker_type", "contact", "project"]
    template_name = "records/worker_form.html"
    success_url = reverse_lazy("worker_list")

class WorkerUpdateView(UpdateView):
    model = Worker
    fields = ["worker_name", "worker_type", "contact", "project"]
    template_name = "records/worker_form.html"
    success_url = reverse_lazy("worker_list")

class WorkerDeleteView(DeleteView):
    model = Worker
    template_name = "records/confirm_delete.html"
    success_url = reverse_lazy("worker_list")

# ---------------- Attendance ----------------
class AttendanceListView(ListView):
    model = WorkerAttendance
    template_name = "records/attendance_list.html"
    context_object_name = "attendances"

class AttendanceCreateView(CreateView):
    model = WorkerAttendance
    form_class = AttendanceForm
    template_name = "records/attendance_form.html"
    success_url = reverse_lazy("attendance_list")

    def form_valid(self, form):
        worker = form.cleaned_data['worker']
        members_count = form.cleaned_data['members_count']
        wage_per_worker = FIXED_WAGES.get(worker.worker_type, 0)
        form.instance.daily_wage = wage_per_worker * members_count
        return super().form_valid(form)

class AttendanceUpdateView(UpdateView):
    model = WorkerAttendance
    form_class = AttendanceForm
    template_name = "records/attendance_form.html"
    success_url = reverse_lazy("attendance_list")

    def form_valid(self, form):
        worker = form.cleaned_data['worker']
        members_count = form.cleaned_data['members_count']
        wage_per_worker = FIXED_WAGES.get(worker.worker_type, 0)
        form.instance.daily_wage = wage_per_worker * members_count
        return super().form_valid(form)

class AttendanceDeleteView(DeleteView):
    model = WorkerAttendance
    template_name = "records/attendance_confirm_delete.html"
    success_url = reverse_lazy("attendance_list")
