import sys
import matplotlib.pyplot as plt


def read_standings(filename):
    standings = {}
    race_details = []
    try:
        with open(filename, "r") as file:
            header = file.readline().strip().split(", ")
            if header[0] != "Competitors":
                sys.exit("First column must be 'Competitors'.")

            competitors = header[1:]
            for competitor in competitors:
                standings[competitor] = []

            for line in file:
                data = line.strip().split(", ")
                race_name = f"{data[1]}"  # Combining race location and type
                race_details.append(race_name)
                for competitor, pts in zip(competitors, data[2:]):
                    standings[competitor].append(
                        int(pts)
                    )  # Directly store points as integers
    except FileNotFoundError:
        sys.exit(f"File {filename} not found.")
    return standings, race_details, competitors


def plot_standings(standings, race_details, competitors):
    plt.figure(figsize=(12, 6))

    for competitor in competitors:
        points = standings[competitor]
        plt.plot(race_details, points, label=competitor, marker="o", linestyle="-")

    plt.xlabel("Race and Type")
    plt.ylabel("Points")
    plt.title("Points Over Races")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()  # Adjust layout to not cut off labels
    plt.show()


def plot_cumulative_scores(standings, race_details, competitors):
    plt.figure(figsize=(12, 6))

    for competitor in competitors:
        cumulative_scores = [
            sum(standings[competitor][: i + 1])
            for i in range(len(standings[competitor]))
        ]
        plt.plot(
            race_details, cumulative_scores, label=competitor, marker="o", linestyle="-"
        )

    plt.xlabel("Race and Type")
    plt.ylabel("Cumulative Points")
    plt.title("Cumulative Scores Over Races")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()  # Adjust layout to not cut off labels
    plt.show()


if __name__ == "__main__":
    filename = "fantasy_standings_dummy.txt"
    standings, race_details, competitors = read_standings(filename)

    # For plotting individual race points
    plot_standings(standings, race_details, competitors)

    # For plotting cumulative scores
    plot_cumulative_scores(standings, race_details, competitors)
