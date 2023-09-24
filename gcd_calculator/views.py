from django.shortcuts import render  # import render function to render html templates
from .gcd import gcd_numbers #to import the 

def calculate_gcd(request): #view fuction that take a request 
    if request.method == 'POST': # cheking the request method is POST 
        input_numbers = request.POST.get('numbers', '').split()  # Getting the input string

        # Split the input string into a list of strings with filter and validate the input
        input_numbers = [int(num) for num in input_numbers if num.isdigit() and int(num) > 0]    

        # Checking if there are at least two valid positive integers
        if len(input_numbers) >= 2:
            gcd = gcd_numbers(input_numbers)

            # renders the 'result.html' template with the GCD value passed as context data
            return render(request, 'gcd_calculator/result.html', {'gcd': gcd})
        else:
            error_message = "Please enter at least two valid positive integers." # message informing the user to enter at least two valid positive integers.
    else:
        error_message = None # this indicating that there are no errors or messages to display.

    # renders the 'calculate_gcd.html' template
    return render(request, 'gcd_calculator/calculate_gcd.html', {'error_message': error_message})