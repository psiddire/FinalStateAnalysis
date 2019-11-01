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
      'x_sec' : 21658.0,
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
      'x_sec' : 992.5,
}
datadefs["W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 544.3,
}
datadefs["W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 464.4,
}
datadefs["WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 464.4,
}


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
datadefs["ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v1"] = {
      'analyses' : ['LFV'],
      'datasetpath' : '/ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
      'pu' : 'upgrade2018',
      'calibrationTarget' : 'RunIIAutumn18MiniAOD',
      'x_sec' : 0.507*0.0627,
}


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


datadefs['embedded_EmbeddingRun2018A_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018A/MuTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 315257,
      'lastRun' : 316995,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018B_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018B/MuTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 317080,
      'lastRun' : 319077,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018C_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018C/MuTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 319337,
      'lastRun' : 320065,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018D_MuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018D/MuTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 320673,
      'lastRun' : 325172,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}


datadefs['embedded_EmbeddingRun2018A_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018A/ElTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 315257,
      'lastRun' : 316995,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018B_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018B/ElTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 317080,
      'lastRun' : 319077,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018C_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018C/ElTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 319337,
      'lastRun' : 320065,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018D_ElTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018D/ElTauFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 320673,
      'lastRun' : 325172,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}


datadefs['embedded_EmbeddingRun2018A_ElMuFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018A/ElMuFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 315257,
      'lastRun' : 316995,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018B_ElMuFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018B/ElMuFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 317080,
      'lastRun' : 319077,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018C_ElMuFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018C/ElMuFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 319337,
      'lastRun' : 320065,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}
datadefs['embedded_EmbeddingRun2018D_ElMuTauFinalState'] = {
      'datasetpath' : "/EmbeddingRun2018D/ElMuFinalState-inputDoubleMu_102X_miniAOD-v1/USER",
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
      'firstRun' : 320673,
      'lastRun' : 325172,
      'analyses' : ['LFV'],
      'calibrationTarget' : 'RunIIAutumn18MiniAOD'
}


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


if __name__=="__main__":
    query_cli(datadefs)
