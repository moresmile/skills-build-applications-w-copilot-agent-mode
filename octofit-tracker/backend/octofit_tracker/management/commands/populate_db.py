from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create users
        users = [
            User(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
        ]
        User.objects.bulk_create(users)

        # Convert users to dictionaries for ArrayField and EmbeddedField compatibility
        user_dicts = [
            {"_id": str(user._id), "username": user.username, "email": user.email, "password": user.password}
            for user in User.objects.all()
        ]

        # Create team
        team = Team(_id=ObjectId(), name='Blue Team', members=user_dicts)
        team.save()

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=user_dicts[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), user=user_dicts[1], activity_type='Crossfit', duration=timedelta(hours=2)),
        ]
        for activity in activities:
            print(f"Saving activity: {activity}")
            activity.save()
            print(f"Activity saved: {activity}")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
