from runner_and_tournament import Runner, Tournament
import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test = runner.Runner('walk_test')
        for i in range(10):
            test.walk()
        self.assertEqual(test.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test = runner.Runner('run_test')
        for i in range(10):
            test.run()
        self.assertEqual(test.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_1 = runner.Runner('walk_test')
        test_2 = runner.Runner('run_test')
        for i in range(10):
            test_1.walk()
            test_2.run()
        self.assertNotEqual(test_1.distance,test_2.distance)
class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_Ysein = Runner("Усэйн",10)
        self.runner_Andrey = Runner("Андрей", 9)
        self.runner_Nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_running_1(self):
        running = Tournament(90, self.runner_Ysein,self.runner_Nik)
        result = running.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'ошибка')
        self.all_results['running_1'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_running_2(self):
        running = Tournament(90, self.runner_Andrey,self.runner_Nik)
        result = running.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник','ошибка')
        self.all_results['running_2'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_running_3(self):
        running = Tournament(90, self.runner_Ysein,self.runner_Andrey,self.runner_Nik)
        result = running.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник','ошибка')
        self.all_results['running_3'] = result

    if __name__ == '__main__':
        unittest.main()