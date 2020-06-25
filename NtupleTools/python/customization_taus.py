# Embed IDs for taus
import FWCore.ParameterSet.Config as cms
import re

def processDeepProducer(process, producer_name, tauIDSources, workingPoints_):
        for target,points in workingPoints_.iteritems():
            cuts = cms.PSet()
            setattr(tauIDSources, 'by{}VS{}raw'.format(producer_name[0].upper()+producer_name[1:], target),
                        cms.InputTag(producer_name, 'VS{}'.format(target)))
            for point,cut in points.iteritems():
                setattr(cuts, point, cms.string(str(cut)))

                setattr(tauIDSources, 'by{}{}VS{}'.format(point, producer_name[0].upper()+producer_name[1:], target),
                        cms.InputTag(producer_name, 'VS{}{}'.format(target, point)))
            setattr(getattr(process, producer_name), 'VS{}WP'.format(target), cuts)
	    #if "deep" in producer_name:
	    # 	raise RuntimeError('File "{}"'.format(tauIDSources))

def getDpfTauVersion(file_name):
        """returns the DNN version. File name should contain a version label with data takig year (2011-2, 2015-8) and \
           version number (vX), e.g. 2017v0, in general the following format: {year}v{version}"""
        version_search = re.search('201[125678]v([0-9]+)[\._]', file_name)
        if not version_search:
            raise RuntimeError('File "{}" has an invalid name pattern, should be in the format "{year}v{version}". \
                                Unable to extract version number.'.format(file_name))
        version = version_search.group(1)
	return int(version)

def getDeepTauVersion(file_name):
        """returns the DeepTau year, version, subversion. File name should contain a version label with data takig year \
        (2011-2, 2015-8), version number (vX) and subversion (pX), e.g. 2017v0p6, in general the following format: \
        {year}v{version}p{subversion}"""
        version_search = re.search('(201[125678])v([0-9]+)(p[0-9]+|)[\._]', file_name)
        if not version_search:
            raise RuntimeError('File "{}" has an invalid name pattern, should be in the format "{year}v{version}p{subversion}". \
                                Unable to extract version number.'.format(file_name))
        year = version_search.group(1)
        version = version_search.group(2)
        subversion = version_search.group(3)
        if len(subversion) > 0:
            subversion = subversion[1:]
        else:
            subversion = 0
        return int(year), int(version), int(subversion)


