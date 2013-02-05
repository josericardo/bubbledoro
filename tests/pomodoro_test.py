import unittest
from pomodoro import Pomodoro
from dingus import Dingus

WORK_INTERVAL = 25
SHORT_REST = 5
LONG_REST = 30

class TestPomodoro(unittest.TestCase):
  def setUp(self):
    self.sleeper = Dingus()
    self.pomodoro = Pomodoro(self.sleeper, 
                             WORK_INTERVAL, 
                             SHORT_REST, 
                             LONG_REST)

  def test_pomodoro_notifies_observers_after_working(self):
    observer = PomodoroObserver()
    self.pomodoro.add_observer(observer)
    self.pomodoro.work()

    self.assertTrue(observer.notified)

  def test_pomodoro_makes_me_work(self):
    self.pomodoro.work()
    self.slept_for(WORK_INTERVAL)

  def test_pomodoro_makes_me_rest_a_little(self):
    self.pomodoro.short_rest()
    self.slept_for(SHORT_REST)

  def test_pomodoro_makes_me_rest_longer(self):
    self.pomodoro.long_rest()
    self.slept_for(LONG_REST)

  def slept_for(self, interval):
    self.assertTrue(self.sleeper.sleep.calls().once)
    self.assertEqual((interval,), self.sleep_first_param())

  def sleep_first_param(self):
    return self.sleeper.sleep.calls()[0][1]

class PomodoroObserver:
  def __init__(self):
    self.notified = False

  def wakeup(self):
    self.notified = True

  def notified(self):
    return self.notified
