# /// script
# dependencies = [
#   "shapely"
# ]
# ///

import os
from shapely import Polygon, box


def parse(path):
    with open(path) as f:
        tiles = f.readlines()
    return [[int(c) for c in t.split(",")] for t in tiles]


def brute_force(tiles):
    max_area = 0
    for tile1 in range(len(tiles)):
        for tile2 in range(tile1 + 1, len(tiles)):
            tile_a = tiles[tile1]
            tile_b = tiles[tile2]
            area = (abs(tile_a[0] - tile_b[0]) + 1) * (abs(tile_a[1] - tile_b[1]) + 1)
            max_area = max(max_area, area)
    return max_area


def part_2(tiles):
    polygon = Polygon(tiles)
    max_area = 0
    for tile1 in range(len(tiles)):
        for tile2 in range(tile1 + 1, len(tiles)):
            tile_a = tiles[tile1]
            tile_b = tiles[tile2]
            area = (abs(tile_a[0] - tile_b[0]) + 1) * (abs(tile_a[1] - tile_b[1]) + 1)
            tile_box = box(*tile_a, *tile_b)
            if polygon.contains(tile_box):
                max_area = max(max_area, area)
    return max_area


if __name__ == "__main__":
    example_tiles = parse("example.txt")

    assert 50 == brute_force(example_tiles)
    assert 24 == part_2(example_tiles)
    if not os.getenv("SKIP_INPUT"):
        input_tiles = parse("input.txt")
        print(brute_force(input_tiles))
        print(part_2(input_tiles))