def preTaus(process, year, isEmbedded, tSrc, vSrc, **kwargs):

    postfix = kwargs.pop('postfix', '')
    rerunMvaIDs = bool(kwargs.pop('rerunMvaIDs', 0))

    if rerunMvaIDs :
	# Deep Tau v2
        tauIDSources = cms.PSet()
        workingPoints_ = {
                "e": {
                    "VVVLoose": 0.0630386,
                    "VVLoose": 0.1686942,
                    "VLoose": 0.3628130,
                    "Loose": 0.6815435,
                    "Medium": 0.8847544,
                    "Tight": 0.9675541,
                    "VTight": 0.9859251,
                    "VVTight": 0.9928449,
                },
                "mu": {
                    "VLoose": 0.1058354,
                    "Loose": 0.2158633,
                    "Medium": 0.5551894,
                    "Tight": 0.8754835,
                },
                "jet": {
                    "VVVLoose": 0.2599605,
                    "VVLoose": 0.4249705,
                    "VLoose": 0.5983682,
                    "Loose": 0.7848675,
                    "Medium": 0.8834768,
                    "Tight": 0.9308689,
                    "VTight": 0.9573137,
                    "VVTight": 0.9733927,
                },
	}

        file_names = [
             'core:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_core.pb',
             'inner:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_inner.pb',
             'outer:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_outer.pb',
        ]
        process.deepTau2017v2p1 = cms.EDProducer("DeepTauId",
                electrons              = cms.InputTag('slimmedElectrons'),
                muons                  = cms.InputTag('slimmedMuons'),
                taus                   = cms.InputTag(tSrc),
                pfcands                = cms.InputTag('packedPFCandidates'),
                vertices               = cms.InputTag('offlineSlimmedPrimaryVertices'),
                rho                    = cms.InputTag('fixedGridRhoAll'),
                graph_file             = cms.vstring(file_names),
                mem_mapped             = cms.bool(True),
                version                = cms.uint32(getDeepTauVersion(file_names[0])[1]),
                debug_level            = cms.int32(0),
                disable_dxy_pca        = cms.bool(True)

        )

        processDeepProducer(process,'deepTau2017v2p1', tauIDSources, workingPoints_)

        # this sequence has to be included in your cms.Path() before your analyzer which accesses the new variables is called.
        process.rerunMvaIsolation2SeqRun2 = cms.Path(process.deepTau2017v2p1)
        process.schedule.append( process.rerunMvaIsolation2SeqRun2 )

        # embed rerun MVA IDs
        modName = 'miniTausEmbedRerunMVAIDs{0}'.format(postfix)
        mod = cms.EDProducer(
            "MiniAODTauRerunIDEmbedder",
            src = cms.InputTag(tSrc),

            byDeepTau2017v2p1VSmuraw = cms.InputTag("deepTau2017v2p1","VSmu"),
            byLooseDeepTau2017v2p1VSmu = cms.InputTag("deepTau2017v2p1","VSmuLoose"),
            byMediumDeepTau2017v2p1VSmu = cms.InputTag("deepTau2017v2p1","VSmuMedium"),
            byTightDeepTau2017v2p1VSmu = cms.InputTag("deepTau2017v2p1","VSmuTight"),
            byVLooseDeepTau2017v2p1VSmu = cms.InputTag("deepTau2017v2p1","VSmuVLoose"),
            byVTightDeepTau2017v2p1VSmu = cms.InputTag("deepTau2017v2p1","VSmuVTight"),
            byVVLooseDeepTau2017v2p1VSmu = cms.InputTag("deepTau2017v2p1","VSmuVVLoose"),
            byVVTightDeepTau2017v2p1VSmu = cms.InputTag("deepTau2017v2p1","VSmuVVTight"),
            byVVVLooseDeepTau2017v2p1VSmu = cms.InputTag("deepTau2017v2p1","VSmuVVVLoose"),
            byDeepTau2017v2p1VSeraw = cms.InputTag("deepTau2017v2p1","VSe"),
            byLooseDeepTau2017v2p1VSe = cms.InputTag("deepTau2017v2p1","VSeLoose"),
            byMediumDeepTau2017v2p1VSe = cms.InputTag("deepTau2017v2p1","VSeMedium"),
            byTightDeepTau2017v2p1VSe = cms.InputTag("deepTau2017v2p1","VSeTight"),
            byVLooseDeepTau2017v2p1VSe = cms.InputTag("deepTau2017v2p1","VSeVLoose"),
            byVTightDeepTau2017v2p1VSe = cms.InputTag("deepTau2017v2p1","VSeVTight"),
            byVVLooseDeepTau2017v2p1VSe = cms.InputTag("deepTau2017v2p1","VSeVVLoose"),
            byVVTightDeepTau2017v2p1VSe = cms.InputTag("deepTau2017v2p1","VSeVVTight"),
            byVVVLooseDeepTau2017v2p1VSe = cms.InputTag("deepTau2017v2p1","VSeVVVLoose"),
            byDeepTau2017v2p1VSjetraw = cms.InputTag("deepTau2017v2p1","VSjet"),
            byLooseDeepTau2017v2p1VSjet = cms.InputTag("deepTau2017v2p1","VSjetLoose"),
            byMediumDeepTau2017v2p1VSjet = cms.InputTag("deepTau2017v2p1","VSjetMedium"),
            byTightDeepTau2017v2p1VSjet = cms.InputTag("deepTau2017v2p1","VSjetTight"),
            byVLooseDeepTau2017v2p1VSjet = cms.InputTag("deepTau2017v2p1","VSjetVLoose"),
            byVTightDeepTau2017v2p1VSjet = cms.InputTag("deepTau2017v2p1","VSjetVTight"),
            byVVLooseDeepTau2017v2p1VSjet = cms.InputTag("deepTau2017v2p1","VSjetVVLoose"),
            byVVTightDeepTau2017v2p1VSjet = cms.InputTag("deepTau2017v2p1","VSjetVVTight"),
            byVVVLooseDeepTau2017v2p1VSjet = cms.InputTag("deepTau2017v2p1","VSjetVVVLoose"),

        )
        tSrc = modName
        setattr(process,modName,mod)

        pathName = 'runMiniAODTauRerunMVAIDEmbedding{0}'.format(postfix)
        path = cms.Path(getattr(process,modName))
        setattr(process,pathName,path)
        process.schedule.append(getattr(process,pathName))

    modName = 'genembeddedTaus{0}'.format(postfix)
    mod=cms.EDProducer("PATTauGenInfoEmbedder",
          src=cms.InputTag(tSrc)
    )
    setattr(process,modName,mod)
    tSrc = modName
    modPath = 'embeddedTaus{0}'.format(postfix)
    setattr(process,modPath,cms.Path(getattr(process,modName)))
    
    process.schedule.append(getattr(process,modPath))

    # embed IP stuff
    modName = 'miniTausEmbedIp{0}'.format(postfix)
    mod = cms.EDProducer(
        "MiniAODTauIpEmbedder",
        src = cms.InputTag(tSrc),
        vtxSrc = cms.InputTag(vSrc),
    )
    tSrc = modName
    setattr(process,modName,mod)

    pathName = 'runMiniAODTauIpEmbedding{0}'.format(postfix)
    path = cms.Path(getattr(process,modName))
    setattr(process,pathName,path)
    process.schedule.append(getattr(process,pathName))

    # embed trigger filters
    modName = 'minitriggerfilterTaus{0}'.format(postfix)
    mod = cms.EDProducer(
        "MiniAODTauTriggerFilterEmbedder",
        src=cms.InputTag(tSrc),
        bits = cms.InputTag("TriggerResults","","HLT"),
        objects = cms.InputTag("slimmedPatTrigger"),
        #bits = cms.InputTag("TriggerResults","","SIMembedding"),
        #objects = cms.InputTag("slimmedPatTrigger","","MERGE"),
    )
    if isEmbedded:
        mod.bits=cms.InputTag("TriggerResults","","SIMembedding")
        mod.objects=cms.InputTag("slimmedPatTrigger","","MERGE")
	if year=="2016":
	   mod.objects=cms.InputTag("slimmedPatTrigger","","PAT")
    tSrc = modName
    setattr(process,modName,mod)

    pathName = 'runTriggerFilterTauEmbedding{0}'.format(postfix)
    modPath = cms.Path(getattr(process,modName))
    setattr(process,pathName,modPath)
    process.schedule.append(getattr(process,pathName))

    return tSrc


def postTaus(process, tSrc, jSrc,**kwargs):
    postfix = kwargs.pop('postfix','')
    modName = 'miniAODTauJetInfoEmbedding{0}'.format(postfix)
    mod = cms.EDProducer(
        "MiniAODTauJetInfoEmbedder",
        src = cms.InputTag(tSrc),
        embedBtags = cms.bool(False),
        suffix = cms.string(''),
        jetSrc = cms.InputTag(jSrc),
        maxDeltaR = cms.double(0.5),
    )
    setattr(process,modName,mod)
    tSrc = modName
    modPath = 'TauJetInfoEmbedding{0}'.format(postfix)
    setattr(process,modPath,cms.Path(getattr(process,modName)))
    process.schedule.append(getattr(process,modPath))

    return tSrc

