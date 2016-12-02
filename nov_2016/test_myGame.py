from unittest import TestCase


class TestMyApplication(TestCase):
    def test_on_draw(self):
        from .game_demo import MyApplication
        game = MyApplication(200, 100, 'Demo')
        game.on_draw()
        self.assertEqual(game.is_stopped, True)
        game.close()

    def test_on_draw_stopped(self):
        from .game_demo import MyApplication
        game = MyApplication(200, 100, 'Demo')
        game.is_stopped = False
        game.on_draw()
        self.assertEqual(game.is_stopped, True)
        game.close()
