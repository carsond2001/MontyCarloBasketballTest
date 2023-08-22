import numpy as np
import concurrent.futures

def is_hit_batch(x, y, max_backball_range, max_hoop_distance):
    distances = np.sqrt(x**2 + y**2)
    hit_mask = (distances <= max_backball_range) & (distances <= max_hoop_distance)
    result = np.where(hit_mask, 'hit', 'nonhit')
    result[distances > max_backball_range] = 'out of range'
    return result

def main():
    max_backball_range = 13.25
    max_hoop_distance = 4.75
    total_shots = 10000000

    hits = 0
    batch_size = 100

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(0, total_shots, batch_size):
            batch_x = np.random.uniform(-max_backball_range, max_backball_range, batch_size)
            batch_y = np.random.uniform(-max_backball_range, max_backball_range, batch_size)
            batch_results = is_hit_batch(batch_x, batch_y, max_backball_range, max_hoop_distance)
            batch_hits = np.count_nonzero(batch_results == 'hit')
            hits += batch_hits

    hit_rate = hits / total_shots

    print(f"Total shots: {total_shots}")
    print(f"Total hits: {hits}")
    print(f"Hit rate: {hit_rate:.2%}")

if __name__ == "__main__":
    main()
