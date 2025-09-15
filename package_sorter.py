def sort(width, height, length, mass):
    """
    Sort packages into STANDARD, SPECIAL, or REJECTED
    based on volume, dimensions, and mass.

    Args:
        width (int): Width in cm
        height (int): Height in cm
        length (int): Length in cm
        mass (int): Mass in kg

    Returns:
        str: The stack name ("STANDARD", "SPECIAL", or "REJECTED")
    """
    volume = width * height * length

    # Check bulky and heavy conditions
    bulky = True if (volume >= 1000000 or max(width, height, length) >= 150) else False
    heavy = True if mass >= 20 else False

    # Determine stack
    if bulky and heavy:
        return "REJECTED"
    return "SPECIAL" if (bulky or heavy) else "STANDARD"


# ------------------ Tests ------------------
if __name__ == "__main__":
    # STANDARD: small dimensions, light weight
    print(sort(50, 40, 30, 10))  # Expected: STANDARD

    # SPECIAL: bulky but not heavy
    print(sort(200, 30, 30, 10))  # Expected: SPECIAL

    # SPECIAL: heavy but not bulky
    print(sort(40, 40, 40, 25))  # Expected: SPECIAL

    # REJECTED: both heavy and bulky
    print(sort(200, 200, 200, 30))  # Expected: REJECTED
