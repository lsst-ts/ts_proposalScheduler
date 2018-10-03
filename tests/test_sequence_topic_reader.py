import collections
import unittest
try:
    from unittest import mock
except ImportError:
    import mock

from lsst.ts.scheduler import Main
import SALPY_scheduler


def define_seqprop():
    seqprop = SALPY_scheduler.scheduler_sequencePropConfigC()
    seqprop.name = "SequenceProposal1"
    seqprop.propId = 1
    seqprop.twilightBoundary = -18.0
    seqprop.deltaLst = 60.0
    seqprop.decWindow = 90.0
    seqprop.maxAirmass = 1.5
    seqprop.maxCloud = 0.7
    seqprop.minDistanceMoon = 30.0
    seqprop.excludePlanets = True
    seqprop.numUserRegions = 4
    seqprop.userRegionIds[0] = 1
    seqprop.userRegionIds[1] = 20
    seqprop.userRegionIds[2] = 350
    seqprop.userRegionIds[3] = 4015
    seqprop.numSubSequences = 1
    seqprop.subSequenceNames = "test1"
    seqprop.numSubSequenceFilters[0] = 5
    seqprop.subSequenceFilters = "g,r,i,z,y"
    seqprop.numSubSequenceFilterVisits[0] = 20
    seqprop.numSubSequenceFilterVisits[1] = 25
    seqprop.numSubSequenceFilterVisits[2] = 30
    seqprop.numSubSequenceFilterVisits[3] = 20
    seqprop.numSubSequenceFilterVisits[4] = 27
    seqprop.numSubSequenceEvents[0] = 30
    seqprop.numSubSequenceMaxMissed[0] = 2
    seqprop.subSequenceTimeIntervals[0] = 5 * 24 * 3600
    seqprop.subSequenceTimeWindowStarts[0] = 0.0
    seqprop.subSequenceTimeWindowMaximums[0] = 1.0
    seqprop.subSequenceTimeWindowEnds[0] = 2.0
    seqprop.subSequenceTimeWeights[0] = 1.0
    seqprop.numMasterSubSequences = 2
    seqprop.masterSubSequenceNames = "master1,master2"
    seqprop.numNestedSubSequences[0] = 2
    seqprop.numNestedSubSequences[1] = 1
    seqprop.nestedSubSequenceNames = "nested1,nested2,nested3"
    seqprop.numMasterSubSequenceEvents[0] = 20
    seqprop.numMasterSubSequenceEvents[1] = 15
    seqprop.numMasterSubSequenceMaxMissed[0] = 1
    seqprop.numMasterSubSequenceMaxMissed[1] = 3
    seqprop.masterSubSequenceTimeIntervals[0] = 648000
    seqprop.masterSubSequenceTimeIntervals[1] = 518400
    seqprop.masterSubSequenceTimeWindowStarts[0] = 0.0
    seqprop.masterSubSequenceTimeWindowStarts[1] = 0.0
    seqprop.masterSubSequenceTimeWindowMaximums[0] = 1.0
    seqprop.masterSubSequenceTimeWindowMaximums[1] = 1.0
    seqprop.masterSubSequenceTimeWindowEnds[0] = 2.0
    seqprop.masterSubSequenceTimeWindowEnds[1] = 2.0
    seqprop.masterSubSequenceTimeWeights[0] = 1.0
    seqprop.masterSubSequenceTimeWeights[1] = 1.0
    seqprop.numNestedSubSequenceFilters[0] = 3
    seqprop.numNestedSubSequenceFilters[1] = 2
    seqprop.numNestedSubSequenceFilters[2] = 2
    seqprop.nestedSubSequenceFilters = "r,g,i,z,y,u,y"
    seqprop.numNestedSubSequenceFilterVisits[0] = 10
    seqprop.numNestedSubSequenceFilterVisits[1] = 10
    seqprop.numNestedSubSequenceFilterVisits[2] = 20
    seqprop.numNestedSubSequenceFilterVisits[3] = 3
    seqprop.numNestedSubSequenceFilterVisits[4] = 3
    seqprop.numNestedSubSequenceFilterVisits[5] = 5
    seqprop.numNestedSubSequenceFilterVisits[6] = 5
    seqprop.numNestedSubSequenceEvents[0] = 20
    seqprop.numNestedSubSequenceEvents[1] = 10
    seqprop.numNestedSubSequenceEvents[2] = 15
    seqprop.numNestedSubSequenceMaxMissed[0] = 1
    seqprop.numNestedSubSequenceMaxMissed[1] = 1
    seqprop.numNestedSubSequenceMaxMissed[2] = 5
    seqprop.nestedSubSequenceTimeIntervals[0] = 7200
    seqprop.nestedSubSequenceTimeIntervals[1] = 3600
    seqprop.nestedSubSequenceTimeIntervals[2] = 900
    seqprop.nestedSubSequenceTimeWindowStarts[0] = 0.0
    seqprop.nestedSubSequenceTimeWindowStarts[1] = 0.0
    seqprop.nestedSubSequenceTimeWindowStarts[2] = 0.0
    seqprop.nestedSubSequenceTimeWindowMaximums[0] = 1.0
    seqprop.nestedSubSequenceTimeWindowMaximums[1] = 1.0
    seqprop.nestedSubSequenceTimeWindowMaximums[2] = 1.0
    seqprop.nestedSubSequenceTimeWindowEnds[0] = 2.0
    seqprop.nestedSubSequenceTimeWindowEnds[1] = 2.0
    seqprop.nestedSubSequenceTimeWindowEnds[2] = 2.0
    seqprop.nestedSubSequenceTimeWeights[0] = 1.0
    seqprop.nestedSubSequenceTimeWeights[1] = 1.0
    seqprop.nestedSubSequenceTimeWeights[2] = 1.0
    seqprop.numFilters = 6
    seqprop.filterNames = "u,g,r,i,z,y"
    seqprop.brightLimit[0] = 21.0
    seqprop.brightLimit[1] = 21.0
    seqprop.brightLimit[2] = 21.0
    seqprop.brightLimit[3] = 21.0
    seqprop.brightLimit[4] = 21.0
    seqprop.brightLimit[5] = 21.0
    seqprop.darkLimit[0] = 30.0
    seqprop.darkLimit[1] = 30.0
    seqprop.darkLimit[2] = 30.0
    seqprop.darkLimit[3] = 30.0
    seqprop.darkLimit[4] = 30.0
    seqprop.darkLimit[5] = 30.0
    seqprop.maxSeeing[0] = 2.0
    seqprop.maxSeeing[1] = 2.0
    seqprop.maxSeeing[2] = 2.0
    seqprop.maxSeeing[3] = 2.0
    seqprop.maxSeeing[4] = 2.0
    seqprop.maxSeeing[5] = 2.0
    seqprop.numFilterExposures[0] = 2
    seqprop.numFilterExposures[1] = 2
    seqprop.numFilterExposures[2] = 2
    seqprop.numFilterExposures[3] = 2
    seqprop.numFilterExposures[4] = 2
    seqprop.numFilterExposures[5] = 2
    seqprop.exposures[0] = 15
    seqprop.exposures[1] = 15
    seqprop.exposures[2] = 15
    seqprop.exposures[3] = 15
    seqprop.exposures[4] = 15
    seqprop.exposures[5] = 15
    seqprop.exposures[6] = 15
    seqprop.exposures[7] = 15
    seqprop.exposures[8] = 15
    seqprop.exposures[9] = 15
    seqprop.exposures[10] = 15
    seqprop.exposures[11] = 15
    seqprop.maxNumTargets = 100
    seqprop.acceptSerendipity = false
    seqprop.acceptConsecutiveVisits = true
    seqprop.restartLostSequences = true
    seqprop.restartCompleteSequences = false
    seqprop.maxVisitsGoal = 250000
    seqprop.airmassBonus = 0.5
    seqprop.hourAngleBonus = 0.5
    seqprop.hourAngleMax = 5.0
    return seqprop



