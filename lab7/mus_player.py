import pygame
import os


pygame.init()


WIDTH, HEIGHT = 300, 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mus Player")


music_dir = "music"
music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]
if not music_files:
    print("No MP3 files found in the 'music' directory.")
    pygame.quit()
    exit()

current_track = 0

def play_music():
    """Current track."""
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    pygame.mixer.music.play()
    print(f"NOW PLAYING: {music_files[current_track]}")

def stop_music():
    """Stops the music."""
    pygame.mixer.music.stop()
    print("Stopped")

def next_track():
    """Next track."""
    global current_track
    current_track = (current_track + 1) % len(music_files)
    play_music()

def previous_track():
    """Previous track."""
    global current_track
    current_track = (current_track - 1) % len(music_files)
    play_music()

play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Spacebar for play/pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print("Paused")
                else:
                    pygame.mixer.music.unpause()
                    print(f"Playing: {music_files[current_track]}")
            elif event.key == pygame.K_s:  # 's' for stop
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()

    pygame.time.Clock().tick(30)

pygame.quit()