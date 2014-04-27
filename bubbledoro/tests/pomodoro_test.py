import unittest
from bubbledoro.pomodoro import Pomodoro
from dingus import Dingus

WORK_INTERVAL = 25
SHORT_REST = 5
LONG_REST = 30

def new_pomodoro(sleeper):
    return Pomodoro(sleeper, WORK_INTERVAL, SHORT_REST, LONG_REST)


class FakeSleeper:
    def __init__(self): self.calls = 0

    def sleep(self, time):
        self.calls += 1
        return '' if self.calls > 1 else 'i'


class FakeObserver:

    def __init__(self):
        self.received_events = []

    def wakeup(self, event):
        self.received_events.append(event)

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

  def test_pomodoro_can_be_restarted(self):
    observer = FakeObserver()
    pomodoro = new_pomodoro(FakeSleeper())
    pomodoro.add_observer(observer)
    pomodoro.work()

    before_work_events = [e for e in observer.received_events if e == 'before_work']
    msg = "Two before_work events were expected, because the pomodoro was interrupted"
    self.assertEqual(2, len(before_work_events), msg)

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
