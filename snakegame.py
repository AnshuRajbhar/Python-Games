import pygame as pg

pg.init()  # Initialize pygame
pg.mixer.init()  # Initialize the mixer for sound

# Load the sound file (make sure 'click.wav' is in the same directory or provide the full path)
try:
    eat_sound = pg.mixer.Sound('C:\\Users\\DELL\\Music\\applecrunch.wav')
except FileNotFoundError:
    print("Sound file not found. Make sure 'click.wav' is in the correct directory.")
    eat_sound = None

y, step, head = segments = [15, 16, 17]
n, apple = step, 99

screen_width, screen_height = 225, 225
screen = pg.display.set_mode([screen_width, screen_height], pg.SCALED)
font = pg.font.Font(None, 30)

score = 0

while segments.count(head) % 2 * head % n * (head & 240):
    for e in pg.event.get(768):
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_UP and step != n:
                step = -n
            elif e.key == pg.K_DOWN and step != -n:
                step = n
            elif e.key == pg.K_LEFT and step != 1:
                step = -1
            elif e.key == pg.K_RIGHT and step != -1:
                step = 1

    segments = segments[apple != head:] + [head + step]

    screen.fill('black')

    if apple == head:
        apple = segments[0]
        score += 1
        if eat_sound:  # Play the sound when an apple is eaten
            eat_sound.play()

    for i, v in enumerate([apple] + segments):
        screen.fill('green' if i else 'red', ((v - 1) % n * y, (v - n) // n * y, y, y))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 0, screen_width, 30))
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 0))

    pg.display.flip()

    head += step

    pg.time.wait(100)
