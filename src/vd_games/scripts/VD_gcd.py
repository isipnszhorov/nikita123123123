"""GCD game script."""

from vd_games.engine import run_game
from vd_games.games import gcd


def main():
    """Run GCD game."""
    run_game(gcd)


if __name__ == "__main__":
    main()
