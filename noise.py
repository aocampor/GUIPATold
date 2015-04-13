import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("Alignment.CommonAlignmentProducer.GlobalPosition_Fake_cff")
process.load("EventFilter.RPCRawToDigi.RPCSQLiteCabling_cfi")
process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
process.load("Geometry.CommonDetUnit.bareGlobalTrackingGeometry_cfi")
process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
process.load("RecoMuon.DetLayers.muonDetLayerGeometry_cfi")
process.load("MagneticField.Engine.volumeBasedMagneticField_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
    '----input_file----'
    )
)

process.demo = cms.EDAnalyzer('Noise',
        histoName = cms.untracked.string('----output_file----')                      
)


process.p = cms.Path(process.demo)
