from django.db import models
from .utils import FIXED_WAGES
# --------------------------
# 1️⃣ Projects Module
# --------------------------
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)

    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Sold', 'Sold'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)

    image = models.ImageField(upload_to='project_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.project_name} (P{self.project_id})"


# --------------------------
# 2️⃣ Materials Module
# --------------------------
class Material(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="materials")

    MATERIAL_CHOICES = [
        ('Cement', 'Cement'),
        ('Bricks', 'Bricks (playas)'),
        ('Sand_E', 'M-sand'),
        ('Sand_B', 'P-sand'),
        ('Jelly_Q', 'Jelly (¼ size)'),
        ('Jelly_H', 'Jelly (3/4 size)'),
        ('Jelly_P', 'Jelly (1.5 size)'),
        ('Jelly_S', 'Jelly (Bolder)'),
        ('Tiles_Q', 'Tiles (TMT(8mm))'),
        ('Tiles_H', 'Tiles (TMT(10mm))'),
        ('Tiles_P', 'Tiles (TMT(12mm))'),
        ('Tiles_S', 'Tiles (TMT(16mm))'),
        ('Tiles_R', 'Tiles (TMT(20mm))'),
        ('Paints', 'Paints'),
        ('Wood_M_Teak', 'Wood(main_door(teak))'),
        ('Wood_M_Saal', 'Wood(main_door(saal))'),
        ('Wood_M_Mahagani', 'Wood(main_door(mahagani))'),
        ('Wood_W_Mahagani', 'Wood(windows(mahagani))'),
        ('Wood_W_Upvc', 'Wood(windows(upvc))'),
        ('Electronics_Wire', 'Electronics(wire(2.5sq,1.5sq,1sq))'),
        ('Electronics_Plug', 'Electronics(plug)'),
        ('Electronics_LED', 'Electronics(LEDLight(ceiling_4inch,elevation_3inch))'),
        ('Electronics_Tube', 'Electronics(Tubelight)'),
        ('Plumbing_Upvc', 'Plumbing(upvc(1inch,3/4inch))'),
        ('Plumbing_Pvc', 'Plumbing(pvc(4inch,2.5inch,1.5inch))'),
        ('Plumbing_Fittings', 'Plumbing(Fittings(Bathroom,Kitchen))'),
        ('Grill', 'Grill(grill,gate)'),
    ]
    material_name = models.CharField(max_length=50, choices=MATERIAL_CHOICES)
    quantity_purchased = models.IntegerField(default=0)
    quantity_used = models.IntegerField(default=0)
    quantity_sold = models.IntegerField(default=0)
    supplier_name = models.CharField(max_length=100, null=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    @property
    def remaining_stock(self):
        return self.quantity_purchased - (self.quantity_used + self.quantity_sold)

    def __str__(self):
        return f"{self.material_name} - {self.project.project_name}"


# --------------------------
# 3️⃣ Worker Roles (Choices)
# --------------------------
# models.py

class WorkerRole(models.TextChoices):
    MESTHRI = "Mesthri", "Mesthri"
    MESON = "Meson", "Meson"
    MAMTIYAL = "Mamtiyal", "Mamtiyal"
    SITTAAL = "Sittaal", "Sittaal"
    PAINTER = "Painter", "Painter"
    ELECTRICIAN = "Electrician", "Electrician"
    PLUMBER = "Plumber", "Plumber"

# --------------------------
# 4️⃣ Workers Module
# --------------------------
class Worker(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="workers")
    worker_name = models.CharField(max_length=100)
    worker_type = models.CharField(max_length=50, choices=WorkerRole.choices)
    contact = models.CharField(max_length=15, blank=True, null=True)
    weekly_wage = models.IntegerField(default=0) 

    PAYMENT_STATUS = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='Unpaid')

    def __str__(self):
        return f"{self.worker_name} ({self.worker_type}) - {self.project.project_name}"


# --------------------------
# 5️⃣ Worker Attendance
# --------------------------
FIXED_WAGES = {
    "Mesthri": 1100,
    "Meson": 1000,
    "Mamtiyal": 800,
    "Sittaal": 350,
    "Painter": 1100,
    "Electrician": 1200,
    "Plumber": 1200,
}

class WorkerAttendance(models.Model):
    worker = models.ForeignKey("Worker", on_delete=models.CASCADE)
    date = models.DateField()
    members_count = models.IntegerField(default=1)
    remarks = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[("Present", "Present"), ("Absent", "Absent")],
        default="Present"
    )
    daily_wage = models.IntegerField(editable=False, default=0)  # 👈 integer

    def save(self, *args, **kwargs):
        wage_per_worker = FIXED_WAGES.get(self.worker.worker_type, 0)
        self.daily_wage = self.members_count * wage_per_worker
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.worker.worker_type} - {self.date} - ₹{self.daily_wage}"
