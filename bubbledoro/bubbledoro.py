#!/usr/bin/env python

from pomodoro import Pomodoro
from sleeper import Sleeper


class Bubbledoro:
    def __init__(self,  pomodoro=Pomodoro(Sleeper(), 0.03, 0.02, 0.05)):
        self.pomodoro = pomodoro

    def run(self):
        running = 'y'

        while running == 'y':
            self.run_one_cycle()
            running = self.should_keep_running()

    def run_one_cycle(self):
        i = 0

        while i < 3:
            self.pomodoro.work()
            self.pomodoro.short_rest()

            i += 1

        self.pomodoro.work()
        self.pomodoro.long_rest()

    def should_keep_running(self):
        back = ''

        while back != 'y' and back != 'n':
            if back != '':
                print('Valid options: y or n')

            back = raw_input('Back to work? [Y/n] ').strip().lower()

        return back
