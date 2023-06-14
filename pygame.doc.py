# 基本的なPygameの「ゲームループ」
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720)) #ウィンドウのサイズを1280x720ピクセルで設定
clock = pygame.time.Clock() #ゲームループを制御するための clock オブジェクトを作成
running = True #running フラグを True に初期化(ループが継続し続けます。)

while running: #running フラグが True の間、ゲームループが実行されます。
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get(): #pygame.event.get() によって発生したイベントを取得し、ループ内で処理します。
        if event.type == pygame.QUIT:
            running = False #pygame.QUIT イベントが発生した場合、running フラグを False に設定してゲームループを終了

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple") #screen.fill() を使用して、ウィンドウの内容を毎フレームクリアします。このコードでは、ウィンドウの背景色を紫色（"purple"）で塗りつぶしています。

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip() #バックバッファに描画された内容がフロントバッファに反映され、画面に表示されます。

    clock.tick(60)  # limits FPS to 60

pygame.quit()