from django.contrib import admin
from .models import PersonToContact

from .models import (
    PersonToContact, Employee, Position, FileStorage, EmployeePosition,
    Customer, Service, Solution, Research, Publication, Project, 
    ServiceArtifact, SolutionArtifact, ResearchPublication, 
    PublicationAuthor, PublicationFile, ProjectArtifact, ProjectSolution
)


# admin.site.register(PersonToContact)



@admin.register(PersonToContact)
class PersonToContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PersonToContact._meta.fields]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Position._meta.fields]


@admin.register(FileStorage)
class FileStorageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FileStorage._meta.fields]


@admin.register(EmployeePosition)
class EmployeePositionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EmployeePosition._meta.fields]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Solution._meta.fields]


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Research._meta.fields]


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Publication._meta.fields]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.fields]


@admin.register(ServiceArtifact)
class ServiceArtifactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ServiceArtifact._meta.fields]


@admin.register(SolutionArtifact)
class SolutionArtifactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SolutionArtifact._meta.fields]


@admin.register(ResearchPublication)
class ResearchPublicationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ResearchPublication._meta.fields]


@admin.register(PublicationAuthor)
class PublicationAuthorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PublicationAuthor._meta.fields]


@admin.register(PublicationFile)
class PublicationFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PublicationFile._meta.fields]


@admin.register(ProjectArtifact)
class ProjectArtifactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProjectArtifact._meta.fields]


@admin.register(ProjectSolution)
class ProjectSolutionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProjectSolution._meta.fields]
