import pygame
import random
import os

pygame.init()
pygame.mixer.init()

lebar, tinggi = 600, 600
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("Snake Sederhana")

putih = (255,255,255)
hitam = (0,0,0)
merah = (255,0,0)
hijau = (0,255,0)

clock = pygame.time.Clock()
snake_block = 20
speed = 7

font = pygame.font.SysFont(None, 30)

if os.path.exists("eat.mp3.mpeg"):
    eat_sound = pygame.mixer.Sound("eat.mp3.mpeg")
else:
    eat_sound = None

if os.path.exists("bg_music.mp3.mpeg"):
    pygame.mixer.music.load("bg_music.mp3.mpeg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

if os.path.exists("bg.jpg.jpeg"):
    bg_img = pygame.image.load("bg.jpg.jpeg")
    bg_img = pygame.transform.scale(bg_img, (lebar,tinggi))
else:
    bg_img = None

def tampil_skor(score):
    teks = font.render("Skor: " + str(score), True, hitam)
    layar.blit(teks, [10, 10])

def game():
    game_over = False
    game_close = False

    x = (lebar // 2) // snake_block * snake_block
    y = (tinggi // 2) // snake_block * snake_block

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    foodx =  round (random.randrange(0, lebar-snake_block) / snake_block) * snake_block
    foody =  round (random.randrange(0, tinggi-snake_block) / snake_block) * snake_block

    while not game_over:

        while game_close:
            if bg_img:
                layar.blit(bg_img, (0,0))
            else:
                layar.fill(putih)

            pesan = font.render("Game Over! C= Restart Q=Keluar", True, merah)
            layar.blit(pesan, [120, tinggi/2])
            tampil_skor(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        return
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x>=lebar or x<0 or y>=tinggi or y<0:
            game_close = True

        x += x_change
        y += y_change

        if bg_img:
            layar.blit(bg_img, (0,0))
        else:
            layar.fill(putih)

        pygame.draw.rect(layar, merah, [foodx, foody, snake_block, snake_block])

        snake_head=[x, y]
        snake_list.append(snake_head)

        if len(snake_list)>snake_length:
            del snake_list[0]

        for segmen in snake_list[:-1]:
            if segmen == snake_head:
                game_close = True

        for block in snake_list:
            pygame.draw.rect(layar, hijau, [block[0], block[1], snake_block, snake_block])

        tampil_skor(snake_length - 1)
        pygame.display.update()

        if x == foodx and y == foody:
            if eat_sound:
                eat_sound.play()

            foodx = round(random.randrange(0, lebar - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, tinggi - snake_block) / snake_block) * snake_block
            snake_length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

while True:
    game()