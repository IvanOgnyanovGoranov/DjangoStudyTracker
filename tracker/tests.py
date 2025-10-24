import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Subject, DAILY_GOAL_MSG

class SubjectModelTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_daily_goal_negative_raises_validation_error(self):
        subject = Subject(user=self.user, name="Math", daily_goal=-5)
        with self.assertRaises(ValidationError) as context:
            subject.full_clean()  # triggers validators
        self.assertIn(DAILY_GOAL_MSG, str(context.exception))

    def test_daily_goal_exceeds_max_raises_validation_error(self):
        subject = Subject(user=self.user, name="Science", daily_goal=2000)
        with self.assertRaises(ValidationError) as context:
            subject.full_clean()
        self.assertIn(DAILY_GOAL_MSG, str(context.exception))

    def test_daily_goal_valid_saves_correctly(self):
        subject = Subject(user=self.user, name="History", daily_goal=60)
        try:
            subject.full_clean()  # should not raise
            subject.save()
        except ValidationError:
            self.fail("full_clean() raised ValidationError unexpectedly!")

        # Confirm object exists in DB
        self.assertEqual(Subject.objects.count(), 1)
        self.assertEqual(Subject.objects.first().daily_goal, 60)


class EditSubjectTests(TestCase):

    def setUp(self):
        pass



if __name__ == '__main__':
    unittest.main()