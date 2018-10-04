from builtins import str
import os
import logging
import unittest

from lsst.utils import getPackageDir
from lsst.ts.astrosky.model import AstronomicalSkyModel
from lsst.ts.dateloc import ObservatoryLocation
from lsst.ts.scheduler.kernel import read_conf_file, conf_file_path
from lsst.ts.proposalScheduler.proposals import AreaDistributionProposal


class TestAreaDistributionProposal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        location = ObservatoryLocation()
        location.for_lsst()
        cls.skyModel = AstronomicalSkyModel(location)
        # For tests which require sky brightness.
        cls.start_stamp = 1664582400

    def setUp(self):
        logging.getLogger().setLevel(logging.WARN)
        configfilepath = os.path.join(getPackageDir('ts_proposalScheduler'), 'tests', 
                                      'conf', 'survey', 'areaProp1.conf')
        (path, name_ext) = os.path.split(configfilepath)
        (name, ext) = os.path.splitext(name_ext)
        proposal_confdict = read_conf_file(configfilepath)
        self.areaprop = AreaDistributionProposal(1, name, proposal_confdict, self.skyModel)

    def test_init(self):
        self.assertEqual(self.areaprop.name, "areaProp1")
        self.assertEqual(str(self.areaprop.params.filter_list),
                         "['u', 'g', 'r', 'i', 'z', 'y']")
        # Dictionaries do not preserve their order. This is a bad test.
        #self.assertEqual(str(self.areaprop.params.filter_goal_dict),
        #                 "{'g': 10.0, 'i': 25.0, 'r': 25.0, 'u': 7.0, 'y': 20.0, 'z': 20.0}")
        #self.assertEqual(str(self.areaprop.params.filter_min_brig_dict),
        #                 "{'g': 21.0, 'i': 20.25, 'r': 20.5, 'u': 21.0, 'y': 17.5, 'z': 17.5}")
        #self.assertEqual(str(self.areaprop.params.filter_max_brig_dict),
        #                 "{'g': 30.0, 'i': 30.0, 'r': 30.0, 'u': 30.0, 'y': 21.0, 'z': 21.0}")
        #self.assertEqual(str(self.areaprop.params.filter_max_seeing_dict),
        #                 "{'g': 1.5, 'i': 0.8, 'r': 0.9, 'u': 1.5, 'y': 1.0, 'z': 1.3}")
        #self.assertEqual(str(self.areaprop.params.filter_exp_times_dict),
        #                 "{'g': [15.0, 15.0], 'i': [15.0, 15.0], 'r': [15.0, 15.0], "
        #                 "'u': [25.0, 25.0], 'y': [15.0, 15.0], 'z': [15.0, 15.0]}")
        self.assertEqual(self.areaprop.params.max_airmass, 2.5)
        self.assertAlmostEqual(self.areaprop.params.min_alt, 23.578, delta=1e-3)

    def test_build_fields_tonight_list(self):
        # This test doesn't need skybrightness.
        # Can just start at 'original' 2022-01-01
        lsst_start_timestamp =  1640995200.0
        night = 1

        self.areaprop.build_tonight_fields_list(lsst_start_timestamp, night)
        field_list = self.areaprop.tonight_fields_list
        fieldid_list = []
        for field in field_list:
            fieldid_list.append(field.fieldid)
        self.assertEqual(len(fieldid_list), 10)
        self.assertEqual(str(fieldid_list), "[1764, 1873, 2006, 2108, 2234, 2346, 2464, 2572, 2692, 2802]")

        lsst_six_months = lsst_start_timestamp + 182 * 24 * 3600
        night = 181

        self.areaprop.build_tonight_fields_list(lsst_six_months, night)
        field_list = self.areaprop.tonight_fields_list
        fieldid_list = []
        for field in field_list:
            fieldid_list.append(field.fieldid)
        self.assertEqual(len(fieldid_list), 73)
        self.assertEqual(str(fieldid_list),
                         "[1764, 1819, 1824, 1825, 1840, 1841, 1860, 1861, 1873, 1939, 1940, 1949, 1950, "
                         "1973, 1974, 1996, 2006, 2061, 2066, 2067, 2084, 2085, 2105, 2106, 2108, 2183, "
                         "2184, 2201, 2202, 2211, 2212, 2226, 2234, 2304, 2315, 2316, 2319, 2320, 2329, "
                         "2330, 2346, 2425, 2426, 2427, 2428, 2439, 2440, 2450, 2464, 2536, 2543, 2544, "
                         "2555, 2556, 2563, 2564, 2572, 2655, 2656, 2657, 2658, 2669, 2670, 2682, 2692, "
                         "2762, 2769, 2770, 2783, 2784, 2787, 2788, 2802]")
        configfilepath = os.path.join(getPackageDir('ts_proposalScheduler'), 'tests', 'conf', 
                                      'survey', 'weak_lensing.conf')
        (path, name_ext) = os.path.split(configfilepath)
        (name, ext) = os.path.splitext(name_ext)
        proposal_confdict = read_conf_file(configfilepath)
        self.areaweak = AreaDistributionProposal(2, name, proposal_confdict, self.skyModel)
        self.areaweak.build_tonight_fields_list(lsst_start_timestamp, night)
        field_list = self.areaweak.tonight_fields_list
        fieldid_list = []
        for field in field_list:
            fieldid_list.append(field.fieldid)
        self.assertEqual(len(fieldid_list), 1515)

    def test_areadistributionproposal_start_night(self):

        lsst_start_timestamp = self.start_stamp
        night = 2
        self.areaprop.start_night(lsst_start_timestamp, ["g", "r", "i", "z", "y"], night)

        field_list = self.areaprop.tonight_fields_list
        fieldid_list = []
        for field in field_list:
            fieldid_list.append(field.fieldid)
        fieldid_list = fieldid_list[0:7]
        expected_fieldid_list = str([1764, 1819, 1824, 1825, 1840, 1841, 1860])
        self.assertEqual(str(fieldid_list), expected_fieldid_list)
        """ # Dictionaries will not always return contents in the same order. Bad test.
        self.assertEqual(str(self.areaprop.tonight_targets_dict[fieldid_list[0]]["g"]),
                         "targetid=0 field=1764 filter=g exp_times=[15.0, 15.0] ra=13.726 dec=-19.793 "
                         "ang=0.000 alt=0.000 az=0.000 rot=0.000 telalt=0.000 telaz=0.000 telrot=0.000 "
                         "time=0.0 airmass=0.000 brightness=0.000 cloud=0.00 seeing=0.00 "
                         "visits=0 progress=0.00% "
                         "seqid=0 ssname= groupid=1 groupix=1 firstdd=False ddvisits=0 "
                         "need=0.000 bonus=0.000 value=0.000 propboost=1.000 "
                         "propid=[] need=[] bonus=[] value=[] propboost=[] "
                         "slewtime=0.000 cost=0.000 rank=0.000")
        self.assertEqual(str(self.areaprop.tonight_targets_dict[fieldid_list[-1]]["g"]),
                         "targetid=0 field=2802 filter=g exp_times=[15.0, 15.0] ra=12.654 dec=3.318 "
                         "ang=0.000 alt=0.000 az=0.000 rot=0.000 telalt=0.000 telaz=0.000 telrot=0.000 "
                         "time=0.0 airmass=0.000 brightness=0.000 cloud=0.00 seeing=0.00 "
                         "visits=0 progress=0.00% "
                         "seqid=0 ssname= groupid=1 groupix=1 firstdd=False ddvisits=0 "
                         "need=0.000 bonus=0.000 value=0.000 propboost=1.000 "
                         "propid=[] need=[] bonus=[] value=[] propboost=[] "
                         "slewtime=0.000 cost=0.000 rank=0.000")
        """
        self.assertEqual(self.areaprop.survey_targets_goal, 7300)
        self.assertEqual(self.areaprop.survey_targets_visits, 0)
        self.assertEqual(self.areaprop.survey_targets_progress, 0.0)

    def test_areadistributionproposal_suggest_targets(self):

        lsst_start_timestamp = self.start_stamp
        night = 1
        self.areaprop.start_night(lsst_start_timestamp, ["g", "r", "i", "z", "y"], night)

        timestamp = lsst_start_timestamp
        target_list = self.areaprop.suggest_targets(timestamp, None, None, 0, 0)
        self.assertEqual(len(target_list), 100)
        self.assertEqual(str(target_list[0])[:75],
                         "targetid=0 field=1819 filter=g exp_times=[15.0, 15.0] ra=0.000 dec=-17.910 ")
        self.assertEqual(str(target_list[-1])[:73],
                         "targetid=0 field=2319 filter=g exp_times=[15.0, 15.0] ra=353.808 dec=-7.2")

        timestamp += 60
        target_list = self.areaprop.suggest_targets(timestamp, None, None, 0, 0)
        self.assertEqual(len(target_list), 100)
        self.assertEqual(str(target_list[0])[:75],
                         "targetid=0 field=1819 filter=g exp_times=[15.0, 15.0] ra=0.000 dec=-17.910 ")
        self.assertEqual(str(target_list[-1])[:73],
                         "targetid=0 field=2315 filter=y exp_times=[15.0, 15.0] ra=356.903 dec=-7.3")

        observation = target_list[0]
        self.assertEqual(observation.goal, 10)
        self.assertEqual(observation.visits, 0)
        self.assertEqual(observation.progress, 0.0)
        self.assertEqual(self.areaprop.survey_targets_goal, 7300.0)
        self.assertEqual(self.areaprop.survey_targets_visits, 0)
        self.assertEqual(self.areaprop.survey_targets_progress, 0.0)
        self.areaprop.register_observation(observation)
        self.assertEqual(observation.goal, 10)
        self.assertEqual(observation.visits, 1)
        self.assertEqual(observation.progress, 0.1)
        self.assertEqual(self.areaprop.survey_targets_goal, 7300.0)
        self.assertEqual(self.areaprop.survey_targets_visits, 1)
        self.assertEqual(self.areaprop.survey_targets_progress, 0.000136986301369863)

        timestamp += 60
        target_list = self.areaprop.suggest_targets(timestamp, None, None, 0, 0)
        self.assertEqual(len(target_list), 100)
        self.assertEqual(str(target_list[0])[:75],
                         "targetid=0 field=1819 filter=r exp_times=[15.0, 15.0] ra=0.000 dec=-17.910 ")
        self.assertEqual(str(target_list[-1])[:75],
                         "targetid=0 field=2315 filter=y exp_times=[15.0, 15.0] ra=356.903 dec=-7.324")

    def test_rolling_cadence_proposal_region_selections(self):
        configfilepath = os.path.join(getPackageDir('ts_proposalScheduler'), 'tests', 'conf', 'survey', 'rolling_cadence.conf')
        (path, name_ext) = os.path.split(configfilepath)
        (name, ext) = os.path.splitext(name_ext)
        proposal_confdict = read_conf_file(configfilepath)
        self.rolling = AreaDistributionProposal(2, name, proposal_confdict, self.skyModel)
        self.rolling.build_tonight_fields_list(1640995200.0, 1)
        field_list = self.rolling.tonight_fields_list
        fieldid_list = [field.fieldid for field in field_list]
        self.assertEqual(len(fieldid_list), 1621)

        self.rolling.build_tonight_fields_list(1704067200.0, 730)
        field_list = self.rolling.tonight_fields_list
        fieldid_list = [field.fieldid for field in field_list]
        self.assertEqual(len(fieldid_list), 546)

        self.rolling.build_tonight_fields_list(1767139200.0, 1460)
        field_list = self.rolling.tonight_fields_list
        fieldid_list = [field.fieldid for field in field_list]
        self.assertEqual(len(fieldid_list), 543)

        self.rolling.build_tonight_fields_list(1830211200.0, 2190)
        field_list = self.rolling.tonight_fields_list
        fieldid_list = [field.fieldid for field in field_list]
        self.assertEqual(len(fieldid_list), 531)

        self.rolling.build_tonight_fields_list(1893283200.0, 2920)
        field_list = self.rolling.tonight_fields_list
        fieldid_list = [field.fieldid for field in field_list]
        self.assertEqual(len(fieldid_list), 1617)
