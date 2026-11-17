"""Training driver for pulse encoders."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    print(f"training pulse encoder with {args.config}")


if __name__ == "__main__":
    main()