skip_msg = 'Skipping this unit test because of errors: '
skip_msg += 'telemetry and events may be mixed up .. '
skip_msg += 'but definitely numNestedSubSequences needs to be clarified - int or string?'
@unittest.skip(skip_msg)
class TestSequencePropTopicReader(unittest.TestCase):

    def setUp(self):
        seqprop = define_seqprop()
        
        patcher1 = mock.patch("lsst.ts.scheduler.main.Driver")
        self.addCleanup(patcher1.stop)
        self.mock_driver = patcher1.start()

        options = collections.namedtuple("options", ["timeout"])
        options.timeout = 60.0

        self.main = Main(options)

    def check_filter(self, cdict, name, *truths):
        band_filter = "filter_{}".format(name)
        self.assertTrue(band_filter in cdict)
        self.assertEqual(cdict[band_filter]["min_brig"], truths[0])
        self.assertEqual(cdict[band_filter]["max_brig"], truths[1])
        self.assertEqual(cdict[band_filter]["max_seeing"], truths[2])
        self.assertListEqual(cdict[band_filter]["exp_times"], truths[3])

    def check_subsequence(self, cdict, name, is_master, *truths):
        offset = 1
        if is_master:
            offset = 0
        self.assertTrue(name in cdict)
        if not is_master:
            self.assertListEqual(cdict[name]["filters"], truths[0])
            self.assertListEqual(cdict[name]["visits_per_filter"], truths[1])
        else:
            self.assertListEqual(cdict[name]["nested_names"], truths[0])
        self.assertEqual(cdict[name]["num_events"], truths[1 + offset])
        self.assertEqual(cdict[name]["num_max_missed"], truths[2 + offset])
        self.assertEqual(cdict[name]["time_interval"], truths[3 + offset])
        self.assertEqual(cdict[name]["time_window_start"], truths[4 + offset])
        self.assertEqual(cdict[name]["time_window_max"], truths[5 + offset])
        self.assertEqual(cdict[name]["time_window_end"], truths[6 + offset])
        self.assertEqual(cdict[name]["time_weight"], truths[7 + offset])

    def test_reader(self):
        confdict = self.main.sal.rtopic_seq_prop_config(seqprop)
        self.assertEquals(confdict["sky_nightly_bounds"]["twilight_boundary"], -18.0)
        self.assertEquals(confdict["sky_nightly_bounds"]["delta_lst"], 60.0)
        self.assertEquals(confdict["constraints"]["max_cloud"], 0.7)
        self.assertEquals(confdict["constraints"]["max_airmass"], 1.5)
        self.assertEquals(confdict["constraints"]["min_distance_moon"], 30.0)
        self.assertTrue(confdict["constraints"]["exclude_planets"])
        self.assertListEqual(confdict["sky_region"]["user_regions"], [1, 20, 350, 4015])
        self.assertEqual(confdict["sky_exclusions"]["dec_window"], 90.0)
        self.assertListEqual(confdict["subsequences"]["names"], ["test1"])
        self.check_subsequence(confdict, "subseq_test1", False,
                               ["g", "r", "i", "z", "y"], [20, 25, 30, 20, 27],
                               30, 2, 432000, 0.0, 1.0, 2.0, 1.0)
        self.assertListEqual(confdict["master_subsequences"]["names"], ["master1", "master2"])
        self.assertListEqual(confdict["master_subsequences"]["num_nested"], [2, 1])
        self.check_subsequence(confdict, "msubseq_master1", True, ["nested1", "nested2"],
                               20, 1, 648000, 0.0, 1.0, 2.0, 1.0)
        self.check_subsequence(confdict, "msubseq_master2", True, ["nested3"],
                               15, 3, 518400, 0.0, 1.0, 2.0, 1.0)
        self.check_subsequence(confdict, "nsubseq_nested1", False,
                               ["r", "g", "i"], [10, 10, 20],
                               20, 1, 7200, 0.0, 1.0, 2.0, 1.0)
        self.check_subsequence(confdict, "nsubseq_nested2", False,
                               ["z", "y"], [3, 3],
                               10, 1, 3600, 0.0, 1.0, 2.0, 1.0)
        self.check_subsequence(confdict, "nsubseq_nested3", False,
                               ["u", "y"], [5, 5],
                               15, 5, 900, 0.0, 1.0, 2.0, 1.0)
        band_filters = "u,g,r,i,z,y"
        for band_filter in band_filters.split(','):
            self.check_filter(confdict, band_filter, 21.0, 30.0, 2.0, [15, 15])
        self.assertEquals(confdict["scheduling"]["max_num_targets"], 100)
        self.assertFalse(confdict["scheduling"]["accept_serendipity"])
        self.assertTrue(confdict["scheduling"]["accept_consecutive_visits"])
        self.assertTrue(confdict["scheduling"]["restart_lost_sequences"])
        self.assertFalse(confdict["scheduling"]["restart_complete_sequences"])
        self.assertEqual(confdict["scheduling"]["max_visits_goal"], 250000)
        self.assertEquals(confdict["scheduling"]["airmass_bonus"], 0.5)
        self.assertEquals(confdict["scheduling"]["hour_angle_bonus"], 0.5)
        self.assertEquals(confdict["scheduling"]["hour_angle_max"], 5.0)
