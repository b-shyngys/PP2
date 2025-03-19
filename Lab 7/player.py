import pygame
import os

pygame.init()


screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Keyboard Music Player")


music_folder = "music" 
playlist = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

if not playlist:
    raise Exception("Нет mp3 файлов в папке 'music'")

current_track = 0


pygame.mixer.init()

def load_track(index):
    pygame.mixer.music.load(os.path.join(music_folder, playlist[index]))
    pygame.mixer.music.play()

load_track(current_track)
paused = False


button_play = pygame.Rect(50, 150, 50, 30)
button_stop = pygame.Rect(110, 150, 50, 30)
button_next = pygame.Rect(170, 150, 50, 30)
button_prev = pygame.Rect(230, 150, 50, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                elif paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    load_track(current_track)

            elif event.key == pygame.K_DOWN:
                pygame.mixer.music.stop()

            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(playlist)
                load_track(current_track)

            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(playlist)
                load_track(current_track)


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_play.collidepoint(event.pos):
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                elif paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    load_track(current_track)

            elif button_stop.collidepoint(event.pos):
                pygame.mixer.music.stop()

            elif button_next.collidepoint(event.pos):
                current_track = (current_track + 1) % len(playlist)
                load_track(current_track)

            elif button_prev.collidepoint(event.pos):
                current_track = (current_track - 1) % len(playlist)
                load_track(current_track)

    screen.fill((30, 30, 30))


    pygame.draw.rect(screen, (0, 255, 0), button_play)
    pygame.draw.rect(screen, (255, 0, 0), button_stop)
    pygame.draw.rect(screen, (0, 0, 255), button_next)
    pygame.draw.rect(screen, (255, 255, 0), button_prev)


    font = pygame.font.Font(None, 24)
    screen.blit(font.render('Play', True, (0, 0, 0)), (button_play.x + 5, button_play.y + 5))
    screen.blit(font.render('Stop', True, (0, 0, 0)), (button_stop.x + 5, button_stop.y + 5))
    screen.blit(font.render('Next', True, (0, 0, 0)), (button_next.x + 5, button_next.y + 5))
    screen.blit(font.render('Prev', True, (0, 0, 0)), (button_prev.x + 5, button_prev.y + 5))

    pygame.display.flip()

pygame.quit()