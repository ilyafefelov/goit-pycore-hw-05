def caching_fibonacci():
    """
    Returns a function that computes the Fibonacci sequence using caching.

    The returned function takes a non-negative integer `n` as input and returns the `n`-th Fibonacci number.
    It uses a cache to store previously computed Fibonacci numbers for faster computation.

    Raises:
        TypeError: If `n` is not an integer.
        ValueError: If `n` is a negative integer.

    Returns:
        int: The `n`-th Fibonacci number.
    """
    cache = {}  # Cache to store previously computed Fibonacci numbers

    def fibonacci(n):
        """
        Calculate the nth Fibonacci number.

        Parameters:
        - n (int): The index of the Fibonacci number to calculate.

        Returns:
        - int: The nth Fibonacci number.

        Raises:
        - TypeError: If the input is not an integer.
        - ValueError: If the input is a negative integer.

        """

        # Check input
        if not isinstance(n, int):
            raise TypeError("Must be an integer")
        if n < 0:
            raise ValueError("Must be a non-negative integer")
        
        # Base cases: Fibonacci(0) = 0, Fibonacci(1) = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # Check if the result is in cache
        if n in cache:
            return cache[n]
        
        # Compute the Fibonacci number recursively and store it in the cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

# Test
fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(15))  # 610
print(fib("test"))  # TypeError
print(fib(-1))  # ValueError