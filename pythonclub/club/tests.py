from django.test import TestCase
from .models import Resource, Meeting, MeetingMinute, Event

# Create your tests here.
#model test

class ResourceTest(TestCase):
    def test_stringOutput(self):
        testresource=Resource(resourcename='Lenovo Yoga 720')
        self.assertEqual(str(testresource), testresource.resourcename)

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class MeetingTest(TestCase):
    def test_stringOutput(self):
        testmeeting=Meeting(meetingtitle='UW Student')
        self.assertEqual(str(testmeeting), testmeeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MinuteTest(TestCase):
    def test_stringOutput(self):
        testminute=MeetingMinute(minutetext='Meet UW Student')
        self.assertEqual(str(testminute), testminute.minutetext)

    def test_tablename(self):
        self.assertEqual(str(MeetingMinute._meta.db_table), 'meetingminute')

class EventTest(TestCase):
    def test_stringOutput(self):
        testevent=Event(eventtitle='New Year')
        self.assertEqual(str(testevent), testevent.eventtitle)

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')
