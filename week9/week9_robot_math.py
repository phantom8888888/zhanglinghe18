#!/usr/bin/env python3
"""Week 9 robot vision math helpers."""

import math


def pixel_to_angle(pixel_x, image_width, horizontal_fov_deg):
    center = image_width / 2
    normalized = (pixel_x - center) / center
    return normalized * math.radians(horizontal_fov_deg / 2)


def estimate_distance(real_width, focal_length_px, observed_width_px):
    return real_width * focal_length_px / observed_width_px


if __name__ == "__main__":
    print("angle(rad):", round(pixel_to_angle(400, 640, 70), 4))
    print("distance(m):", round(estimate_distance(0.15, 800, 120), 3))
