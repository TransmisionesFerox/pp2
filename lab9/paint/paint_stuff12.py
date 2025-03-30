import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'draw'  # 'draw', 'rect', 'circle', 'erase', 'square', 'triangle_right', 'triangle_equilateral', 'rhombus'
    color = (0, 0, 255)
    points = []
    shape_start = None  # Generic start point for shapes

    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'yellow': (255, 255, 0),
        'purple': (128, 0, 128)
    }

    color_positions = {
        'red': (650, 10),
        'green': (650, 40),
        'blue': (650, 70),
        'black': (700, 10),
        'white': (700, 40),
        'yellow': (700, 70),
        'purple': (750, 10)
    }

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_d:
                    mode = 'draw'
                elif event.key == pygame.K_r:
                    mode = 'rect'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_e:
                    mode = 'erase'
                elif event.key == pygame.K_s:
                    mode = 'square'
                elif event.key == pygame.K_t:
                    mode = 'triangle_right'
                elif event.key == pygame.K_y:
                    mode = 'triangle_equilateral'
                elif event.key == pygame.K_h:
                    mode = 'rhombus'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mode == 'draw' or mode == 'erase':
                        points = [event.pos]
                    else:
                        shape_start = event.pos

                    for color_name, pos in color_positions.items():
                        rect = pygame.Rect(pos[0], pos[1], 20, 20)
                        if rect.collidepoint(event.pos):
                            color = colors[color_name]

                elif event.button == 3:
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    if mode == 'draw' or mode == 'erase':
                        points = points + [event.pos]
                        points = points[-256:]

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if shape_start:
                        shape_end = event.pos
                        if mode == 'rect':
                            pygame.draw.rect(screen, color, pygame.Rect(shape_start, (shape_end[0] - shape_start[0], shape_end[1] - shape_start[1])))
                        elif mode == 'circle':
                            radius_circle = int(((shape_end[0] - shape_start[0])**2 + (shape_end[1] - shape_start[1])**2)**0.5)
                            pygame.draw.circle(screen, color, shape_start, radius_circle)
                        elif mode == 'square':
                            side = min(abs(shape_end[0] - shape_start[0]), abs(shape_end[1] - shape_start[1]))
                            pygame.draw.rect(screen, color, pygame.Rect(shape_start, (side, side)))
                        elif mode == 'triangle_right':
                            pygame.draw.polygon(screen, color, [shape_start, shape_end, (shape_start[0], shape_end[1])])
                        elif mode == 'triangle_equilateral':
                            side = int(math.sqrt((shape_end[0] - shape_start[0])**2 + (shape_end[1] - shape_start[1])**2))
                            height = int(side * math.sqrt(3) / 2)
                            pygame.draw.polygon(screen, color, [shape_start, (shape_start[0] + side, shape_start[1]), (shape_start[0] + side / 2, shape_start[1] - height)])
                        elif mode == 'rhombus':
                            dx = shape_end[0] - shape_start[0]
                            dy = shape_end[1] - shape_start[1]
                            pygame.draw.polygon(screen, color, [shape_start, (shape_start[0] + dx, shape_start[1] + dy / 2), shape_end, (shape_start[0] + dx, shape_start[1] - dy / 2)])
                        shape_start = None

        screen.fill((255, 255, 255))

        i = 0
        while i < len(points) - 1:
            if mode == 'erase':
                draw_color = (255, 255, 255)
            else:
                draw_color = color
            drawLineBetween(screen, i, points[i], points[i + 1], radius, draw_color)
            i += 1

        for color_name, pos in color_positions.items():
            pygame.draw.rect(screen, colors[color_name], pygame.Rect(pos[0], pos[1], 20, 20))

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()