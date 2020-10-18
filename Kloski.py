import sys
import pygame

from settings import Settings
from digital_blocks import DigitalBlocks
from button import Button
from game_stats import GameStats
from timepiece import Timepiece
from step_record import StepRecord
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    stats = GameStats(ai_settings)
    timepiece = Timepiece(ai_settings, screen, stats)
    step_record = StepRecord(ai_settings, screen, stats)

    blocks = DigitalBlocks(ai_settings, screen)
    pygame.display.set_caption("Kloski")
    
    fclock = pygame.time.Clock()
    play_button = Button(ai_settings, screen, "Play")
    reset_button = Button(ai_settings, screen, "Reset")
    reset_button.set_button_lower_right()
    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(stats, blocks, play_button, reset_button, timepiece, step_record)
        if stats.game_active:
            if(gf.check_win(blocks)):
                stats.game_active = False
                gf.check_min_time(stats, timepiece)

        gf.update_screen(ai_settings, screen, stats, blocks, play_button, reset_button, timepiece, step_record)
        fclock.tick(ai_settings.fps)

if __name__ == '__main__':
    run_game()

