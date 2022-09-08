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
