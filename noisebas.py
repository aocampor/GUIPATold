import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        '----input_file----'
    )
)

process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

#Geometry
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
#process.load("MagneticField.Engine.volumeBasedMagneticField_cfi")
process.load("RecoLocalMuon.Configuration.RecoLocalMuonCosmics_cff")
process.load("RecoMuon.Configuration.RecoMuonCosmics_cff")
process.load("RecoMuon.MuonSeedGenerator.CosmicMuonSeedProducer_cfi")
process.load("RecoMuon.CosmicMuonProducer.cosmicMuons_cfi")

#Geometry
process.load("Geometry.DTGeometry.dtGeometry_cfi")
process.load("Alignment.CommonAlignmentProducer.GlobalPosition_Fake_cff")


process.demo = cms.EDAnalyzer('RPCOffLineNoise',
                              root_file_name = cms.untracked.string("----output_file----"),
                              GMTInputTag = cms.InputTag("muonRPCDigis"),
                              labelDT = cms.untracked.string("muonDTDigis"),
#                              bins = cms.untracked.int32(10000),
                              noise = cms.untracked.bool(False),
                              limit = cms.untracked.int32(100),
                              hours = cms.untracked.int32(10)      ### How many hours does the run takes                              
)


process.p = cms.Path(process.demo)
