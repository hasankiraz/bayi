import argparse


def greet(name: str) -> None:
    """Print a greeting message."""
    if name:
        print(f"Merhaba, {name}! Bu bayi projesine hoş geldiniz.")
    else:
        print("Merhaba! Bu bayi projesine hoş geldiniz.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple greeting tool")
    parser.add_argument("--name", type=str, default="", help="Name to greet")
    args = parser.parse_args()
    greet(args.name)


if __name__ == "__main__":
    main()
