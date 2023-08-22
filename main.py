import random
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import time


def is_hit(x, y, max_backball_range, max_hoop_distance):
    distance = (x ** 2 + y ** 2) ** 0.5

    if distance <= max_backball_range:
        if distance <= max_hoop_distance:
            return "hit"
        else:
            return "nonhit"
    else:
        return "out of range"


def visualize_shots(shots, max_backball_range, max_hoop_distance, current_hit_rate):
    plt.clf()  # Clear the current figure
    hoop_circle = plt.Circle((0, 0), max_hoop_distance, color='green', alpha=0.3)
    backball_circle = plt.Circle((0, 0), max_backball_range, color='blue', fill=False)

    ax = plt.gca()
    ax.add_artist(hoop_circle)
    ax.add_artist(backball_circle)

    for x, y, result in shots:
        if result == "hit":
            color = 'red'
            plt.scatter(x, y, color=color)
        else:
            color = 'black'
            plt.scatter(x, y, color=color, alpha=0.5)

    plt.xlim(-max_backball_range, max_backball_range)
    plt.ylim(-max_backball_range, max_backball_range)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Basketball Shots')
    plt.legend(['Hoop', 'Max Range', 'Hits', 'Non-Hits'])

    # Display current hit rate
    plt.text(max_backball_range * 0.6, max_backball_range * 0.8, f'Hit Rate: {current_hit_rate:.2%}', fontsize=12,
             color='black')

    plt.show()


def main():
    max_backball_range = 13.25
    max_hoop_distance = 4.75
    total_shots = 10000  # Adjust the number of shots

    plt.ion()  # Turn on interactive mode for real-time plotting
    fig = plt.figure(figsize=(8, 8))

    plt.xlim(-max_backball_range, max_backball_range)
    plt.ylim(-max_backball_range, max_backball_range)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Basketball Shots')
    plt.legend(['Hoop', 'Max Range', 'Hits', 'Non-Hits'])

    plt.draw()
    plt.pause(0.01)

    hits = 0
    shots = []

    for i in range(total_shots):
        x = random.uniform(-max_backball_range, max_backball_range)
        y = random.uniform(-max_backball_range, max_backball_range)

        result = is_hit(x, y, max_backball_range, max_hoop_distance)
        if result != "out of range":
            shots.append((x, y, result))

        if result == "hit":
            hits += 1

        current_hit_rate = hits / (i + 1)
        visualize_shots(shots, max_backball_range, max_hoop_distance, current_hit_rate)

        plt.pause(0.01)
        clear_output(wait=True)

    plt.ioff()  # Turn off interactive mode after finishing
    plt.show()

    hit_rate = hits / total_shots

    print(f"Total shots: {total_shots}")
    print(f"Total hits: {hits}")
    print(f"Hit rate: {hit_rate:.2%}")


if __name__ == "__main__":
    main()
