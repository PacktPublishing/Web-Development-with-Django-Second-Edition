from pprint import pformat

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "List all user sessions and the data that they contain."

    def handle(self, *args, **options):
        session_store = SessionStore()
        for session in Session.objects.all():
            data = session_store.decode(session.session_data)
            user = User.objects.get(id=data["_auth_user_id"])
            self.stdout.write(
                f"Session Key: {session.session_key} "
                f"User: {user.id} {user.username} {user.email} "
            )
            self.stdout.write(pformat(data))
