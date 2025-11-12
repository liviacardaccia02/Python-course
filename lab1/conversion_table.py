def celsius_to_fahrenheit(celsius):
    converted = []
    for c in celsius:
        converted.append((c * 9/5) + 32)
    return converted

def fahrenheit_to_celsius(fahrenheit):
    converted = []
    for f in fahrenheit:
        converted.append( (f - 32) * 5/9)
    return converted

def main():
    print("Temperature Conversion Table")
    target_unit = ''
    while (target_unit not in ('C', 'F')):
        target_unit = input("Enter the target unit ('C' or 'F'): ").upper() 

    start_value = int(input("Enter the start value: "))
    end_value = int(input("Enter the end value: "))

    step = 1 if start_value <= end_value else -1

    if target_unit == 'C':
        converter = celsius_to_fahrenheit
        first_label = "°C"
        second_label = "°F"
    else:
        converter = fahrenheit_to_celsius
        first_label = "°F"
        second_label = "°C"

    original = range(start_value, end_value - 1, step)
    converted = converter(original)

    for orig, conv in zip(original, converted):
        print(f"{orig} {first_label} = {conv:.2f} {second_label}")

if __name__ == "__main__":
    main()