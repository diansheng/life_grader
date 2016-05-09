from django.test import TestCase
from grader.modelizer.formula import calculate_score, cost_effectiveness
from grader.models import TimeLog
from datetime import timedelta


class SimpleTest(TestCase):
    def setUp(self):
        TimeLog.objects.create(activity='reading', duration=timedelta(hours=2))
        TimeLog.objects.create(activity='exercise', duration=timedelta(hours=1))
        TimeLog.objects.create(activity='learning', duration=timedelta(hours=3))
        TimeLog.objects.create(activity='guitar', duration=timedelta(hours=1))
        TimeLog.objects.create(activity='guitar', duration=timedelta(hours=2))

    # Create your tests here.
    def test_score(self):
        s = calculate_score()
        t = cost_effectiveness(TimeLog.objects.all())
        self.assertTrue(s>0)
        self.assertTrue(t>0)
        print 'simple score', s
        print 'effectiveness score', t
