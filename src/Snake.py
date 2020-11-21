import pygame

pygame.init()




class Snake:

    def __init__(self,dis_width,dis_height):
        self.dis_width=dis_width
        self.dis_height=dis_height
        self.x1 = dis_width / 2
        self.y1 = dis_height / 2
        self.snake_List = []
        self.snake_block = 10
        self.Length_of_snake=1





    def _move_(self,dis):
        pygame.init()
        black = (0, 0, 0)
        clock = pygame.time.Clock()
        x1_change = 0
        y1_change = 0
        snake_speed = 15
        game_over = False
        while not game_over:
            dis.fill(black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -self.snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = self.snake_block
                        x1_change = 0

            if self.x1 >= self.dis_width or self.x1 < 0 or self.y1 >= self.dis_height or self.y1 < 0:
                game_over = True

            self.x1 += x1_change
            self.y1 += y1_change
            snake_Head = []
            snake_Head.append(self.x1)
            snake_Head.append(self.y1)
            self.snake_List.append(snake_Head)

            if len(self.snake_List) > self.Length_of_snake:
                del self.snake_List[0]


            for x in self.snake_List[:-1]:
                if x == snake_Head:
                    game_over = True


            red = (213, 50, 80)
            for x in self.snake_List:
                pygame.draw.rect(dis, red, [x[0], x[1], self.snake_block, self.snake_block])

            pygame.display.update()

            clock.tick(snake_speed)

        pygame.quit()
        quit()

width=600
heigth=400
s=Snake(width,heigth)
dis = pygame.display.set_mode((width,heigth))
s._move_(dis)


