# Embed IDs for jets
import FWCore.ParameterSet.Config as cms
import os

def preMETFromUES(process, pfSrc, jSrc, vSrc, metSrc, mSrc, eSrc, tSrc, pSrc):

    process.metUncSequence = cms.Sequence()

    #Jet projection ==
    pfCandsNoJets = cms.EDProducer("CandPtrProjector", 
        src = cms.InputTag(pfSrc), 
        veto = cms.InputTag(jSrc)
    )
    setattr(process, "pfCandsNoJets", pfCandsNoJets)
    process.metUncSequence += getattr(process, "pfCandsNoJets")
    #electron projection ==
    pfCandsNoJetsNoEle = cms.EDProducer("CandPtrProjector", 
        src = cms.InputTag("pfCandsNoJets"),
        veto = cms.InputTag(eSrc)
    )
    setattr(process, "pfCandsNoJetsNoEle", pfCandsNoJetsNoEle)
    process.metUncSequence += getattr(process, "pfCandsNoJetsNoEle")
    #muon projection ==
    pfCandsNoJetsNoEleNoMu = cms.EDProducer("CandPtrProjector", 
        src = cms.InputTag("pfCandsNoJetsNoEle"),
        veto = cms.InputTag(mSrc)
    )
    setattr(process, "pfCandsNoJetsNoEleNoMu", pfCandsNoJetsNoEleNoMu)
    process.metUncSequence += getattr(process, "pfCandsNoJetsNoEleNoMu")
    #tau projection ==
    pfCandsNoJetsNoEleNoMuNoTau = cms.EDProducer("CandPtrProjector", 
        src = cms.InputTag("pfCandsNoJetsNoEleNoMu"),
        veto = cms.InputTag(tSrc)
    )
    setattr(process, "pfCandsNoJetsNoEleNoMuNoTau", pfCandsNoJetsNoEleNoMuNoTau)
    process.metUncSequence += getattr(process, "pfCandsNoJetsNoEleNoMuNoTau")
    #photon projection ==
    pfCandsForUnclusteredUnc = cms.EDProducer("CandPtrProjector", 
        src = cms.InputTag("pfCandsNoJetsNoEleNoMuNoTau"),
        veto = cms.InputTag(pSrc)
    )
    setattr(process, "pfCandsForUnclusteredUnc", pfCandsForUnclusteredUnc)
    process.metUncSequence += getattr(process, "pfCandsForUnclusteredUnc")

    process.metUncPath = cms.Path(process.metUncSequence)
    process.schedule.append(process.metUncPath)
    
    modName = 'miniAODMETUesSystEmbedding'
    mod = cms.EDProducer(
        "MiniAODMETUesSystEmbedder",
        srcMET = cms.untracked.InputTag(metSrc),
        srcPF = cms.untracked.InputTag("pfCandsForUnclusteredUnc"),
        )
    metSrc = modName
    setattr(process,modName,mod)
    
    pathName = 'metUesSystematicsEmbedding'
    path = cms.Path(getattr(process,modName))
    setattr(process,pathName,path)
    
    print modName+" for  MET?"
    
    process.schedule.append(getattr(process,pathName))

    print metSrc 

    return metSrc

