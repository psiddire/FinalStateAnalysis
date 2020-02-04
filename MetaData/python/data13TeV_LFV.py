'''
Data definitions for 13 TeV samples.
'''

from datacommon import square, cube, quad, picobarns, br_w_leptons, br_z_leptons, query_cli
from string import Template

try:
      from yellowhiggs import xs, br, xsbr
      br(130.,'WW')
except:
      #print "warning: yellowhiggs error"
      #define / override functions to avoid crashes
      def br(*args, **kwargs):
            return -99
      def xs(*args, **kwargs):
            return -99, (-99, 99)
      def xsbr(*args, **kwargs):
            return -99, (-99, 99)

data_name_map = {}

datadefs = {}

# 2018
datadefs["GluGlu_LFV_HToETau_M125_TuneCP5_PSweights_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses': ['LFV'],
      'datasetpath': '/GluGlu_LFV_HToETau_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu': 'upgrade2018',
      'calibrationTarget': 'RunIIAutumn18MiniAOD',
      'x_sec': 48.58*0.01,
}
datadefs["VBF_LFV_HToETau_M125_TuneCP5_PSweights_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses': ['LFV'],
      'datasetpath': '/VBF_LFV_HToETau_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu': 'upgrade2018',
      'calibrationTarget': 'RunIIAutumn18MiniAOD',
      'x_sec': 3.782*0.01,
}
datadefs["GluGlu_LFV_HToMuTau_M125_TuneCP5_PSweights_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses': ['LFV'],
      'datasetpath': '/GluGlu_LFV_HToMuTau_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu': 'upgrade2018',
      'calibrationTarget': 'RunIIAutumn18MiniAOD',
      'x_sec': 48.58*0.01,
}
datadefs["VBF_LFV_HToMuTau_M125_TuneCP5_PSweights_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses': ['LFV'],
      'datasetpath': '/VBF_LFV_HToMuTau_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu': 'upgrade2018',
      'calibrationTarget': 'RunIIAutumn18MiniAOD',
      'x_sec': 3.782*0.01,
}
# 2017
datadefs['GluGlu_LFV_HToETau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/GluGlu_LFV_HToETau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAOD',
      'x_sec': 48.58*0.01
}
datadefs['GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAOD',
      'x_sec': 48.58*0.01
}
datadefs['VBF_LFV_HToMuTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/VBF_LFV_HToMuTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAOD',
      'x_sec': 3.782*0.01
}
datadefs['VBF_LFV_HToETau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/VBF_LFV_HToETau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAOD',
      'x_sec': 3.782*0.01
}
# 2016
datadefs["GluGlu_LFV_HToETau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses': ['LFV'],
      'datasetpath': '/GluGlu_LFV_HToETau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu': 'PUMoriond17',
      'calibrationTarget': 'RunIISummer16MiniAODv3',
      'x_sec': 48.58*0.01,
}
datadefs["VBF_LFV_HToETau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"] = {
      'analyses': ['LFV'],
      'datasetpath': '/VBF_LFV_HToETau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
      'pu': 'PUMoriond17',
      'calibrationTarget': 'RunIISummer16MiniAODv3',
      'x_sec': 3.782*0.01,
}
datadefs["GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses': ['LFV'],
      'datasetpath': '/GluGlu_LFV_HToMuTau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu': 'PUMoriond17',
      'calibrationTarget': 'RunIISummer16MiniAODv3',
      'x_sec': 48.58*0.01,
}
datadefs["VBF_LFV_HToMuTau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses': ['LFV'],
      'datasetpath': '/VBF_LFV_HToMuTau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu': 'PUMoriond17',
      'calibrationTarget': 'RunIISummer16MiniAODv3',
      'x_sec': 3.782*0.01,
}

