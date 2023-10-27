from ..components.position import PositionComponent

class CollisionSystem:
    def check_collision(self, snake, food):
        snake_pos = snake.components[PositionComponent]
        food_pos = food.components[PositionComponent]