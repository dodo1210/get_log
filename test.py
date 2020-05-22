# coding:utf-8
import unittest
from get_log import Task1, Task2, Bonus
import web

class Test(unittest.TestCase):
    def test_task1_equal(self):
        t = Task1()
        f = open('qgames.log',"r")
        json = t.task1(f)   
        self.assertEqual(json,json)

    def test_task1_not_equal(self):
        t = Task1()
        f = open('qgames.log',"r")
        json = t.task1(f)
        self.assertNotEqual(None,json)
    
    def teste_endGame_equal(self):
        phrase = '20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT'
        t = Task1()
        f = open('qgames.log',"r")
        json = t.endGame(['Isgalamido'],0,t.eachN_kill(phrase),t.eachN_kill(phrase),0)
        json2 = t.endGame(['Isgalamido'],0,t.eachN_kill(phrase),t.eachN_kill(phrase),0)
        self.assertEqual(json,json)

    def teste_endGame_not_equal(self):
        phrase = '20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT'
        t = Task1()
        f = open('qgames.log',"r")
        json = t.endGame(['Isgalamido'],0,t.eachN_kill(phrase),t.eachN_kill(phrase),0)
        json2 = t.endGame(['<world>'],0,t.eachN_kill(phrase),t.eachN_kill(phrase),0)
        self.assertNotEqual(json,json2)

    def teste_eachN_kill_equal(self):
        t = Task1()
        f = open('qgames.log',"r")
        name = t.eachN_kill('20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT')
        name2 = t.eachN_kill('20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT')
        self.assertEqual(name,name2)

    def teste_each_not_N_kill_equal(self):
        t = Task1()
        f = open('qgames.log',"r")
        name = t.eachN_kill('20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT')
        name2 = t.eachN_kill('20:54 Kill: 1022 2 22: <world2> killed Isgalamido by MOD_TRIGGER_HURT')
        self.assertNotEqual(name,name2)

    def teste_eachN_killed_equal(self):
        t = Task1()
        f = open('qgames.log',"r")
        name = t.eachN_killed('20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT')
        name2 = t.eachN_killed('20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT')
        self.assertEqual(name,name2)

    def teste_each_not_N_killed_equal(self):
        t = Task1()
        f = open('qgames.log',"r")
        name = t.eachN_killed('20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT')
        name2 = t.eachN_killed('20:54 Kill: 1022 2 22: <world> killed Isgalamido2 by MOD_TRIGGER_HURT')
        self.assertNotEqual(name,name2)

    def teste_task2_is_none(self):
        t = Task1()
        f = open('qgames.log',"r")
        json = t.task1(f)
        t2 = Task2.task2(self,json)
        self.assertIsNone(t2)

    def test_bonus_equal(self):
        b = Bonus()
        f = open('qgames.log',"r")
        json = b.bonus(f)   
        self.assertEqual(json,json)

    def test_bonus_not_equal(self):
        b = Bonus()
        f = open('qgames.log',"r")
        json = b.bonus(f)
        self.assertNotEqual(None,json)

    def test_web__game_equal(self):
        json = web.game()
        json2 = web.game()
        self.assertEqual(json,json2)

    def test_web__game_not_equal(self):
        json = web.game()
        self.assertNotEqual(json,None)

    def test_web_search_game_equal(self):
        json = web.search_game(2)
        json2 = web.search_game(2)
        self.assertEqual(json,json2)

    def test_web_search_game_not_equal(self):
        json = web.search_game(2)
        json2 = web.search_game(1)
        self.assertNotEqual(json,json2)


if __name__ == "__main__":
    unittest.main()