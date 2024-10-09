from django.db import models


# Create your models here.
class Task(models.Model):

    class StatusChoices(models.TextChoices):
        PENDING = "P", "Pending"
        IN_PROGRESS = "I", "In Progress"
        COMPLETED = "C", "Completed"

    class TagChoices(models.TextChoices):
        WORK = "W", "Work"
        PERSONAL = "P", "Personal"

    owner = models.ForeignKey(
        "auth.User", related_name="tasks", on_delete=models.CASCADE
    )
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=1, choices=TagChoices.choices)
    status = models.CharField(
        max_length=1,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )

    def __str__(self):
        return f"{self.description} - {self.get_status_display()}"
