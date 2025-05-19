import pygame
from ship import Ship
from bullet import Bullet
from enemy import Enemy
import game_functions as gf
from pygame.sprite import Group
import random
import sys

# Função para desenhar botões
def draw_button(screen, rect, text, font, color_bg, color_text):
    pygame.draw.rect(screen, color_bg, rect)
    text_img = font.render(text, True, color_text)
    text_rect = text_img.get_rect(center=rect.center)
    screen.blit(text_img, text_rect)

def criar_inimigo(screen, enemies):
    largura_tela = screen.get_width()
    x = random.randint(0, largura_tela - 60)
    enemy = Enemy(screen, x)
    enemies.add(enemy)

def menu(screen, font):
    menu_running = True
    while menu_running:
        screen.fill((30, 30, 30))

        titulo = font.render("INVASÃO ALIENS", True, (200, 200, 60))
        screen.blit(titulo, (screen.get_width() // 2 - titulo.get_width() // 2, 150))

        # Botões
        btn_jogar = pygame.Rect(screen.get_width()//2 - 100, 350, 200, 60)
        btn_sair = pygame.Rect(screen.get_width()//2 - 100, 450, 200, 60)
        draw_button(screen, btn_jogar, "JOGAR", font, (100, 200, 100), (0, 0, 0))
        draw_button(screen, btn_sair, "SAIR", font, (200, 100, 100), (0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if btn_jogar.collidepoint(mouse_pos):
                    menu_running = False
                if btn_sair.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

def game_over_screen(screen, font):
    over_running = True
    while over_running:
        screen.fill((30, 30, 30))
        texto = font.render("GAME OVER", True, (200, 30, 30))
        screen.blit(texto, (screen.get_width() // 2 - texto.get_width() // 2, 200))

        # Botão voltar ao menu
        btn_menu = pygame.Rect(screen.get_width()//2 - 100, 350, 200, 60)
        draw_button(screen, btn_menu, "VOLTAR AO MENU", font, (100, 200, 100), (0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if btn_menu.collidepoint(mouse_pos):
                    over_running = False

        pygame.display.flip()

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Invasão Aliens")
    font = pygame.font.SysFont(None, 48)

    while True:
        menu(screen, font)
        # Início do jogo
        ship = Ship(screen)
        bullets = Group()
        enemies = Group()
        kills = 0
        game_over = False
        inimigo_delay = 1000
        ultimo_inimigo = pygame.time.get_ticks()

        while not game_over:
            tempo_atual = pygame.time.get_ticks()
            gf.check_events(bullets, screen, ship)
            ship.update()
            bullets.update()
            enemies.update()

            # Lançar inimigos aos poucos
            if tempo_atual - ultimo_inimigo > inimigo_delay:
                criar_inimigo(screen, enemies)
                ultimo_inimigo = tempo_atual

            # Colisões
            collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
            if collisions:
                kills += 1

            # Chegada de inimigos no final ou nave
            for enemy in enemies:
                if enemy.rect.bottom >= screen.get_height() or enemy.rect.colliderect(ship.rect):
                    game_over = True

            gf.update_screen(screen, ship, bullets, enemies)
            kills_text = font.render(f"Kills: {kills}", True, (30, 30, 30))
            screen.blit(kills_text, (20, 20))
            pygame.display.flip()

        # Tela de game over e voltar ao menu
        game_over_screen(screen, font)

run_game()