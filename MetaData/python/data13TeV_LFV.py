"""
Data definitions for 13 TeV samples.
"""
from datacommon import square, cube, quad, picobarns, br_w_leptons, br_z_leptons, query_cli
from string import Template
try:
    from yellowhiggs import xs, br, xsbr
    br(130.0, 'WW')
except:

    def br(*args, **kwargs):
        return -99


    def xs(*args, **kwargs):
        return (-99, (-99, 99))


    def xsbr(*args, **kwargs):
        return (-99, (-99, 99))


data_name_map = {}
datadefs = {}


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


datadefs['GluGlu_LFV_HToETau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
'analyses': ['LFV'],
 'datasetpath': '/GluGlu_LFV_HToETau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAOD',
 'x_sec': 48.58*0.01
}
datadefs['VBF_LFV_HToETau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
'analyses': ['LFV'],
 'datasetpath': '/VBF_LFV_HToETau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAOD',
 'x_sec': 3.782*0.01
}


datadefs['DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
 'analyses': ['LFV'],
 'datasetpath': '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 5343
}
datadefs['DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
 'analyses': ['LFV'],
 'datasetpath': '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 21658.0#18610#15810
}
datadefs['DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1'] = {                  
 'analyses': ['LFV'],
 'datasetpath': '/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 877.8
}
datadefs['DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v2'] = {
 'analyses': ['LFV'],
 'datasetpath': 'DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 304.4
} 
datadefs['DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v2'] = {
 'analyses': ['LFV'],
 'datasetpath': 'DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 111.5
}
datadefs['DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_v2_94X_mc2017_realistic_v14-v2'] = {
 'analyses': ['LFV'],
 'datasetpath': '/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_v2_94X_mc2017_realistic_v14-v2/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 44.03
}


datadefs['WW_TuneCP5_13TeV-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
 'analyses': ['LFV'],
 'datsetpath': '/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 75.88#118.7
}
datadefs['WZ_TuneCP5_13TeV-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
 'analyses': ['LFV'],
 'datsetpath': '/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 27.57#47.13
}
datadefs['ZZ_TuneCP5_13TeV-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
 'analyses': ['LFV'],
 'datsetpath': '/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 12.14#16.52
}


datadefs['WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3'] = {
 'analyses': ['LFV'],
 'datasetpath': '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 52940
}
datadefs['W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4'] = {
 'analyses': ['LFV'],
 'datasetpath': '/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 8104.0
}
datadefs['W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v5'] = {
 'analyses': ['LFV'],
 'datasetpath': '/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v5/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 2793.0
}
datadefs['W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
 'analyses': ['LFV'],
 'datasetpath': '/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 992.5
}
datadefs['W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2'] = {
 'analyses': ['LFV'],
 'datasetpath': '/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 544.3
}
datadefs['WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
 'analyses': ['LFV'],
 'datasetpath': '/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 464.4
}


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
datadefs['TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1'] = {
 'analyses': ['LFV'],
 'datasetpath': '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
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

datadefs['QCD_Pt-20toInf_MuEnrichedPt15_TuneCP5_13TeV_pythia8_v14-v1'] = {
 'analyses': ['LFV'],
 'datasetpath': '/QCD_Pt-20toInf_MuEnrichedPt15_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 720648000#238900
}

datadefs['ZHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
 'analyses': ['LFV'],
 'datasetpath': '/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 0.884*0.0627
}
datadefs['ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1'] = {
 'analyses': ['LFV'],
 'datasetpath': '/ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 0.507*0.0627
}
datadefs['WminusHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
 'analyses': ['LFV'],
 'datasetpath': '/WminusHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 0.533*0.06272
}
datadefs['WplusHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1'] = {
 'analyses': ['LFV'],
 'datasetpath': '/WplusHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 0.840*0.06272
}


datadefs['EWKWMinus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2'] = {
 'analyses': ['LFV'],
 'datasetpath': '/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 20.25
}
datadefs['EWKWPlus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2'] = {
 'analyses': ['LFV'],
 'datasetpath': '/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 25.62
}
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


datadefs['data_SingleMuon_ReReco_Run2017B'] = {
 'datasetpath': '/SingleMuon/Run2017B-17Nov2017-v1/MINIAOD',
 'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
 'firstRun': 297050,
 'lastRun': 299329,
 'analyses': ['LFV'],
 'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_SingleMuon_ReReco_Run2017C'] = {
 'datasetpath': '/SingleMuon/Run2017C-17Nov2017-v1/MINIAOD',
 'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
 'firstRun': 299368,
 'lastRun': 302029,
 'analyses': ['LFV'],
 'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_SingleMuon_ReReco_Run2017D'] = {
 'datasetpath': '/SingleMuon/Run2017D-17Nov2017-v1/MINIAOD',
 'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
 'firstRun': 302031,
 'lastRun': 302663,
 'analyses': ['LFV'],
 'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_SingleMuon_ReReco_Run2017E'] = {
 'datasetpath': '/SingleMuon/Run2017E-17Nov2017-v1/MINIAOD',
 'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
 'firstRun': 303825,
 'lastRun': 304797,
 'analyses': ['LFV'],
 'calibrationTarget': 'RunIIFall17MiniAODv2'
}
datadefs['data_SingleMuon_ReReco_Run2017F'] = {
 'datasetpath': '/SingleMuon/Run2017F-17Nov2017-v1/MINIAOD',
 'lumi_mask': 'FinalStateAnalysis/RecoTools/data/masks/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
 'firstRun': 305044,
 'lastRun': 306460,
 'analyses': ['LFV'],
 'calibrationTarget': 'RunIIFall17MiniAODv2'
}


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


datadefs['embedded_EmbeddingRun2017B_MuMuFinalState'] = {
 'analyses': ['LFV'],
 'datasetpath': '/EmbeddingRun2017B/MuonEmbedding-inputDoubleMu_94X_miniAOD-v2/USER',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017C_MuMuFinalState'] = {
 'analyses': ['LFV'],
 'datasetpath': '/EmbeddingRun2017C/MuonEmbedding-inputDoubleMu_94X_miniAOD-v2/USER',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017D_MuMuFinalState'] = {
 'analyses': ['LFV'],
 'datasetpath': '/EmbeddingRun2017D/MuonEmbedding-inputDoubleMu_94X_miniAOD-v2/USER',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017E_MuMuFinalState'] = {
 'analyses': ['LFV'],
 'datasetpath': '/EmbeddingRun2017E/MuonEmbedding-inputDoubleMu_94X_miniAOD-v2/USER',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 1.0
}
datadefs['embedded_EmbeddingRun2017F_MuMuFinalState'] = {
 'analyses': ['LFV'],
 'datasetpath': '/EmbeddingRun2017F/MuonEmbedding-inputDoubleMu_94X_miniAOD-v2/USER',
 'pu': '2017',
 'calibrationTarget': 'RunIIFall17MiniAODv2',
 'x_sec': 1.0
}

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


if __name__ == '__main__':
    query_cli(datadefs)
