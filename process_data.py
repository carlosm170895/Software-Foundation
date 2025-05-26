#!/usr/bin/env python3
import sys
import csv

if len(sys.argv) != 2:
    print("Usage: python process_data.py input.csv")
    sys.exit(1)

input_file = sys.argv[1]
output_file = "output.csv"

try:
    print(f"Reading input file: {input_file}")
    with open(input_file, mode='r', newline='') as f:
        reader = csv.DictReader(f)
        people = list(reader)

    print("Finished reading, starting calculations...")

    output_data = []
    for person in people:
        name = person["Name"]
        age = int(person["Age"])
        height_m = float(person["Height"])

        future_age = age + 10
        height_cm = round(height_m * 100, 1)
        greeting = (
            f"Hello, {name}! You are {age} years old and {height_m:.2f} m tall. "
            f"In 10 years, you'll be {future_age} years old and {height_cm:.1f} cm tall."
        )

        output_data.append({
            "Name": name,
            "Age": age,
            "Future Age": future_age,
            "Height (m)": f"{height_m:.2f}",
            "Height (cm)": height_cm,
            "Greeting": greeting
        })

    with open(output_file, mode='w', newline='') as f:
        fieldnames = ["Name", "Age", "Future Age", "Height (m)", "Height (cm)", "Greeting"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_data)

    print(f"Results written to {output_file}")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except KeyError:
    print("Error: Input file must have columns: Name, Age, Height.")
except Exception as e:
    print(f"Unexpected error: {e}")