# 2018
datadefs["DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 5343.0,
}
datadefs["DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 18610.0,
}
datadefs["DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 877.8,
}
datadefs["DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 304.4,
}
datadefs["DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 111.5,
}
datadefs["DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' :  44.03,
}
# 2017
datadefs['DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 5343.0,
}
datadefs['DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 18610.0,
}
datadefs['DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_v3_94X_mc2017_realistic_v14_ext1-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_v3_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 877.8,
}
datadefs['DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': 'DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 304.4,
}
datadefs['DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': 'DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 111.5,
}
datadefs['DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_v2_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_v2_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 44.03,
}
# 2016
datadefs["DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 4963.0,
}
datadefs["DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 18610.0,
}
datadefs["DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 1012.5,
}
datadefs["DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 332.8,
}
datadefs["DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 101.8,
}
datadefs["DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' :  54.8,
}

# 2018
datadefs["WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 52940.0,
}
datadefs["W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 8104.0,
}
datadefs["W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 2793.0,
}
datadefs["W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 992.5,
}
datadefs["W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 544.3,
}
datadefs["WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 464.4,
}
# 2017
datadefs['WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3'] = {
      'analyses': ['LFV'],
      'datasetpath': '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 52940.0,
}
datadefs['W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4'] = {
      'analyses': ['LFV'],
      'datasetpath': '/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 8104.0,
}
datadefs['W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v5'] = {
      'analyses': ['LFV'],
      'datasetpath': '/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v5/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 2793.0,
}
datadefs['W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 992.5,
}
datadefs['W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 544.3,
}
datadefs['WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 464.4,
}
# 2016
datadefs["WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 50260.0,
}
datadefs["W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 9644.5,
}
datadefs["W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 3144.5,
}
datadefs["W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 954.8,
}
datadefs["W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 485.6,
}
datadefs["WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 489.0,
}

# 2018
datadefs["ZZ_TuneCP5_13TeV-pythia8_-102X_upgrade2018_realistic_v15-v2"]={
      'analyses' : ['LFV'],
      'datsetpath' : '/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 12.14,
}
datadefs["WZ_TuneCP5_13TeV-pythia8_-102X_upgrade2018_realistic_v15-v3"]={
      'analyses' : ['LFV'],
      'datsetpath' : '/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 27.57,
}
datadefs["WW_TuneCP5_13TeV-pythia8_-102X_upgrade2018_realistic_v15-v2"]={
      'analyses' : ['LFV'],
      'datsetpath' : '/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 75.88,
}
# 2017
datadefs['ZZ_TuneCP5_13TeV-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datsetpath': '/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 12.14,
}
datadefs['WZ_TuneCP5_13TeV-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datsetpath': '/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 27.57,
}
datadefs['WW_TuneCP5_13TeV-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datsetpath': '/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 75.88,
}
# 2016
datadefs["ZZ_TuneCUETP8M1_13TeV-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"]={
      'analyses' : ['LFV'],
      'datsetpath' : '/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 12.14,
}
datadefs["WZ_TuneCUETP8M1_13TeV-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"]={
      'analyses' : ['LFV'],
      'datsetpath' : '/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 27.57,
}
datadefs["WW_TuneCUETP8M1_13TeV-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"]={
      'analyses' : ['LFV'],
      'datsetpath' : '/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 75.88,
}

# 2018
datadefs["TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec': 88.29,
}
datadefs["TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec': 365.35,
}
datadefs["TTToHadronic_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec': 377.96,
}
# 2017
datadefs['TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 831.76
}
datadefs['TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 88.29
}
datadefs['TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 365.35
}
datadefs['TTToHadronic_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 377.96
}
# 2016
datadefs["TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec': 831.76,
}

# 2018
datadefs["ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15_ext1-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec': 35.85,
}
datadefs["ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15_ext1-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec': 35.85,
}
datadefs["ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec': 80.95,
}
datadefs["ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec': 136.02,
}
# 2017
datadefs['ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 35.85
}
datadefs['ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 35.85
}
datadefs['ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 80.95
}
datadefs['ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 136.02
}
# 2016
datadefs["ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec': 35.85,
}
datadefs["ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec': 35.85,
}
datadefs["ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec': 80.95,
}
datadefs["ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec': 136.02,
}

