# FDE-Technical-Screen
A scalable backend system built with Python (FastAPI, Django, Flask) featuring REST APIs, microservices, and data pipelines. Includes optimized SQL databases, Docker + Kubernetes deployment, CI/CD, and secure auth with OAuth2/JWT. Designed for performance, scalability, and reliability.


# Package Sorting Robot

This project implements a sorting function for robotic automation that dispatches packages into the correct stack based on their dimensions and mass.  

It was built as part of a coding challenge for a robotic automation factory scenario.  

---

## Objective

The robotic arm must decide whether a package is **STANDARD**, **SPECIAL**, or **REJECTED** based on the following rules:

### Rules

- A package is **bulky** if:
  - Its volume (`Width × Height × Length`) is **≥ 1,000,000 cm³**, OR  
  - Any one of its dimensions is **≥ 150 cm**.  

- A package is **heavy** if:
  - Its mass is **≥ 20 kg**.  

### Sorting Logic

- **STANDARD** → Not bulky and not heavy  
- **SPECIAL** → Either bulky or heavy (but not both)  
- **REJECTED** → Both bulky **and** heavy  

---

## Implementation

The core function is:

```python
def sort(width, height, length, mass):
    volume = width * height * length
    bulky = True if (volume >= 1000000 or max(width, height, length) >= 150) else False
    heavy = True if mass >= 20 else False

    if bulky and heavy:
        return "REJECTED"
    return "SPECIAL" if (bulky or heavy) else "STANDARD"

Project Structure
.
├── sort.py        # Main implementation file
├── tests.py       # Simple test cases
└── README.md      # Documentation

Usage

git clone https://github.com/your-username/package-sorting-robot.git
cd package-sorting-robot
python3 sort.py


Examples

print(sort(50, 40, 30, 10))     # STANDARD
print(sort(200, 30, 30, 10))    # SPECIAL (bulky)
print(sort(40, 40, 40, 25))     # SPECIAL (heavy)
print(sort(200, 200, 200, 30))  # REJECTED


Output

STANDARD
SPECIAL
SPECIAL
REJECTED


Testing

python3 sort.py


