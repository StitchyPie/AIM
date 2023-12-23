import django.utils.timezone as timezone

def calculate_age(dob):
    today = timezone.now().date()
    age = today.year - dob.year
    if today < dob.replace(year=today.year):
        age -= 1
    return age