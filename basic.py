'''Python: Basic

15 points

This assignment will develop your familiarity with doing simple computations in Python.
'''
import math
def savings(gross_pay, tax_rate, expenses):
    after_tax = math.floor((1-tax_rate)*gross_pay)
    takehome_pay = after_tax - expenses
    return takehome_pay

import math
def material_waste(total_material, material_units, num_jobs, job_consumption):
    job_waste = total_material - (num_jobs * job_consumption)
    return str(job_waste) + material_units

import math
def interest(principal, rate, periods):
    simple_interest=math.floor((principal*rate*periods)+principal)
    return simple_interest
