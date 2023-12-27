import pygame as pg

y, step, head= segments = [15, 16, 17]
n,apple = step, 99
screen_fill = pg.display.set_mode([225] * 2, pg.SCALED).fill
speed=150
score=0

while segments.count(head) % 2 * head % n * (head & 240):
    if e := pg.event.get(768):
        step = (e[0].key % 4 * 17 + 15) % 49 - n
    segments = segments[apple != head:] + [head + step]

    screen_fill('dark green')
    if apple == head:
        score += 1
        print(f"Score: {score}")
        apple = segments[0]
    for i, v in enumerate([apple] + segments):
        screen_fill('green' if i else 'red',
        ((v - 1) % n * y,  (v - n) // n * y, y, y))
    pg.display.flip()
    head += step
    pg.time.wait(speed)

print(f"Final score is {score}!")
if score<10:
    print("Loser 👎")
elif score>20:
    print("you are a pro 👑")
else:
    print("keep practicing")