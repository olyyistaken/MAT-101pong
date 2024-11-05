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
| x0 y0 z0 | Ball position at time t |
| x1 y1 z1 | Ball position at time t+1 |
| n | Number of time units |

## Example

```bash
./101pong 1.0 2.0 3.0 2.0 4.0 5.0 3
```

## Exit codes

| Code | Reason |
|------|--------|
| 0 | Success |
| 84 | Error (bad arguments) |

## Built with

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)