from constant import *
from grader.models import TimeLog
from math import sqrt


def calculate_score():
    total_score = 0
    records = TimeLog.objects.all()
    print TimeLog.objects.count()
    for record in records:
        rate = activity_weights[record.activity]['rate']
        hours = get_hrs_from_timedelta(record.duration)
        score = rate * hours
        print 'activity: %s, score = rate(%d) x duration(%d) = %d' % (record.activity, rate, hours, score)
        total_score += score

    print 'total score=%d' % total_score
    return total_score


def get_hrs_from_timedelta(td):
    days, seconds = td.days, td.seconds
    hours = days * 24 + float(seconds) / 3600
    return hours


def cost_effectiveness(records):
    # calculate the cost-effectiveness, inspired by marginal benefit function
    # in particular, inspired by Cobb-Douglas production function
    # a 6 minutes offset is to correct the effective function.
    # if one spend less than 6 minutes in an activity, no benefit has been obtained,
    # it is assumed that it takes 6 minutes to be mentally prepared
    # -- from wikipedia, sigmoid --
    # Many natural processes, such as those of complex system learning curves,
    # exhibit a progression from small beginnings that accelerates and approaches a climax over time.
    # When a detailed description is lacking, a sigmoid function is often used[2] .
    #
    # y=at^-1/2
    total_score = 0
    for record in records:
        rate = activity_weights[record.activity]['rate']
        hours = get_hrs_from_timedelta(record.duration)
        expd = activity_weights[record.activity]['expected']
        score = rate * expd * sqrt(float(hours) / expd)
        print 'activity: %s, score = rate(%d) x duration(%d) = %d' % (record.activity, rate, hours, score)
        total_score += score

    print 'total score=%d' % total_score
    return total_score