# 2018
datadefs["EWKZ2Jets_ZToLL_M-50_TuneCP5_PSweights_13TeV-madgraph-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/EWKZ2Jets_ZToLL_M-50_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 3.987,
}
datadefs["EWKZ2Jets_ZToNuNu_TuneCP5_PSweights_13TeV-madgraph-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/EWKZ2Jets_ZToNuNu_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 10.01,
}
datadefs["EWKWPlus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 25.62,
}
datadefs["EWKWMinus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 20.25,
}
# 2017
datadefs['EWKZ2Jets_ZToLL_M-50_TuneCP5_13TeV-madgraph-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EWKZ2Jets_ZToLL_M-50_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 3.987
}
datadefs['EWKZ2Jets_ZToNuNu_TuneCP5_13TeV-madgraph-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EWKZ2Jets_ZToNuNu_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 10.01
}
datadefs['EWKWPlus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 25.62
}
datadefs['EWKWMinus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 20.25
}
# 2016
datadefs["EWKZ2Jets_ZToLL_M-50_13TeV-madgraph-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v3"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/EWKZ2Jets_ZToLL_M-50_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v3/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 3.987,
}
datadefs["EWKZ2Jets_ZToNuNu_13TeV-madgraph-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/EWKZ2Jets_ZToNuNu_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 10.01,
}
datadefs["EWKWPlus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/EWKWPlus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 25.62,
}
datadefs["EWKWMinus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/EWKWMinus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 20.25,
}

# 2018
datadefs["GluGluHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 48.58*0.0627,
}
datadefs["VBFHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15_ext1-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 3.782*0.0627,
}
datadefs["WplusHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/WplusHToTauTau_M125_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 0.840*0.0627,
}
datadefs["WminusHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/WminusHToTauTau_M125_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 0.533*0.0627,
}
datadefs["ZHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 0.884*0.0627,
}
# 2017
datadefs['GluGluHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2'] = {
      'analyses': ['LFV'],
      'datasetpath': '/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 48.58*0.0627
}
datadefs['VBFHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 3.782*0.0627
}
datadefs['WplusHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/WplusHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 0.840*0.06272
}
datadefs['WminusHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/WminusHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 0.533*0.06272
}
datadefs['ZHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 0.884*0.0627
}
# 2016
datadefs["GluGluHToTauTau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v3"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v3/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 48.58*0.0627,
}
datadefs["VBFHToTauTau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 3.782*0.0627,
}
datadefs["WplusHToTauTau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/WplusHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 0.840*0.0627,
}
datadefs["WminusHToTauTau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/WminusHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 0.533*0.0627,
}
datadefs["ZHToTauTau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 0.884*0.0627,
}

# 2018
datadefs["GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 48.58*0.0227,
}
datadefs["VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 3.782*0.0227,
}
# 2017
datadefs['GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 48.58*0.0227
}
datadefs['VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 3.782*0.0227
}
# 2016
datadefs["GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 48.58*0.0227,
}
datadefs["VBFHToWWTo2L2Nu_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/VBFHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
      'pu' : 'PUMoriond17',
      'calibrationTarget' : 'RunIISummer16MiniAODv3',
      'x_sec' : 3.782*0.0227,
}

datadefs['QCD_Pt-20toInf_MuEnrichedPt15_TuneCP5_13TeV_pythia8_v14-v1'] = {
      'analyses': ['LFV'],
      'datasetpath': '/QCD_Pt-20toInf_MuEnrichedPt15_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
      'pu': 'PUMoriond17',
      'calibrationTarget': 'RunIISummer16MiniAODv3',
      'x_sec': 720648000.0,
}

