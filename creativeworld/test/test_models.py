from django.test import TestCase
from creativeworld.models import Contact


class ContactModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Contact.objects.create(name='John', email='testwave@gmail.com', 
        subject='Testing', message='Testing contact model code')

        Contact.objects.create(name="Hogan", email='princeaffumasante@gmail.com',
        subject='Transfer News', message="These are all the latest transfer news")

    def test_name_label(self):
        '''function to test for name field in contact model'''
        userContact = Contact.objects.get(id=1)
        field_label = userContact._meta.get_field('name').verbose_name

        self.assertEqual(field_label, 'Full Name')

    def test_name_max_length(self):
        '''function to test for max length of name in the Contact model'''
        name = Contact.objects.get(id=1)
        name_max_length = name._meta.get_field('name').max_length

        self.assertEqual(name_max_length, 200)

    def test_email_label(self):
        '''function to test for email label from contact model'''
        useremail = Contact.objects.get(id=1)
        field_label = useremail._meta.get_field('email').verbose_name

        self.assertEqual(field_label, 'Email')

    def test_duplicate_email(self):
        ''' This function is to check for duplicates of emails'''
        userid_1 = Contact.objects.get(id=1).email
        userid_2 = Contact.objects.get(id=2).email

        self.assertNotEqual(userid_1, userid_2)

    def test_subject_label(self):
        ''' function to test for subject field in the Contact model'''
        subject = Contact.objects.get(id=1)
        field_label = subject._meta.get_field('subject').verbose_name

        self.assertEqual(field_label, 'Subject')

    def test_subject_max_length(self):
        '''To test for the max length of the subject field in Contact model'''
        subject = Contact.objects.get(id=2)
        subject_max_length = subject._meta.get_field('subject').max_length

        self.assertEqual(subject_max_length, 400)

    def test_message_label(self):
        '''To test message label in Contact model'''
        message_id = Contact.objects.get(id=2)
        message_label = message_id._meta.get_field('message').verbose_name

        self.assertEqual(message_label, "Message")

    def test_message_max_length(self):
        ''' To test the max length of message field in Contact model'''
        message_id = Contact.objects.get(id=1)
        message_max = message_id._meta.get_field('message').max_length

        self.assertEqual(message_max, None)