def generate_fibonacci_sequence(n):
    sequence = [0,1]
    if n <= 2:
        return sequence[:n]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

n = int(input("Enter the number of fibonacci numbers to generate : "))
fibonacci_sequence = generate_fibonacci_sequence(n)
print("Fibonacci Sequence : ",fibonacci_sequence)
