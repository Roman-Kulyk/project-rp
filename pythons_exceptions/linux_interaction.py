def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")

try:
    linux_interaction()
except RuntimeError as error:
    print(error)
    print("Doing even more Linux things.")