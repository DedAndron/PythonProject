from django.shortcuts import render
from datetime import date, timedelta


def home(request):
    context = {}

    if request.method == 'POST':

        action = request.POST.get('action')

        # Task 1: Login
        if action == 'login':

            login = request.POST.get('login')
            password = request.POST.get('password')

            users = {
                'admin': {
                    'password': 'admin123',
                    'role': 'Administrator'
                },
                'user': {
                    'password': 'user123',
                    'role': 'User'
                }
            }

            if login in users and users[login]['password'] == password:
                context['login_result'] = {
                    'success': True,
                    'login': login,
                    'role': users[login]['role']
                }
            else:
                context['login_result'] = {
                    'success': False,
                    'message': 'Incorrect username or password.'
                }

        # Task 2: Calculator
        elif action == 'calculator':

            try:
                num1 = float(request.POST.get('num1'))
                num2 = float(request.POST.get('num2'))
                num3 = float(request.POST.get('num3'))

                operation = request.POST.get('operation')

                numbers = [num1, num2, num3]

                if operation == 'min':
                    result = min(numbers)
                    operation_name = 'Minimum'

                elif operation == 'max':
                    result = max(numbers)
                    operation_name = 'Maximum'

                elif operation == 'avg':
                    result = sum(numbers) / 3
                    operation_name = 'Arithmetic mean'

                else:
                    raise ValueError('Select an operation.')

                context['calculator_result'] = {
                    'result': result,
                    'operation': operation_name
                }

            except (ValueError, TypeError):
                context['calculator_error'] = 'Enter three valid numbers and select an operation.'

        # Task 3: Registration
        elif action == 'registration':

            try:
                age = int(request.POST.get('age'))

                if age < 1 or age > 120:
                    raise ValueError

                registration = {
                    'first_name': request.POST.get('first_name'),
                    'last_name': request.POST.get('last_name'),
                    'age': age,
                    'email': request.POST.get('email'),
                    'gender': request.POST.get('gender'),
                    'address': request.POST.get('address'),
                    'newsletter': request.POST.get('newsletter') == 'on'
                }

                if not all([
                    registration['first_name'],
                    registration['last_name'],
                    registration['email'],
                    registration['gender'],
                    registration['address']
                ]):
                    raise ValueError

                context['registration_result'] = registration

            except (ValueError, TypeError):
                context['registration_error'] = 'Please check the information you entered.'

        # Task 4: Programmer's Day
        elif action == 'programmer_day':

            try:
                year = int(request.POST.get('year'))

                if year < 1 or year > 9998:
                    raise ValueError

                programmer_date = date(year, 1, 1) + timedelta(days=255)

                months = [
                    'January', 'February', 'March',
                    'April', 'May', 'June',
                    'July', 'August', 'September',
                    'October', 'November', 'December'
                ]

                weekdays = [
                    'Monday',
                    'Tuesday',
                    'Wednesday',
                    'Thursday',
                    'Friday',
                    'Saturday',
                    'Sunday'
                ]

                context['programmer_result'] = {
                    'year': year,
                    'day': programmer_date.day,
                    'month': months[programmer_date.month - 1],
                    'weekday': weekdays[programmer_date.weekday()]
                }

            except (ValueError, TypeError):
                context['programmer_error'] = 'Enter a valid year (from 1 to 9998).'

    return render(request, 'main/index.html', context)