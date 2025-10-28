import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Subject, DAILY_GOAL_MSG, EditSubject, StudyProgress, STUDY_TIME_MSG
from .forms import AddSubjectForm, EditSubjectForm


class SubjectModelTests(TestCase):

    def setUp(self):
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
            subject.full_clean()
            subject.save()
        except ValidationError:
            self.fail("full_clean() raised ValidationError unexpectedly!")


        self.assertEqual(Subject.objects.count(), 1)
        self.assertEqual(Subject.objects.first().daily_goal, 60)


class EditSubjectModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.subject = Subject.objects.create(user=self.user, name='Math', daily_goal=30)

    def test_edit_daily_goal_zero_raises_validation_error(self):
        edit = EditSubject(subject=self.subject, new_daily_goal=0)
        with self.assertRaises(ValidationError) as context:
            edit.full_clean()
        self.assertIn(DAILY_GOAL_MSG, str(context.exception))

    def test_edit_daily_goal_max_raises_validation_error(self):
        edit = EditSubject(subject=self.subject, new_daily_goal=1100)
        with self.assertRaises(ValidationError) as context:
            edit.full_clean()
        self.assertIn(DAILY_GOAL_MSG, str(context.exception))

    def test_edit_goal_valid_saves_correctly(self):
        edit = EditSubject(subject=self.subject, new_daily_goal=180)
        try:
            edit.full_clean()
            edit.save()
        except ValidationError:
            self.fail("full_clean() raised ValidationError unexpectedly!")

class SubjectsProgressModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.subject = Subject.objects.create(user=self.user, name='Math', daily_goal=200)

    def test_user_adds_study_progress_zero_raises_validation_error(self):
        progress = StudyProgress(subject=self.subject, time_studied=0)
        with self.assertRaises(ValidationError) as context:
            progress.full_clean()
        self.assertIn(STUDY_TIME_MSG, str(context.exception))

    def test_user_adds_valid_study_time_saves_correctly(self):
        progress = StudyProgress(subject=self.subject, time_studied=20)
        try:
            progress.full_clean()
            progress.save()
        except ValidationError:
            self.fail("full_clean() raised ValidationError unexpectedly!")


class EditSubjectFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.subject = Subject.objects.create(user=self.user, name='Math', daily_goal=60)

    def test_valid_daily_goal_successful(self):
        form = EditSubjectForm(data={'new_daily_goal': 60}, instance=EditSubject(subject=self.subject))
        self.assertTrue(form.is_valid())

    def test_invalid_daily_goal_fails(self):
        form = EditSubjectForm(data={'new_daily_goal': 0}, instance=EditSubject(subject=self.subject))
        self.assertFalse(form.is_valid())
        self.assertIn('new_daily_goal', form.errors)


class AddSubjectFromTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.subject = Subject.objects.create(user=self.user, name='Math', daily_goal=60)




class AddSubjectFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.subject = Subject.objects.create(user=self.user, name='Math', daily_goal=60)

    def test_valid_subject_form_passes(self):
        form = AddSubjectForm(data={'name': 'History', 'daily_goal': 45}, user=self.user)
        self.assertTrue(form.is_valid())

    def test_duplicate_subject_name_fails(self):
        form = AddSubjectForm(data={'name': 'math', 'daily_goal': 30}, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn("This subject already exists!", form.errors['name'][0])

    def test_name_whitespace_is_stripped(self):
        form = AddSubjectForm(data={'name': '  Physics  ', 'daily_goal': 40}, user=self.user)
        self.assertTrue(form.is_valid())
        cleaned_name = form.clean_name()
        self.assertEqual(cleaned_name, 'Physics')



if __name__ == '__main__':
    unittest.main()