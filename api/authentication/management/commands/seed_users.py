from decouple import config
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from api.authentication.models import Role


class SeedUsersManager:
    GROUPS_PERMISSIONS_MAPPINGS = {
        "BOOK_READ": ["view_book", "view_page"],
        "BOOK_CHANGE": ["add_book", "change_book", "delete_book", "add_page", "change_page", "delete_page"],
    }

    ROLES_GROUPS_MAPPINGS = {
        Role.NAME_READER: ["BOOK_READ"],
        Role.NAME_EDITOR: ["BOOK_READ", "BOOK_CHANGE"],
    }

    def __init__(self, command):
        self.command = command
        self.user_model = get_user_model()

    def execute(self):
        self._create_superuser(
            username=config("DJANGO_SUPERUSER_USERNAME", default="admin"),
            email=config("DJANGO_SUPERUSER_EMAIL", default="admin@admin.com"),
            password=config("DJANGO_SUPERUSER_PASSWORD", default="admin"),
        )
        self._create_groups_with_permissions()
        self._create_roles_and_assign_groups()
        self._create_users_and_assign_roles()
        self.command.stdout.write(self.command.style.SUCCESS("All roles, groups, permissions, and users configured."))

    def _create_superuser(self, username, email, password):
        if not self.user_model.objects.filter(username=username).exists():
            self.user_model.objects.create_superuser(username, email, password)
            self.command.stdout.write(self.command.style.SUCCESS(f"Superuser {username} created."))

    def _create_groups_with_permissions(self):
        for group_name, permission_codenames in self.GROUPS_PERMISSIONS_MAPPINGS.items():
            group, _ = Group.objects.get_or_create(name=group_name)
            permissions = Permission.objects.filter(codename__in=permission_codenames)
            group.permissions.set(permissions)

    def _create_roles_and_assign_groups(self):
        for role_name, group_names in self.ROLES_GROUPS_MAPPINGS.items():
            role, _ = Role.objects.get_or_create(name=role_name)
            groups = [Group.objects.get(name=name) for name in group_names]
            role.groups.set(groups)
            self.command.stdout.write(
                self.command.style.SUCCESS(f"Role '{role_name}' assigned groups: {', '.join(group_names)}")
            )

    def _create_users_and_assign_roles(self):
        for role_name, _ in Role.NAME_CHOICES:
            user, created = self.user_model.objects.get_or_create(
                username=role_name,
                defaults={"email": f"{role_name}@{role_name}.com"}
            )
            user.role = Role.objects.get(name=role_name)
            user.save(update_fields=["role"])
            if created:
                user.set_password(role_name)
                self.command.stdout.write(
                    self.command.style.SUCCESS(f"User '{role_name}' created and assigned role '{role_name}'.")
                )


class Command(BaseCommand):
    help = 'Populate the database with default users, roles, and permissions.'

    def handle(self, *args, **kwargs):
        SeedUsersManager(self).execute()
