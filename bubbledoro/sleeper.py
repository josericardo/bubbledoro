import time
from commands import getstatusoutput


class Sleeper:
    def sleep(self, time_in_min):
        sleep_secs = time_in_min*60
        cmd = 'read -t %d -n 1 BUBBLEDOROTMP; echo $BUBBLEDOROTMP' % sleep_secs
        cmd_result = getstatusoutput(cmd)
        return cmd_result[1]
