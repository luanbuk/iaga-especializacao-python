import statistics;
import numbers;

def returnNumberOrThrowIfNot(a):
    try:
        a = float(a)
    except (ValueError, TypeError):
        raise TypeError(f"Variable '{a}' should be a number") from None

    if not isinstance(a, numbers.Number):
        raise TypeError(f"Variable '{a}' should be a number")

    return a

values = []
print("Digite o primeiro número: ")
values.append(returnNumberOrThrowIfNot(input()));

print("Digite o segundo número: ")
values.append(returnNumberOrThrowIfNot(input()));

print(f"Média: {statistics.mean(values)}")