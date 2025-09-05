# ✅ records/admin.py
from django.contrib import admin
from .models import Project, Material, Worker, WorkerAttendance

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'location', 'start_date', 'end_date', 'status')
    search_fields = ('project_name', 'location')
    list_filter = ('status',)

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_name', 'project', 'quantity_purchased', 'quantity_used', 'remaining_stock', 'cost')
    search_fields = ('material_name', 'supplier_name')
    list_filter = ('material_name',)

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('worker_name', 'worker_type', 'contact', 'project', 'weekly_wage', 'payment_status')
    search_fields = ('worker_name',)
    list_filter = ('worker_type', 'payment_status')

class WorkerAttendanceAdmin(admin.ModelAdmin):
    list_display = ('worker', 'date', 'members_count', 'daily_wage', 'status', 'remarks')  # ✅ show daily_wage + status
    list_filter = ('date', 'worker__worker_type', 'status')
    search_fields = ('worker__name',)
    readonly_fields = ('daily_wage',)  # ✅ makes daily_wage visible but not editable in admin form

# ✅ Register models with admin
admin.site.register(Project, ProjectAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(WorkerAttendance, WorkerAttendanceAdmin)
