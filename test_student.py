import unittest
from datetime import timedelta
from student import Student
from unittest.mock import patch


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("John", "Doe")

    def test_full_name(self):
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        self.assertNotEqual(self.student.email, "John.Doe@email.com")
        self.assertEqual(self.student.email, "john.doe@email.com")
        self.student = Student("Alan", "Sample")
        self.assertEqual(self.student.email, "alan.sample@email.com")

    def test_apply_extension(self):
        original_end_date = self.student.end_date
        num_days = 2
        self.student.apply_extension(num_days)
        self.assertEqual(
            original_end_date + timedelta(num_days),
            self.student.end_date,
        )

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failure(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False
            mocked_get.return_value.text = (
                "Something went wrong with the requests"
            )

            schedule = self.student.course_schedule()
            self.assertEqual(
                schedule, "Something went wrong with the requests"
            )


if __name__ == "__main__":
    unittest.main()
