from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def validate_policy_criteria(request):
    if request.method == 'POST':
        # Get request data
        sum_assured = request.POST.get('sum_assured')
        age = request.POST.get('age')
        annual_income = request.POST.get('annual_income')
        otp = request.POST.get('otp')

        # Validate the sum assured
        if sum_assured not in [50000, 100000, 150000, 200000]:
            return JsonResponse({'message': 'Invalid sum assured.'}, status=400)

        # Validate the age
        if age < 18 or age > 70:
            return JsonResponse({'message': 'Age must be between 18 and 70.'}, status=400)

        # Validate the annual income
        if annual_income < 40000:
            return JsonResponse({'message': 'Annual income must be more than 40000.'}, status=400)

        # Validate the OTP
        if not otp:
            return JsonResponse({'message': 'OTP authentication is required.'}, status=400)

        # If all criteria are valid
        return JsonResponse({'message': 'All criteria are valid.'}, status=200)

    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=405)