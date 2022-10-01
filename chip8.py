import pygame

from monitor import Monitor 
from keyboard import Keyboard
from cpu import CPU


pygame.display.set_caption("Chip8")

FPS = 60

def init():
    monitor = Monitor(20)
    keyboard = Keyboard()
    cpu = CPU(monitor, keyboard)
    cpu.load_sprites_into_memory()
    cpu.load_rom("./roms/IBMLogo.ch8")

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        cpu.cycle()

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT: 
                    run = False
                case pygame.KEYDOWN:
                    keyboard.key_down(event.key)
                case pygame.KEYUP:
                    keyboard.key_up(event.key)
        

    
    pygame.quit()
  

def main(): 
    init()

if __name__ == "__main__": main()