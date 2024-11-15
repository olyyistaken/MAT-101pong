# 101pong

Epitech project — Mathematics for 3D programming.

Computes the velocity vector of a ball, predicts its position at time `t + n`, and calculates the incidence angle with the paddle.

## Usage

```bash
make
./101pong x0 y0 z0 x1 y1 z1 n
```

## Arguments

| Argument | Description |
|----------|-------------|
| x0 y0 z0 | Ball position at time t-1 |
| x1 y1 z1 | Ball position at time t |
| n | Time shift (integer ≥ 0) |

## Example

```bash
./101pong 1.1 3 5 -7 9 2 4
# The velocity vector of the ball is:
# (-8.10, 6.00, -3.00)
# At time t + 4, ball coordinates will be:
# (-39.40, 33.00, -10.00)
# The incidence angle is:
# 16.57 degrees
```

## Exit codes

| Code | Reason |
|------|--------|
| 0 | Success |
| 84 | Error (bad arguments) |

## Bonus — 2D Pong

A playable 2D Pong game built with pygame. Requires `pygame` (`pip install pygame`).

```bash
make bonus
./bonus/pong
```

| Key | Action |
|-----|--------|
| Z / S | Left paddle up / down |
| ↑ / ↓ | Right paddle up / down |
| R | Restart after a win |
| ESC | Quit |

First to 7 points wins. The HUD displays the live velocity vector and incidence angle, directly using the math from the main project.

## Built with

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.6-green?style=flat)
