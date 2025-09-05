from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  

    # Projects
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),

    # ---------------- Workers ----------------
   path('workers/', views.WorkerListView.as_view(), name='worker_list'),
   path('workers/create/', views.WorkerCreateView.as_view(), name='worker_create'),
   path('workers/<int:pk>/update/', views.WorkerUpdateView.as_view(), name='worker_update'),
   path('workers/<int:pk>/delete/', views.WorkerDeleteView.as_view(), name='worker_delete'),


    # Materials
    path('materials/', views.MaterialListView.as_view(), name='material_list'),
    path('materials/create/', views.MaterialCreateView.as_view(), name='material_create'),
    path('materials/<int:pk>/update/', views.MaterialUpdateView.as_view(), name='material_update'),
    path('materials/<int:pk>/delete/', views.MaterialDeleteView.as_view(), name='material_delete'),

    # Attendance
    path('attendance/', views.AttendanceListView.as_view(), name='attendance_list'),
    path('attendance/create/', views.AttendanceCreateView.as_view(), name='attendance_create'),
    path('attendance/<int:pk>/update/', views.AttendanceUpdateView.as_view(), name='attendance_update'),
    path('attendance/<int:pk>/delete/', views.AttendanceDeleteView.as_view(), name='attendance_delete'),
]
