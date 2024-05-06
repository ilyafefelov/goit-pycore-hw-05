import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]: 
    """
    Generator function that extracts floating-point numbers from a given text.

    Args:
        text (str): The input text from which numbers will be extracted.

    Yields:
        float: The floating-point numbers extracted from the text.

    """
    pattern = r'\b\d+\.\d+\b' # Match floating-point numbers in the text 
    matches = [match.group() for match in re.finditer(pattern, text)] # Find all matches in the text and convert to a list
    
    print('Вилучені числа: ', matches)
    
    for match in matches: # Iterate over the matches 
        try:
            yield float(match) # Yield the floating-point number
        except (ValueError, TypeError) as e:
            print(f"Invalid number: {match}. Error: {e}")

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Calculate the sum of profits using the provided function.

    Args:
        text (str): The input text.
        func (Callable[[str], Generator[float, None, None]]): The function to extract profits from the text.

    Returns:
        float: The sum of profits.

    """
    numbers = func(text)
    
    try:
        return sum(numbers)
    except (TypeError, ValueError) as e:
        print(f"Invalid input: unable to calculate the sum of profits. Error: {e}")
        return 0.0



# Test
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")