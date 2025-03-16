import pygame
import os
import time
import math


pygame.init()


WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mic Clock")


background = pygame.image.load("clock_face.jpg").convert_alpha()
right_hand = pygame.image.load("mic_hand_right.png").convert_alpha()  
left_hand = pygame.image.load("mic_hand_left.png").convert_alpha()  


background = pygame.transform.scale(background, (WIDTH, HEIGHT))


right_hand_rect = right_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
left_hand_rect = left_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))


right_hand_pivot = (right_hand_rect.width // 2, right_hand_rect.height - 20) 
left_hand_pivot = (left_hand_rect.width // 2, left_hand_rect.height - 20)

def rotate_hand(image, rect, angle, pivot):
    """Rotate an image around a pivot point."""
    rotated_image = pygame.transform.rotate(image, -angle)  
    rotated_rect = rotated_image.get_rect(center=rect.center)

    offset_x = pivot[0] - rect.width // 2
    offset_y = pivot[1] - rect.height // 2

    rotated_rect.center = (rect.centerx + offset_x * math.cos(math.radians(angle)) - offset_y * math.sin(math.radians(angle)),
                           rect.centery + offset_x * math.sin(math.radians(angle)) + offset_y * math.cos(math.radians(angle)))

    return rotated_image, rotated_rect

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    minutes_angle = (minutes / 60) * 360
    seconds_angle = (seconds / 60) * 360
    
    rotated_right_hand, rotated_right_hand_rect = rotate_hand(right_hand, right_hand_rect, minutes_angle, right_hand_pivot)
    rotated_left_hand, rotated_left_hand_rect = rotate_hand(left_hand, left_hand_rect, seconds_angle, left_hand_pivot)
    
    screen.blit(background, (0, 0))
    
    screen.blit(rotated_right_hand, rotated_right_hand_rect)
    screen.blit(rotated_left_hand, rotated_left_hand_rect)
    
    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()