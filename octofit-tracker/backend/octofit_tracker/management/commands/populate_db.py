from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create users
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
        ]
        User.objects.bulk_create([User(**user) for user in users])

        # Create team
        team = Team.objects.create(name="Blue Team")
        team.save()
        for user in User.objects.all():
            team.members.add(user)

        # Create activities
        activities = [
            {"user": User.objects.first(), "activity_type": "Cycling", "duration": timedelta(hours=1)},
            {"user": User.objects.all()[1], "activity_type": "Crossfit", "duration": timedelta(hours=2)},
        ]
        Activity.objects.bulk_create([Activity(**activity) for activity in activities])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
