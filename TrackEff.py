import FWCore.ParameterSet.Config as cms

process = cms.Process("RPCEff")

# Conditions (Global Tag is used here):
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.connect = "frontier://PromptProd/CMS_COND_31X_GLOBALTAG"
process.GlobalTag.globaltag = "GR09_31X_V1P::All"
process.prefer("GlobalTag")

#Geometry
process.load("Configuration.StandardSequences.Geometry_cff")

# reconstruction sequence for Cosmics
process.load("Configuration.StandardSequences.ReconstructionCosmics_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")

process.load("RecoLocalMuon.RPCRecHit.rpcRecHits_cfi")
##------------ Cosmics ----------------------------------------------------
# Seed generator
from RecoMuon.MuonSeedGenerator.CosmicMuonSeedProducer_cfi import *
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cfi")
process.load("RecoLocalMuon.Configuration.RecoLocalMuonCosmics_cff")
process.load("RecoMuon.Configuration.RecoMuonCosmics_cff")
process.load("RecoMuon.MuonSeedGenerator.CosmicMuonSeedProducer_cfi")
process.load("RecoMuon.CosmicMuonProducer.cosmicMuons_cfi")
process.cosmicMuons.TrajectoryBuilderParameters.EnableRPCMeasurement = False
##--------------------------------------------------------------------------

process.load("DQMServices.Components.MEtoEDMConverter_cfi")
process.load("DQMServices.Core.DQM_cfg")

process.source = cms.Source("PoolSource",
    debugFlag = cms.untracked.bool(True),
    debugVebosity = cms.untracked.uint32(10),
    fileNames = cms.untracked.vstring(
    '----input_file----'
    )
)

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.ModuleWebRegistry = cms.Service("ModuleWebRegistry")

process.LockService = cms.Service("LockService",
    labels = cms.untracked.vstring('source')
)

from RecoMuon.TrackingTools.MuonServiceProxy_cff import *
process.load("RecoMuon.TrackingTools.MuonServiceProxy_cff")

process.rpcefftrack = cms.EDFilter("RPCEffTrackExtrapolationNew",
                                   MuonServiceProxy,
                                   dt4DSegments = cms.InputTag("dt4DSegments"),
                                   cscSegments =  cms.InputTag("cscSegments"),
                                   RPCRecHits = cms.InputTag("rpcRecHits"),
                                   NavigationType = cms.string("Direct"),
                                   trajectoryInput = cms.untracked.string('cosmicMuons'),
                                   EffRootFileName = cms.untracked.string('---GRPC---'),
                                   PropagatorName = cms.string('SteppingHelixPropagatorAny')
                                   )

##process.p1 = cms.Path(process.cosmicMuons*process.rpcefftrack)

process.p1 = cms.Path(process.offlineBeamSpot*process.CosmicMuonSeed*process.cosmicMuons*process.rpcRecHits*process.rpcefftrack)


process.DQM.collectorHost = ''
process.DQM.collectorPort = 9090
process.DQM.debug = False

