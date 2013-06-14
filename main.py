#!/usr/bin/env python

from pomodoro import Pomodoro
from sleeper import Sleeper
from bubbledoro import Bubbledoro


class TerminalWriter:
    def wakeup(self, event):
        if event == 'before_work':
            print 'You should be working...'
        elif event == 'before_short_rest':
            print 'You should rest a little...'
        elif event == 'before_long_rest':
            print 'You should rest for a little longer now...'


class Beeper:
    def wakeup(self, event):
        if event.startswith('after'):
            print("\a")


class PomodoroWatcher:
    def wakeup(self, event):
        print("%s has finished" % event)

pomodoro = Pomodoro(Sleeper(), 25, 5, 20)
pomodoro.add_observer(Beeper())
pomodoro.add_observer(TerminalWriter())

Bubbledoro(pomodoro).run()
