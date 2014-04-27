import sleeper


class Pomodoro:
    def __init__(self, sleeper, work_in_min, short_rest_in_min, long_rest_in_min):

        self.sleeper = sleeper
        self.work_in_min = work_in_min
        self.short_rest_in_min = short_rest_in_min
        self.long_rest_in_min = long_rest_in_min
        self.observers = []

    @staticmethod
    def default():
        return Pomodoro(sleeper.Sleeper(), 25, 5, 30)

    def add_observer(self, observer):
        self.observers.append(observer)

    def work(self):
        self.sleep_and_notify(self.work_in_min, 'work')

    def short_rest(self):
        self.sleep_and_notify(self.short_rest_in_min, 'short_rest')

    def long_rest(self):
        self.sleep_and_notify(self.long_rest_in_min, 'long_rest')

    def sleep_and_notify(self, sleep_time, event):
        self.notify('before_' + event)
        user_input = self.sleeper.sleep(sleep_time)

        if not user_input:
            self.notify('after_' + event)
        elif user_input.lower() == 'i':
            self.sleep_and_notify(sleep_time, event)

    def notify(self, event):
        for o in self.observers:
            o.wakeup(event)
