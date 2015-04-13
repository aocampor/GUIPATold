import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#        'file:myfile.root'
              '----input_file----'
    )
)
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

#Geometry
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("Alignment.CommonAlignmentProducer.GlobalPosition_Fake_cff")
process.load("EventFilter.RPCRawToDigi.RPCSQLiteCabling_cfi")

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
#process.load("Configuration.StandardSequences.volumeBasedMagneticField_cfi")
process.load("RecoLocalMuon.Configuration.RecoLocalMuonCosmics_cff")
process.load("RecoMuon.Configuration.RecoMuonCosmics_cff")
process.load("RecoMuon.MuonSeedGenerator.CosmicMuonSeedProducer_cfi")
process.load("RecoMuon.CosmicMuonProducer.cosmicMuons_cfi")

#Geometry
process.load("Geometry.DTGeometry.dtGeometry_cfi")
process.load("Alignment.CommonAlignmentProducer.GlobalPosition_Fake_cff")
process.demo = cms.EDAnalyzer('RPCStripProfile',
                              GMTInputTag = cms.InputTag("muonRPCDigis"),
                              hours = cms.untracked.int32(5),      ### How many hours does the run takes
                              region = cms.untracked.int32(---region---),      ### Endcaps +-1 and barrel 0
                              subregion = cms.untracked.int32(---wheel---)      ### ring or wheel depending if endcap or barrel
)

process.TFileService = cms.Service("TFileService", fileName = cms.string('----strip----') )
#process.copyAll = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string("prueba.root") )
#process.printEventNumber = cms.EDAnalyzer("AsciiOutputModule")

process.p = cms.Path(process.demo)
#process.out = cms.EndPath(process.copyAll + process.printEventNumber)
