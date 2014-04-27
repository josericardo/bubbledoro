import unittest
from bubbledoro.pomodoro import Pomodoro
from dingus import Dingus

WORK_INTERVAL = 25
SHORT_REST = 5
LONG_REST = 30

def new_pomodoro(sleeper):
    return Pomodoro(sleeper, WORK_INTERVAL, SHORT_REST, LONG_REST)

class TestPomodoro(unittest.TestCase):
  def setUp(self):
    self.sleeper = Dingus()

  def test_pomodoro_notifies_observers_after_working(self):
    observer = Dingus()
    pomodoro = new_pomodoro(self.sleeper)
    pomodoro.add_observer(observer)
    pomodoro.work()

    self.assertTrue(observer.wakeup.calls().once)

  def test_pomodoro_makes_me_work(self):
    pomodoro = new_pomodoro(self.sleeper)
    pomodoro.work()
    self.slept_for(WORK_INTERVAL)

  def test_pomodoro_makes_me_rest_a_little(self):
    pomodoro = new_pomodoro(self.sleeper)
    pomodoro.short_rest()
    self.slept_for(SHORT_REST)

  def test_pomodoro_makes_me_rest_longer(self):
    pomodoro = new_pomodoro(self.sleeper)
    pomodoro.long_rest()
    self.slept_for(LONG_REST)

  def slept_for(self, interval):
    self.assertTrue(self.sleeper.sleep.calls().once)
    self.assertEqual((interval,), self.sleep_first_param())

  def sleep_first_param(self):
    return self.sleeper.sleep.calls()[0][1]
