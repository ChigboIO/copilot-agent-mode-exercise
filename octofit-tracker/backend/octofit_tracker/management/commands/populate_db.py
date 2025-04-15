from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data using model classes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Add test users
        user1 = User.objects.create(email='john@example.com', name='John Doe', password='password123')
        user2 = User.objects.create(email='jane@example.com', name='Jane Doe', password='password456')

        # Add test teams
        team1 = Team.objects.create(name='Team Alpha', members=[user1.id])
        team2 = Team.objects.create(name='Team Beta', members=[user2.id])

        # Add test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-04-15')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=60, date='2025-04-15')

        # Add test leaderboard entries
        Leaderboard.objects.create(team=team1, points=100)
        Leaderboard.objects.create(team=team2, points=150)

        # Add test workouts
        Workout.objects.create(name='Morning Run', description='A quick morning run', duration=30)
        Workout.objects.create(name='Evening Yoga', description='Relaxing yoga session', duration=45)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
