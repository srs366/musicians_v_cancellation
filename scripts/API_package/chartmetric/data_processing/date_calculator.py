import datetime
from dateutil.relativedelta import relativedelta

def date_calculator(incident_date, n_months, n_days=0):

    '''Take a date as input (incident_date) and return the date values that are
    one month prior and post

    incident_date: the date to calculate pre/post in string form
    n_month: the number of months you want to calculate before and
    after
    n_days: the number of days to calculate before and after. Default value is
    0 if left blanks

    If both n_month and n_days are specified the dates pre/post will be the
    sum of both'''

    date_format = '%Y-%m-%d'

    # Convert to datetime and reformat
    dtObj = datetime.datetime.strptime(incident_date, date_format)

    # Perform date arithmetic
    since_date = (dtObj - relativedelta(months=n_months,days=n_days)).date()
    until_date = (dtObj + relativedelta(months=n_months,days=n_days)).date()

    # Convert back to strings
    since_date = str(since_date)
    until_date = str(until_date)

    return since_date, until_date

def date_calculator_socials(incident_date, n_days=50):

    '''Same as other date calculator, but is for the socials to take into account for 100
    day limit on API calls'''

    date_format = '%Y-%m-%d'

    # Convert to datetime and reformat
    dtObj = datetime.datetime.strptime(incident_date, date_format)

    # Perform date arithmetic
    since_date = (dtObj - relativedelta(days=n_days)).date()
    until_date = (dtObj + relativedelta(days=n_days)).date()

    # Convert back to strings
    since_date = str(since_date)
    until_date = str(until_date)

    return since_date, until_date

def date_calculator_socials2(since_date,until_date):

    '''Same as other date calculator, but is for the socials to take into account for 100
    day limit on API calls'''

    date_format = '%Y-%m-%d'

    # Convert to datetime and reformat
    dtObj1 = datetime.datetime.strptime(since_date, date_format)
    dtObj2 = datetime.datetime.strptime(until_date, date_format)

    # Perform date arithmetic
    date1 = (dtObj1 - relativedelta(days=1)).date()
    date2 = (dtObj1 - relativedelta(days=101)).date()
    date3 = (dtObj2 + relativedelta(days=1)).date()
    date4 = (dtObj2 + relativedelta(days=101)).date()

    # Convert back to strings
    date_pre1 = str(date1)
    date_pre2 = str(date2)
    date_post_1 = str(date3)
    date_post2 = str(date4)

    return date_pre1, date_pre2, date_post_1, date_post2
