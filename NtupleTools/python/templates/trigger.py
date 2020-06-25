'''

Ntuple branch template sets for trigger selections

Each string is transformed into an expression on a FinalStateEvent object.

Author: Evan K. Friis

IMPORTANT NOTE: If you want the logical OR of several paths, separate them 
by '|' rather than by ','. 
(When the Smart Trigger gets a group of paths separated by commas, it uses 
the one with the lowest prescale (taking the first in case of a tie).

'''

from FinalStateAnalysis.Utilities.cfgtools import PSet

_trig_template = PSet(
    namePass = 'evt.hltResult("paths")',
    #nameGroup = 'evt.hltGroup("paths")',
    #namePrescale = 'evt.hltPrescale("paths")',
)

singleLepton_25ns_MC = PSet(
    _trig_template.replace(
        name='IsoMu24',
        paths=r'HLT_IsoMu24_v\\d+'
        ),
    _trig_template.replace(
        name='IsoMu27',
        paths=r'HLT_IsoMu27_v\\d+'
        ),
    _trig_template.replace(
        name='Mu50',
        paths=r'HLT_Mu50_v\\d+'
        ),
    _trig_template.replace(
        name='singleE25eta2p1Tight',
        paths=r'HLT_Ele25_eta2p1_WPTight_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='Ele27WPTight',
        paths=r'HLT_Ele27_WPTight_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='Ele32WPTight',
        paths=r'HLT_Ele32_WPTight_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='Ele35WPTight',
        paths=r'HLT_Ele35_WPTight_Gsf_v\\d+'
        ),
    )

singleLepton_25ns = PSet(
    _trig_template.replace(
        name='IsoMu24',
        paths=r'HLT_IsoMu24_v\\d+'
        ),
    _trig_template.replace(
        name='IsoMu27',
        paths=r'HLT_IsoMu27_v\\d+'
        ),
    _trig_template.replace(
        name='Mu50',
        paths=r'HLT_Mu50_v\\d+'
        ),
    _trig_template.replace(
        name='singleE25eta2p1Tight',
        paths=r'HLT_Ele25_eta2p1_WPTight_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='Ele27WPTight',
        paths=r'HLT_Ele27_WPTight_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='Ele32WPTight',
        paths=r'HLT_Ele32_WPTight_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='Ele35WPTight',
        paths=r'HLT_Ele35_WPTight_Gsf_v\\d+'
        ),
    )

doubleLepton_25ns = PSet(
    _trig_template.replace(
        name='mu12e23DZ',
        paths=r'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v\\d+'
        ),
    _trig_template.replace(
        name='mu12e23',
        paths=r'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='mu23e12DZ',
        paths=r'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v\\d+'
        ),
    _trig_template.replace(
        name='mu23e12',
        paths=r'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='mu8e23DZ',
        paths=r'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v\\d+'
        ),
    _trig_template.replace(
        name='mu8e23',
        paths=r'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24LooseTau30',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24LooseTau30TightID',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_TightID_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24LooseHPSTau30',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24LooseHPSTau30TightID',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_TightID_CrossL1_v\\d+'
        ),
    )

tripleLepton = PSet(
    )

