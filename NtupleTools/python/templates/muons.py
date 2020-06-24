'''

Ntuple branch template sets for muon objects.

Each string is transformed into an expression on a FinalStateEvent object.

{object} should be replaced by an expression which evaluates to a pat::Muon
i.e. daughter(1) or somesuch.

Author: Evan K. Friis

'''

import FWCore.ParameterSet.Config as cms
from FinalStateAnalysis.Utilities.cfgtools import PSet

# ID and isolation
id = PSet(
    objectPFIDTight = 'isTightMuon({object_idx})',
    objectPFIDMedium = '{object}.isMediumMuon()',
    objectPFIDLoose = '{object}.isLooseMuon()',

    objectRelPFIsoDBDefaultR04 = cms.string(
        '({object}.pfIsolationR04().sumChargedHadronPt'
        '+ max(0., {object}.pfIsolationR04().sumNeutralHadronEt'
        '+ {object}.pfIsolationR04().sumPhotonEt'
        '- 0.5*{object}.pfIsolationR04().sumPUPt))'
        '/{object}.pt()'
    ),

    objectIsPFMuon = '{object}.isPFMuon',
    objectIsGlobal = '{object}.isGlobalMuon',
    objectIsTracker = '{object}.isTrackerMuon',
    objectGenMotherPdgId = '? (getDaughterGenParticleMotherSmart({object_idx}, 13, 1).isAvailable && getDaughterGenParticleMotherSmart({object_idx}, 13, 1).isNonnull) ? getDaughterGenParticleMotherSmart({object_idx}, 13, 1).pdgId() : -999',
    objectComesFromHiggs = 'comesFromHiggs({object_idx}, 13, 1)',
        
    objectGenPromptTauDecay       = '? (getDaughterGenParticle({object_idx}, 13, 0).isAvailable && getDaughterGenParticle({object_idx}, 13, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 13, 0).statusFlags().isPromptTauDecayProduct() : -999',
    objectGenTauDecay       = '? (getDaughterGenParticle({object_idx}, 13, 0).isAvailable && getDaughterGenParticle({object_idx}, 13, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 13, 0).statusFlags().isTauDecayProduct() : -999',
    objectGenPrompt       = '? (getDaughterGenParticle({object_idx}, 13, 0).isAvailable && getDaughterGenParticle({object_idx}, 13, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 13, 0).statusFlags().isPrompt() : -999',

    objectGenParticle    = '? ({object}.genParticleRef.isNonnull() ) ? {object}.genParticleRef().pdgId() : -999',
    objectGenPdgId       = '? (getDaughterGenParticle({object_idx}, 13, 0).isAvailable && getDaughterGenParticle({object_idx}, 13, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 13, 0).pdgId() : -999',
    objectGenCharge      = '? (getDaughterGenParticle({object_idx}, 13, 0).isAvailable && getDaughterGenParticle({object_idx}, 13, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 13, 0).charge() : -999',
    objectGenEnergy      = '? (getDaughterGenParticle({object_idx}, 13, 0).isAvailable && getDaughterGenParticle({object_idx}, 13, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 13, 0).energy() : -999',
    objectGenEta         = '? (getDaughterGenParticle({object_idx}, 13, 0).isAvailable && getDaughterGenParticle({object_idx}, 13, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 13, 0).eta()   : -999',
    objectGenPhi         = '? (getDaughterGenParticle({object_idx}, 13, 0).isAvailable && getDaughterGenParticle({object_idx}, 13, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 13, 0).phi()   : -999',
    objectGenPt          = '? (getDaughterGenParticle({object_idx}, 13, 0).isAvailable && getDaughterGenParticle({object_idx}, 13, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 13, 0).pt()   : -999',
    objectGenVZ          = '? (getDaughterGenParticle({object_idx}, 13, 0).isAvailable && getDaughterGenParticle({object_idx}, 13, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 13, 0).vz()   : -999',
    objectGenVtxPVMatch  = 'genVtxPVMatch({object_idx})', # is PV closest vtx to gen vtx?
)

energyCorrections = PSet(
)

# Information about the associated track
tracking = PSet(
)

# Trigger matching
trigger_50ns = PSet(
)

trigger_25ns = PSet(
)
