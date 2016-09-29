import math

from ts_scheduler.schedulerTarget import Target
from ts_scheduler.proposal import Proposal

class ScriptedProposal(Proposal):
    def __init__(self, propid, name, confdict, scriptfile, skymodel):

        super(ScriptedProposal, self).__init__(propid, name, confdict, skymodel)

        self.script_file = scriptfile
        self.read_script()

        self.targetid = 0

    def read_script(self):

        scriptfilepath = self.script_file
        lines = file(scriptfilepath).readlines()
        targetid = 0
        self.targetsList = []
        for line in lines:
            line = line.strip()
            if not line:			# skip blank line
                continue
            if line[0] == '#': 		# skip comment line
                continue
            targetid += 1
            values = line.split()
            target = Target()
            target.fieldid = eval(values[0])
            target.filter = values[1]
            target.ra_rad = math.radians(eval(values[2]))
            target.dec_rad = math.radians(eval(values[3]))
            target.ang_rad = math.radians(eval(values[4]))
            target.num_exp = eval(values[5])
            target.exp_times = [int(x) for x in values[6].split(',')]

            self.targetsList.append(target)
        self.log.info("%d targets" % len(self.targetsList))

    def suggest_targets(self, time):

        super(ScriptedProposal, self).suggest_targets(time)

        if self.targetid < len(self.targetsList):
            nexttarget = self.targetsList[self.targetid]
        else:
            nexttarget = self.targetsList[-1]
        nexttarget.targetid = self.targetid
        nexttarget.time = time
        nexttarget.value = 1.0

        target_list = list([nexttarget])

        ra_list = []
        dec_list = []
        filter_list = []
        for target in target_list:
            ra_list.append(target.ra_rad)
            dec_list.append(target.dec_rad)
            filter_list.append(target.filter)
        sky_mags = self.sky.get_sky_brightness_timeblock(time, 1, 1, ra_list, dec_list)

        target_list[0].sky_brightness = sky_mags[0][target.filter][0]

        self.targetid += 1

        return target_list

    def register_observation(self, observation):
        pass
