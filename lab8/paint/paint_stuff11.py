import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Increased screen size
    clock = pygame.time.Clock()

    radius = 15
    mode = 'draw'  # 'draw', 'rect', 'circle', 'erase'
    color = (0, 0, 255)  # Default color blue
    points = []
    rect_start = None
    circle_start = None

    # Color palette
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'yellow': (255,255,0),
        'purple': (128,0,128)
    }

    # Color palette positions
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if mode == 'draw' or mode == 'erase':
                        points = [event.pos]
                    elif mode == 'rect':
                        rect_start = event.pos
                    elif mode == 'circle':
                        circle_start = event.pos

                    # Color selection
                    for color_name, pos in color_positions.items():
                        rect = pygame.Rect(pos[0], pos[1], 20, 20)
                        if rect.collidepoint(event.pos):
                            color = colors[color_name]

                elif event.button == 3:  # Right click
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    if mode == 'draw' or mode == 'erase':
                        points = points + [event.pos]
                        points = points[-256:]

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if mode == 'rect' and rect_start:
                        rect_end = event.pos
                        pygame.draw.rect(screen, color, pygame.Rect(rect_start, (rect_end[0] - rect_start[0], rect_end[1] - rect_start[1])))
                        rect_start = None
                    elif mode == 'circle' and circle_start:
                        circle_end = event.pos
                        radius_circle = int(((circle_end[0] - circle_start[0])**2 + (circle_end[1] - circle_start[1])**2)**0.5)
                        pygame.draw.circle(screen, color, circle_start, radius_circle)
                        circle_start = None

        screen.fill((255, 255, 255))  # White background

        # Draw points
        i = 0
        while i < len(points) - 1:
            if mode == 'erase':
                draw_color = (255, 255, 255)  # Erase with white
            else:
                draw_color = color
            drawLineBetween(screen, i, points[i], points[i + 1], radius, draw_color)
            i += 1

        # Draw color palette
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