# 2018
datadefs['embedded_EmbeddingRun2018A_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018A/MuTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'x_sec': 1.0,
      'pu' : 'upgrade2018',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018B_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018B/MuTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'x_sec': 1.0,
      'pu' : 'upgrade2018',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018C_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018C/MuTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'x_sec': 1.0,
      'pu' : 'upgrade2018',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018D_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018D/MuTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'x_sec': 1.0,
      'pu' : 'upgrade2018',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
# 2017
datadefs['embedded_EmbeddingRun2017B_MuTauFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017B/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017C_MuTauFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017C/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017D_MuTauFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017D/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017E_MuTauFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017E/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017F_MuTauFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017F/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
# 2016
datadefs['embedded_EmbeddingRun2016B_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016B/MuTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016C_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016C/MuTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016D_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016D/MuTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016E_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016E/MuTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016F_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016F/MuTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016G_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016G/MuTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016H_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016H/MuTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}

# 2018
datadefs['embedded_EmbeddingRun2018A_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018A/ElTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'x_sec': 1.0,
      'pu' : 'upgrade2018',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018B_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018B/ElTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'x_sec': 1.0,
      'pu' : 'upgrade2018',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018C_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018C/ElTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'x_sec': 1.0,
      'pu' : 'upgrade2018',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018D_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018D/ElTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'x_sec': 1.0,
      'pu' : 'upgrade2018',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
# 2017
datadefs['embedded_EmbeddingRun2017B_ElTauFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017B/ElTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017C_ElTauFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017C/ElTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017D_ElTauFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017D/ElTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017E_ElTauFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017E/ElTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017F_ElTauFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017F/ElTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
# 2016
datadefs['embedded_EmbeddingRun2016B_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016B/ElTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016C_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016C/ElTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016D_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016D/ElTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016E_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016E/ElTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016F_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016F/ElTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016G_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016G/ElTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016H_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016H/ElTauFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}

# 2018
datadefs['embedded_EmbeddingRun2018A_ElMuFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018A/ElMuFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'x_sec': 1.0,
      'pu' : 'upgrade2018',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018B_ElMuFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018B/ElMuFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'x_sec': 1.0,
      'pu' : 'upgrade2018',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018C_ElMuFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018C/ElMuFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'x_sec': 1.0,
      'pu' : 'upgrade2018',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018D_ElMuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018D/ElMuFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'x_sec': 1.0,
      'pu' : 'upgrade2018',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
# 2017
datadefs['embedded_EmbeddingRun2017B_ElMuFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017B/ElMuFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017C_ElMuFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017C/ElMuFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017D_ElMuFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017D/ElMuFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017E_ElMuFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017E/ElMuFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017F_ElMuFinalState'] = {
      'analyses': ['LFV'],
      'datasetpath': '/EmbeddingRun2017F/ElMuFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
      'pu': '2017',
      'calibrationTarget': 'RunIIFall17MiniAODv2',
      'x_sec': 1.0
}
# 2016
datadefs['embedded_EmbeddingRun2016B_ElMuFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016B/ElMuFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016C_ElMuFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016C/ElMuFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016D_ElMuFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016D/ElMuFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016E_ElMuFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016E/ElMuFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016F_ElMuFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016F/ElMuFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016G_ElMuFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016G/ElMuFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['embedded_EmbeddingRun2016H_ElMuFinalState'] = {
      'datasetpath' : "/EmbeddingRun2016H/ElMuFinalState-imputSep16DoubleMu_mirror_miniAOD-v2/USER",
      'x_sec': 1.0,
      'pu' : 'PUMoriond17',
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}

# 2018
datadefs['data_EGamma_Run2018A-17Sep2018'] = {
      'datasetpath' : "/EGamma/Run2018A-17Sep2018-v2/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 315257,
      'lastRun' : 316995,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['data_EGamma_Run2018B-17Sep2018'] = {
      'datasetpath' : "/EGamma/Run2018B-17Sep2018-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 317080,
      'lastRun' : 319077,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['data_EGamma_Run2018C-17Sep2018'] = {
      'datasetpath' : "/EGamma/Run2018C-17Sep2018-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 319337,
      'lastRun' : 320065,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['data_EGamma_Run2018D-PromptReco'] = {
      'datasetpath' : "/EGamma/Run2018D-PromptReco-v2/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 320673,
      'lastRun' : 325172,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
# 2017
datadefs['data_SingleElectron_Run2017B-31Mar2018'] = {
      'datasetpath': '/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 297050,
      'lastRun': 299329,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_SingleElectron_Run2017C-31Mar2018'] = {
      'datasetpath': '/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 299368,
      'lastRun': 302029,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_SingleElectron_Run2017D-31Mar2018'] = {
      'datasetpath': '/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 302031,
      'lastRun': 302663,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_SingleElectron_Run2017E-31Mar2018'] = {
      'datasetpath': '/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 303825,
      'lastRun': 304797,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_SingleElectron_Run2017F-31Mar2018'] = {
      'datasetpath': '/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 305044,
      'lastRun': 306460,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
# 2016
datadefs['data_SingleElectron_Run2016B_v1'] = {
      'datasetpath' : "/SingleElectron/Run2016B-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 273158,
      'lastRun' : 275376,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_SingleElectron_Run2016B_v2'] = {
      'datasetpath' : "/SingleElectron/Run2016B-23Sep2016-v2/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 273158,
      'lastRun' : 275376,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_SingleElectron_Run2016C'] = {
      'datasetpath' : "/SingleElectron/Run2016C-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 275657,
      'lastRun' : 276283,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_SingleElectron_Run2016D'] = {
      'datasetpath' : "/SingleElectron/Run2016D-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 276315,
      'lastRun' : 276811,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_SingleElectron_Run2016E'] = {
      'datasetpath' : "/SingleElectron/Run2016E-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 276831,
      'lastRun' : 277420,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_SingleElectron_Run2016F'] = {
      'datasetpath' : "/SingleElectron/Run2016F-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 277981,
      'lastRun' : 278808,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_SingleElectron_Run2016G'] = {
      'datasetpath' : "/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 278820,
      'lastRun' : 280385,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_SingleElectron_Run2016H'] = {
      'datasetpath' : "/SingleElectron/Run2016H-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 281613,
      'lastRun' : 284044,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}

# 2018
datadefs['data_SingleMuon_Run2018A-17Sep2018'] = {
      'datasetpath' : "/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 315257,
      'lastRun' : 316995,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['data_SingleMuon_Run2018B-17Sep2018'] = {
      'datasetpath' : "/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 317080,
      'lastRun' : 319077,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['data_SingleMuon_Run2018C-17Sep2018'] = {
      'datasetpath' : "/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 319337,
      'lastRun' : 320065,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['data_SingleMuon_Run2018D-PromptReco'] = {
      'datasetpath' : "/SingleMuon/Run2018D-PromptReco-v2/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 320673,
      'lastRun' : 325172,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
# 2017
datadefs['data_SingleMuon_Run2017B-31Mar2018'] = {
      'datasetpath': '/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 297050,
      'lastRun': 299329,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_SingleMuon_Run2017C-31Mar2018'] = {
      'datasetpath': '/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 299368,
      'lastRun': 302029,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_SingleMuon_Run2017D-31Mar2018'] = {
      'datasetpath': '/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 302031,
      'lastRun': 302663,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_SingleMuon_Run2017E-31Mar2018'] = {
      'datasetpath': '/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 303825,
      'lastRun': 304797,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_SingleMuon_Run2017F-31Mar2018'] = {
      'datasetpath': '/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 305044,
      'lastRun': 306460,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
# 2016
datadefs['data_SingleMuon_Run2016B_v1'] = {
      'datasetpath' : "/SingleMuon/Run2016B-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 273158,
      'lastRun' : 275376,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_SingleMuon_Run2016C'] = {
      'datasetpath' : "/SingleMuon/Run2016C-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 275657,
      'lastRun' : 276283,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_SingleMuon_Run2016D'] = {
      'datasetpath' : "/SingleMuon/Run2016D-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 276315,
      'lastRun' : 276811,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_SingleMuon_Run2016E'] = {
      'datasetpath' : "/SingleMuon/Run2016E-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 276831,
      'lastRun' : 277420,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_SingleMuon_Run2016F'] = {
      'datasetpath' : "/SingleMuon/Run2016F-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 277981,
      'lastRun' : 278808,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_SingleMuon_Run2016G'] = {
      'datasetpath' : "/SingleMuon/Run2016G-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 278820,
      'lastRun' : 280385,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_SingleMuon_Run2016H'] = {
      'datasetpath' : "/SingleMuon/Run2016H-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 281613,
      'lastRun' : 284044,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}

# 2018
datadefs['data_MuonEG_Run2018A-17Sep2018'] = {
      'datasetpath' : "/MuonEG/Run2018A-17Sep2018-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 315257,
      'lastRun' : 316995,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['data_MuonEG_Run2018B-17Sep2018'] = {
      'datasetpath' : "/MuonEG/Run2018B-17Sep2018-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 317080,
      'lastRun' : 319077,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['data_MuonEG_Run2018C-17Sep2018'] = {
      'datasetpath' : "/MuonEG/Run2018C-17Sep2018-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 319337,
      'lastRun' : 320065,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['data_MuonEG_Run2018D-PromptReco'] = {
      'datasetpath' : "/MuonEG/Run2018D-PromptReco-v2/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 320673,
      'lastRun' : 325172,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
# 2017
datadefs['data_MuonEG_Run2017B-31Mar2018'] = {
      'datasetpath': '/MuonEG/Run2017B-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 297050,
      'lastRun': 299329,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_MuonEG_Run2017C-31Mar2018'] = {
      'datasetpath': '/MuonEG/Run2017C-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 299368,
      'lastRun': 302029,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_MuonEG_Run2017D-31Mar2018'] = {
      'datasetpath': '/MuonEG/Run2017D-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 302031,
      'lastRun': 302663,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_MuonEG_Run2017E-31Mar2018'] = {
      'datasetpath': '/MuonEG/Run2017E-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 303825,
      'lastRun': 304797,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_MuonEG_Run2017F-31Mar2018'] = {
      'datasetpath': '/MuonEG/Run2017F-31Mar2018-v1/MINIAOD',
      'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
      'firstRun': 305044,
      'lastRun': 306460,
      'analyses': ['LFV'],
      'calibrationTarget': 'RunIIFall17MiniAODv2'
}
# 2016
datadefs['data_MuonEG_Run2016B_v1'] = {
      'datasetpath' : "/MuonEG/Run2016B-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 273158,
      'lastRun' : 275376,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_MuonEG_Run2016C'] = {
      'datasetpath' : "/MuonEG/Run2016C-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 275657,
      'lastRun' : 276283,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_MuonEG_Run2016D'] = {
      'datasetpath' : "/MuonEG/Run2016D-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 276315,
      'lastRun' : 276811,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_MuonEG_Run2016E'] = {
      'datasetpath' : "/MuonEG/Run2016E-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 276831,
      'lastRun' : 277420,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_MuonEG_Run2016F'] = {
      'datasetpath' : "/MuonEG/Run2016F-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 277981,
      'lastRun' : 278808,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_MuonEG_Run2016G'] = {
      'datasetpath' : "/MuonEG/Run2016G-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 278820,
      'lastRun' : 280385,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}
datadefs['data_MuonEG_Run2016H'] = {
      'datasetpath' : "/MuonEG/Run2016H-23Sep2016-v1/MINIAOD",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
      'firstRun' : 281613,
      'lastRun' : 284044,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIISummer16MiniAODv3'
}


if __name__=="__main__":
    query_cli(datadefs)
