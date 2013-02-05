class Pomodoro:

  def __init__(self, sleeper, 
                     work_in_min, 
                     short_rest_in_min, 
                     long_rest_in_min):

    self.sleeper = sleeper
    self.work_in_min = work_in_min
    self.short_rest_in_min = short_rest_in_min
    self.long_rest_in_min = long_rest_in_min
    self.observers = []

  def add_observer(self, observer):
    self.observers.append(observer)

  def work(self):
    self.sleep_and_notify(self.work_in_min)

  def short_rest(self):
    self.sleep_and_notify(self.short_rest_in_min)

  def long_rest(self):
    self.sleep_and_notify(self.long_rest_in_min)
  
  def sleep_and_notify(self, sleep_time):
    self.sleeper.sleep(sleep_time)

    for o in self.observers:
      o.wakeup()
