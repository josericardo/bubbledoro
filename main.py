#!/usr/bin/env python

from pomodoro import Pomodoro
from sleeper import Sleeper
from bubbledoro import Bubbledoro
from commands import getstatusoutput
import datetime


class TerminalWriter:
    def wakeup(self, event):
        if event == 'before_work':
            print 'You should be working...'
        elif event == 'before_short_rest':
            print 'You should rest a little...'
        elif event == 'before_long_rest':
            print 'You should rest for a little longer now...'


class MPG321Notifier:
    def wakeup(self, event):
        sounds = {
            'before_work': 'lets_play',
            'before_short_rest': 'available',
            'before_long_rest': 'chewy'
        }

        sound = sounds.get(event, '')

        if sound:
            print("\a")
            getstatusoutput('mpg321 sounds/%s.wav' % sound)
            print datetime.datetime.now()


class PomodoroWatcher:
    def wakeup(self, event):
        print("%s has finished" % event)

pomodoro = Pomodoro(Sleeper(), 25, 5, 20)

pomodoro.add_observer(MPG321Notifier())
pomodoro.add_observer(TerminalWriter())

Bubbledoro(pomodoro).run()
