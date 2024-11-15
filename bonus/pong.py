#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## 101pong
## File description:
## 2D Pong bonus
##

import sys
import math
import random
import pygame

WIDTH, HEIGHT = 900, 600
FPS = 60

PADDLE_W, PADDLE_H = 12, 80
BALL_R = 8
PADDLE_SPEED = 6
BALL_SPEED_INIT = 5.0
BALL_SPEED_MAX = 14.0
SPEED_INCREMENT = 0.25
WINNING_SCORE = 7

WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0  )
GRAY   = (80,  80,  80 )
LGRAY  = (160, 160, 160)
CYAN   = (0,   200, 220)
YELLOW = (240, 200, 0  )
GREEN  = (80,  220, 80 )


class Paddle:
    def __init__(self, x):
        self.rect  = pygame.Rect(x, HEIGHT // 2 - PADDLE_H // 2, PADDLE_W, PADDLE_H)
        self.score = 0

    def move(self, dy):
        self.rect.y = max(0, min(HEIGHT - PADDLE_H, self.rect.y + dy))

    def draw(self, surf):
        pygame.draw.rect(surf, WHITE, self.rect, border_radius=4)


class Ball:
    def __init__(self):
        self.reset(1)

    def reset(self, direction):
        self.x  = float(WIDTH // 2)
        self.y  = float(HEIGHT // 2)
        self.speed = BALL_SPEED_INIT
        angle = random.uniform(-math.pi / 4, math.pi / 4)
        self.vx = direction * self.speed * math.cos(angle)
        self.vy = self.speed * math.sin(angle)

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def bounce_wall(self):
        self.vy = -self.vy
        self.y  = max(float(BALL_R), min(float(HEIGHT - BALL_R), self.y))

    def bounce_paddle(self, paddle):
        # Incidence angle based on hit position on paddle (connects to 101pong math)
        rel   = (self.y - paddle.rect.centery) / (PADDLE_H / 2.0)
        rel   = max(-1.0, min(1.0, rel))
        angle = rel * (math.pi / 3)          # max ±60°
        self.speed = min(self.speed + SPEED_INCREMENT, BALL_SPEED_MAX)
        self.vx = math.copysign(self.speed * math.cos(angle), -self.vx)
        self.vy = self.speed * math.sin(angle)
        # push ball out of paddle
        if self.vx > 0:
            self.x = paddle.rect.right + BALL_R + 1
        else:
            self.x = paddle.rect.left - BALL_R - 1

    @property
    def rect(self):
        return pygame.Rect(int(self.x) - BALL_R, int(self.y) - BALL_R, BALL_R * 2, BALL_R * 2)

    @property
    def angle_deg(self):
        return math.degrees(math.asin(abs(self.vy) / self.speed))

    def draw(self, surf):
        pygame.draw.circle(surf, WHITE, (int(self.x), int(self.y)), BALL_R)


def draw_dashed_center(surf):
    for y in range(0, HEIGHT, 24):
        pygame.draw.rect(surf, GRAY, (WIDTH // 2 - 1, y, 2, 12))


def draw_hud(surf, ball, left, right, font_big, font_sm):
    # Scores
    ls = font_big.render(str(left.score),  True, WHITE)
    rs = font_big.render(str(right.score), True, WHITE)
    surf.blit(ls, (WIDTH // 4  - ls.get_width() // 2, 20))
    surf.blit(rs, (3 * WIDTH // 4 - rs.get_width() // 2, 20))

    # Vector info (the 101pong math on display)
    vx_t = font_sm.render(f"v = ({ball.vx:+.2f}, {ball.vy:+.2f})", True, CYAN)
    ang_t = font_sm.render(f"angle = {ball.angle_deg:.2f}°",        True, YELLOW)
    spd_t = font_sm.render(f"|v| = {ball.speed:.2f}",               True, LGRAY)
    surf.blit(vx_t,  (10, HEIGHT - 70))
    surf.blit(ang_t, (10, HEIGHT - 46))
    surf.blit(spd_t, (10, HEIGHT - 22))

    # Controls
    ctrl = font_sm.render("Z/S   vs   ↑/↓    |    ESC quit", True, GRAY)
    surf.blit(ctrl, (WIDTH - ctrl.get_width() - 10, HEIGHT - 22))


def draw_winner(surf, text, font_big, font_sm):
    surf.fill((0, 0, 0, 180))
    msg  = font_big.render(text, True, GREEN)
    sub  = font_sm.render("Press R to restart  or  ESC to quit", True, LGRAY)
    surf.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 60))
    surf.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT // 2 + 10))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("101pong – 2D Pong")
    clock = pygame.time.Clock()

    font_big = pygame.font.Font(None, 72)
    font_sm  = pygame.font.Font(None, 28)

    left  = Paddle(24)
    right = Paddle(WIDTH - 24 - PADDLE_W)
    ball  = Ball()
    winner = None

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit(0)
                if event.key == pygame.K_r and winner:
                    left.score  = 0
                    right.score = 0
                    ball.reset(1)
                    winner = None

        if not winner:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:     left.move(-PADDLE_SPEED)
            if keys[pygame.K_s]:     left.move(PADDLE_SPEED)
            if keys[pygame.K_UP]:    right.move(-PADDLE_SPEED)
            if keys[pygame.K_DOWN]:  right.move(PADDLE_SPEED)

            ball.update()

            # Wall bounces
            if ball.y - BALL_R <= 0 or ball.y + BALL_R >= HEIGHT:
                ball.bounce_wall()

            # Paddle collisions
            if ball.rect.colliderect(left.rect)  and ball.vx < 0:
                ball.bounce_paddle(left)
            if ball.rect.colliderect(right.rect) and ball.vx > 0:
                ball.bounce_paddle(right)

            # Scoring
            if ball.x < 0:
                right.score += 1
                ball.reset(-1)
            if ball.x > WIDTH:
                left.score += 1
                ball.reset(1)

            if left.score  >= WINNING_SCORE:
                winner = "Left player wins!"
            if right.score >= WINNING_SCORE:
                winner = "Right player wins!"

        # --- Draw ---
        screen.fill(BLACK)
        draw_dashed_center(screen)
        left.draw(screen)
        right.draw(screen)
        ball.draw(screen)
        draw_hud(screen, ball, left, right, font_big, font_sm)
        if winner:
            draw_winner(screen, winner, font_big, font_sm)

        pygame.display.flip()


main()
