import random
from matplotlib import pyplot as plt
import sys

print(f"sys.argv: {sys.argv}")

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    print(f"Calling echo function with text: {text}")
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        print(f"i:{i}")
        echoed_text += f"\n{text[-i:]}"
    return f"{echoed_text.lower()}"

if __name__ == "__main__":
    text = " ".join(sys.argv[1:])
    print(f"First LINE: text: {text}")
    print(echo(text))
    print("END LINE")
#To be added!