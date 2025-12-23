from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class StudentSkill(models.Model):
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, related_name="StudentSkill"
    )
    student = models.ForeignKey(
        "profiles.StudentProfile", on_delete=models.CASCADE, related_name="StudentSkill"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("expert", "Expert"),
    ]
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="beginner")

    class Meta:
        unique_together = ("student", "skill")

    def __str__(self):
        return f"{self.student} : {self.skill} ({self.get_level_display()})"


class Institution(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    wilaya = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=250, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Domain(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, related_name="domains"
    )

    def __str__(self):
        return self.name


class Specialty(models.Model):
    domain = models.ForeignKey(
        Domain, on_delete=models.CASCADE, related_name="specialties"
    )
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, related_name="specialities"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.domain.name})"
