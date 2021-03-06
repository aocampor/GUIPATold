# The following comments couldn't be translated into the new config version:

#keep the logging output to a nice level

import FWCore.ParameterSet.Config as cms

process = cms.Process("RPCSegmentEff")

process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
process.load("Geometry.CSCGeometry.cscGeometry_cfi")
process.load("Geometry.DTGeometry.dtGeometry_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
process.load("RecoLocalMuon.RPCRecHit.rpcRecHits_cfi")
process.load("DQMServices.Components.MEtoEDMConverter_cfi")
process.load("DQMServices.Core.DQM_cfg")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.connect = "frontier://PromptProd/CMS_COND_31X_GLOBALTAG"
process.GlobalTag.globaltag = "GR09_31X_V1P::All"
process.prefer("GlobalTag")

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )
process.source = cms.Source("PoolSource",
                               fileNames = cms.untracked.vstring('----input_file----')
                            )


process.museg = cms.EDFilter("MuonSegmentEff",

                                 incldt = cms.untracked.bool(True),
                                 incldtMB4 = cms.untracked.bool(True),
                                 inclcsc = cms.untracked.bool(True),

                                 debug = cms.untracked.bool(False),
                                 inves = cms.untracked.bool(False),

                                     DuplicationCorrection = cms.untracked.int32(1),

                                 rangestrips = cms.untracked.double(4.),
                                 rangestripsRB4 = cms.untracked.double(4.),
                                 MinCosAng = cms.untracked.double(0.96),
                                 MaxD = cms.untracked.double(80.0),
                                 MaxDrb4 = cms.untracked.double(150.0),

                                 muonRPCDigis = cms.untracked.string('muonRPCDigis'),
                                 cscSegments = cms.untracked.string('cscSegments'),
                                 dt4DSegments = cms.untracked.string('dt4DSegments'),

                                 EffSaveRootFile = cms.untracked.bool(True),
                                 EffRootFileName = cms.untracked.string('----SRPC----'),
                                 EffSaveRootFileEventsInterval = cms.untracked.int32(100)
                             )

process.p = cms.Path(process.rpcRecHits*process.museg)
##process.p = cms.Path(process.museg)


process.DQM.collectorHost = ''
process.DQM.collectorPort = 9090
process.DQM.debug = False




