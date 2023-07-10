from django.db import models


class PersonToContact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=16, default="DNE")
    email = models.EmailField()
    topic = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Employee(models.Model):
    first_name_kz = models.CharField(max_length=100)
    first_name_ru = models.CharField(max_length=100)
    first_name_en = models.CharField(max_length=100)
    last_name_kz = models.CharField(max_length=100)
    last_name_ru = models.CharField(max_length=100)
    last_name_en = models.CharField(max_length=100)
    patronymic_kz = models.CharField(max_length=100)
    patronymic_ru = models.CharField(max_length=100)
    patronymic_en = models.CharField(max_length=100)
    birthday = models.DateField()
    label = models.CharField(max_length=100)


class Position(models.Model):
    position_type = models.CharField(max_length=100)
    name_kz = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)


class FileStorage(models.Model):
    parent = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    origin_name = models.CharField(max_length=200)
    file_type = models.CharField(max_length=100)


class EmployeePosition(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    dbeg = models.DateField()
    dend = models.DateField()


class Customer(models.Model):
    name_kz = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    fullname_kz = models.CharField(max_length=300)
    fullname_ru = models.CharField(max_length=300)
    fullname_en = models.CharField(max_length=300)
    address = models.CharField(max_length=500)


class Service(models.Model):
    parent = models.CharField(max_length=200)
    service_type = models.CharField(max_length=200)
    name_kz = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    cmt_kz = models.CharField(max_length=200)
    cmt_ru = models.CharField(max_length=200)
    cmt_en = models.CharField(max_length=200)


class Solution(models.Model):
    parent = models.CharField(max_length=200)
    solution_type = models.CharField(max_length=200)
    name_kz = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    cmt_kz = models.CharField(max_length=200)
    cmt_ru = models.CharField(max_length=200)
    cmt_en = models.CharField(max_length=200)


class Research(models.Model):
    parent = models.CharField(max_length=200)
    research_type = models.CharField(max_length=200)
    name_kz = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    cmt_kz = models.CharField(max_length=200)
    cmt_ru = models.CharField(max_length=200)
    cmt_en = models.CharField(max_length=200)


class Publication(models.Model):
    publication_type = models.CharField(max_length=200)
    name_kz = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    lang = models.CharField(max_length=100)
    d_year = models.DateField()
    cmt_kz = models.CharField(max_length=200)
    cmt_ru = models.CharField(max_length=200)
    cmt_en = models.CharField(max_length=200)


class Project(models.Model):
    parent = models.CharField(max_length=200)
    name_kz = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    begin_year = models.DateField()
    end_year = models.DateField()
    head_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    cmt_kz = models.CharField(max_length=200)
    cmt_ru = models.CharField(max_length=200)
    cmt_en = models.CharField(max_length=200)


class ServiceArtifact(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    artifact_type = models.CharField(max_length=200)
    file_storage = models.ForeignKey(FileStorage, on_delete=models.CASCADE)


class SolutionArtifact(models.Model):
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    artifact_type = models.CharField(max_length=200)
    file_storage = models.ForeignKey(FileStorage, on_delete=models.CASCADE)


class ResearchPublication(models.Model):
    research = models.ForeignKey(Research, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)


class PublicationAuthor(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class PublicationFile(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    file_storage = models.ForeignKey(FileStorage, on_delete=models.CASCADE)


class ProjectArtifact(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    artifact_type = models.CharField(max_length=200)
    file_storage = models.ForeignKey(FileStorage, on_delete=models.CASCADE)


class ProjectSolution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
