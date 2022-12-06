from django.test import Client, TestCase
from django.urls import reverse

from ..forms import FeedbackForm
from ..models import Feedback


class FeedbackTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_feedback_form_in_context(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)

    def test_text_label(self):
        text_label = FeedbackTest.form.fields['text'].label
        self.assertEquals(text_label, 'Ваш отзыв')

    def test_email_label(self):
        email_label = FeedbackTest.form.fields['email'].label
        self.assertEquals(email_label, 'Ваша почта')

    def test_create_feedback(self):
        feedback_count = Feedback.objects.count()
        form_data = {
            'text': 'qwerty',
            'email': 'example@yandex.ru',
        }

        response = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True,
        )

        self.assertRedirects(response, reverse('feedback:feedback'))

        self.assertEqual(Feedback.objects.count(), feedback_count + 1)

        self.assertTrue(
            Feedback.objects.filter(
                text='qwerty',
                email='example@yandex.ru',
            ).exists()
        )
