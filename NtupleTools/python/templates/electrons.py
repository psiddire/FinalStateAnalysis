'''

Ntuple branch template sets for electron objects.

Each string is transformed into an expression on a FinalStateEvent object.

{object} should be replaced by an expression which evaluates to a pat::Electron
i.e. daughter(1) or somesuch.

Author: Evan K. Friis

'''

import FWCore.ParameterSet.Config as cms
from FinalStateAnalysis.Utilities.cfgtools import PSet

# ID and isolation
id = PSet(
    objectMVAIsoWP80 = '{object}.electronID("mvaEleID-Fall17-iso-V2-wp80")',
    objectMVAIsoWP90 = '{object}.electronID("mvaEleID-Fall17-iso-V2-wp90")',
    objectMVANoisoWP80 = '{object}.electronID("mvaEleID-Fall17-noIso-V2-wp80")',
    objectMVANoisoWP90 = '{object}.electronID("mvaEleID-Fall17-noIso-V2-wp90")',
    objectCorrectedEt = '{object}.userFloat("ecalTrkEnergyPostCorr")',
    objectEnergyScaleDown = '{object}.userFloat("energyScaleDown")',
    objectEnergyScaleUp = '{object}.userFloat("energyScaleUp")',
    objectEnergyScaleStatDown = '{object}.userFloat("energyScaleStatDown")',
    objectEnergyScaleStatUp = '{object}.userFloat("energyScaleStatUp")',
    objectEnergyScaleSystDown = '{object}.userFloat("energyScaleSystDown")',
    objectEnergyScaleSystUp = '{object}.userFloat("energyScaleSystUp")',
    objectEnergyScaleGainDown = '{object}.userFloat("energyScaleGainDown")',
    objectEnergyScaleGainUp = '{object}.userFloat("energyScaleGainUp")',
    objectEnergySigmaDown = '{object}.userFloat("energySigmaDown")',
    objectEnergySigmaUp = '{object}.userFloat("energySigmaUp")',
    objectEnergySigmaPhiDown = '{object}.userFloat("energySigmaPhiDown")',
    objectEnergySigmaPhiUp = '{object}.userFloat("energySigmaPhiUp")',
    objectEnergySigmaRhoDown = '{object}.userFloat("energySigmaRhoDown")',
    objectEnergySigmaRhoUp = '{object}.userFloat("energySigmaRhoUp")',

    objectRelPFIsoRho = cms.string(
        '({object}.pfIsolationVariables().sumChargedHadronPt'
        '+max(0.0,{object}.pfIsolationVariables().sumNeutralHadronEt'
        '+{object}.pfIsolationVariables().sumPhotonEt'
        '-{object}.userFloat("rho_fastjet")*{object}.userFloat("EffectiveArea")))'
        '/{object}.pt()'
    ),

    # Number of matched conversions
    objectPassesConversionVeto = '{object}.passConversionVeto()',

    # raw energy error
    objectEnergyError = '{object}.corrections().combinedP4Error',
    # shower shape / ID variables
    objectecalEnergy = '{object}.ecalEnergy',
    # Gen Info
    objectGenMotherPdgId = '? (getDaughterGenParticleMotherSmart({object_idx}, 11, 0).isAvailable && getDaughterGenParticleMotherSmart({object_idx}, 11, 0).isNonnull) ? getDaughterGenParticleMotherSmart({object_idx}, 11, 0).pdgId() : -999',
    objectComesFromHiggs = 'comesFromHiggs({object_idx}, 11, 1)',
    objectGenParticle    = '? ({object}.genParticleRef.isNonnull() ) ? {object}.genParticleRef().pdgId() : -999',
    objectGenPdgId       = '? (getDaughterGenParticle({object_idx}, 11, 0).isAvailable && getDaughterGenParticle({object_idx}, 11, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 11, 0).pdgId() : -999',
    objectGenCharge      = '? (getDaughterGenParticle({object_idx}, 11, 0).isAvailable && getDaughterGenParticle({object_idx}, 11, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 11, 0).charge() : -999',
    objectGenEnergy      = '? (getDaughterGenParticle({object_idx}, 11, 0).isAvailable && getDaughterGenParticle({object_idx}, 11, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 11, 0).energy() : -999',
    objectGenEta         = '? (getDaughterGenParticle({object_idx}, 11, 0).isAvailable && getDaughterGenParticle({object_idx}, 11, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 11, 0).eta()   : -999',
    objectGenPhi         = '? (getDaughterGenParticle({object_idx}, 11, 0).isAvailable && getDaughterGenParticle({object_idx}, 11, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 11, 0).phi()   : -999',
    objectGenPt          = '? (getDaughterGenParticle({object_idx}, 11, 0).isAvailable && getDaughterGenParticle({object_idx}, 11, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 11, 0).pt()   : -999',
    objectGenVZ          = '? (getDaughterGenParticle({object_idx}, 11, 0).isAvailable && getDaughterGenParticle({object_idx}, 11, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 11, 0).vz()   : -999',
    objectGenVtxPVMatch  = 'genVtxPVMatch({object_idx})', # is PV closest vtx to gen vtx?
    objectGenPromptTauDecay       = '? (getDaughterGenParticle({object_idx}, 11, 0).isAvailable && getDaughterGenParticle({object_idx}, 11, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 11, 0).statusFlags().isPromptTauDecayProduct() : -999',
    objectGenTauDecay       = '? (getDaughterGenParticle({object_idx}, 11, 0).isAvailable && getDaughterGenParticle({object_idx}, 11, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 11, 0).statusFlags().isTauDecayProduct() : -999',
    objectGenPrompt       = '? (getDaughterGenParticle({object_idx}, 11, 0).isAvailable && getDaughterGenParticle({object_idx}, 11, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 11, 0).statusFlags().isPrompt() : -999',

)

energyCorrections = PSet(

)

tracking = PSet(
    #objectHasConversion = '{object}.userFloat("hasConversion")',
    objectMissingHits = 'getElectronMissingHits({object_idx})',
)

# Information about the matched supercluster
supercluster = PSet(
)

trigger_50ns = PSet(
)

trigger_25ns_MC = PSet(
)

trigger_25ns = PSet(
)
