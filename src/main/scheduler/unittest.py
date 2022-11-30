import random

from Scheduler import *


def general_test():
    caregiver = 'mc'
    pwd = '1234Llcc#'
    patient = 'yx'
    create_caregiver(['', caregiver, pwd])
    login_caregiver(['', caregiver, pwd])
    print('login caregiver %s success' % caregiver)

    vaccines = ['vac1', 'vac2', 'vac3']
    for vaccine in vaccines:
        add_doses([None, vaccine, 100])

    available_dates = ['03-02-2022', '03-03-2022', '03-04-2022']
    for d in available_dates:
        upload_availability(["", d])

    # test search_caregiver_schedule
    # print as caregiver
    search_caregiver_schedule(["", available_dates[0]])
    logout([''])

    # print as patient
    create_patient(["", patient, pwd])
    login_patient(["", patient, pwd])
    search_caregiver_schedule(["", available_dates[0]])

    # test reserve
    reserve(["", available_dates[0], vaccines[0]])

    # test show_appointments
    show_appointments([""])


def test_update_available(caregiver, dates):
    pwd = '1234Llcc#'
    create_caregiver(['', caregiver, pwd])
    login_caregiver(['', caregiver, pwd])
    print(caregiver, pwd, dates)
    for d in dates:
        upload_availability(["", d])
    logout([caregiver, ''])


def test_search_as_caregiver():
    caregiver = 'mc'
    pwd = '1234Llcc#'
    patient = 'yx'
    create_caregiver(['', caregiver, pwd])
    login_caregiver(['', caregiver, pwd])
    search_caregiver_schedule(["", '02-02-2022'])


def test_search_as_patient():
    pwd = '1234Llcc#'
    patient = 'yx'
    create_patient(['', patient, pwd])
    login_patient(['', patient, pwd])
    search_caregiver_schedule(["", '02-02-2022'])


def get_random_date():
    return '%s-%s-%s' % (random.randint(1, 12), random.randint(1, 28), random.randint(2000, 2023))


if __name__ == '__main__':
    # general_test()
    #test_update_available('mc%s' % random.randint(1, 100), [get_random_date() for _ in range(3)])

    #test_update_available('mc%s' % random.randint(100, 1000), ['02-02-2022'])
    #test_update_available('mc%s' % random.randint(1000, 10000), ['02-02-2022'])
    #test_update_available('mc%s' % random.randint(10000, 100000), ['02-02-2022'])

    #test_search_as_caregiver()
    #test_search_as_patient()

    #pwd = '1234Llcc#'
    #patient = 'yx'
    #create_patient(['', patient, pwd])
    #login_patient(['', patient, pwd])
    # reserve(['', '02-02-2022', 'vac2'])
    #logout(['', ])

    #pwd = '1234Llcc#'
    #patient = 'yx'
    #create_patient(['', patient, pwd])
    #login_patient(['', patient, pwd])
    #show_appointments([' '])
    #logout(['', ])


    #pwd = '1234Llcc#'
    #caregiver = 'mc'
    #create_caregiver(['', caregiver, pwd])
    #login_caregiver(['', caregiver, pwd])
    #show_appointments([' '])
    #logout(['', ])

    patient = 'yx123'
    create_patient(['', patient, '123'])
    create_patient(['', patient, '123lL'])
    create_patient(['', patient, '123l#'])

    caregiver = 'mc123'
    create_caregiver(['', caregiver, '123'])
    create_caregiver(['', caregiver, '123l'])
    create_caregiver(['', caregiver, '123l#'])
