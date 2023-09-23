from django.shortcuts import render
from .gcd import gcd_numbers

def calculate_gcd(request):
    if request.method == 'POST':
        input_numbers = request.POST.get('numbers', '').split()
        try:
            input_numbers = [int(num) for num in input_numbers if num.isdigit() and int(num) > 0]
            if len(input_numbers) >= 2:
                gcd = gcd_numbers(input_numbers)
                return render(request, 'gcd_calculator/result.html', {'gcd': gcd})
            else:
                error_message = "Please enter at least two valid positive integers."
        except ValueError:
            error_message = "Invalid input. Please enter positive integers separated by spaces."
    else:
        error_message = None

    return render(request, 'gcd_calculator/calculate_gcd.html', {'error_message': error_message})

















# from django.utils import gcd_two_numbers, gcd_numbers

# Create your views here.

# def calculate_gcd(request):
#     # if request.method == 'POST':
#         # fist_number = request.POST.get('number1', '')
#         # second_number = request.POST.get('number2', '')

#     # def computegcd(a, b):
#     #     if b==0:
#     #         return a
#     #     else:
#     #         return computegcd(b, a%b)
        
#     # gcd_number = computegcd(Numbers.second_number, Numbers.first_number%Numbers.second_number)




#     return render(request, 'gcd_calculator/index.html', {
#         'model':model
#         })
