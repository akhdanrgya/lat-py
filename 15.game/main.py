import pygame

# init
pygame.init()
# variable running game
isRun = True

#  membuat display surface object
window_l = 500
window_p = 500
window = pygame.display.set_mode((window_l, window_p))


#  object game
# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# Kecepatan gerak

speed = 0.3


while isRun:

    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("ANJAAAYY")
            isRun = False


    # ambil semua keyboard press / action
    keys = pygame.key.get_pressed()
    
    # ambil ke kiri
    if keys[pygame.K_a] and x > 0:
        x -= speed

    if keys[pygame.K_d] and x < window_l - lebar:
        x += speed

    if keys[pygame.K_s] and y < window_p - panjang:
        y += speed
        
    if keys[pygame.K_w] and y > 0:
        y -= speed
        
    # update asset
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 120, 0), (x, y, lebar, panjang))
    # render ke display
    pygame.display.update()


pygame.quit()
