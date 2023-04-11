import FWCore.ParameterSet.Config as cms

process = cms.Process("test")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('RecoPPS.Local.totemTimingLocalReconstruction_cff')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.a1 = cms.EDAnalyzer("StreamThingAnalyzer",
    product_to_get = cms.string('m1')
)

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#from Configuration.AlCa.GlobalTag import GlobalTag
#from Configuration.AlCa.autoCond import autoCond
#process.GlobalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_Prompt_Candidate_2023_04_07_14_18_21', '')

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/data/Run2022C/AlCaPPSPrompt/ALCARECO/PPSCalMaxTracks-PromptReco-v1/000/357/329/00000/34f014fe-db35-4c71-aba5-a76206ded90a.root'
),
)

from Configuration.EventContent.EventContent_cff import *

process.output = cms.OutputModule('PoolOutputModule',
    fileName = cms.untracked.string('file:testoutput.root'),
    outputCommands = AODEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.output.outputCommands.append('keep *')
process.output.outputCommands.append('drop CTPPSDiamondRecHitedmDetSetVector_ctppsDiamondRecHitsAlCaRecoProducer__RECO')

process.end_path = cms.EndPath(
    process.output
)

process.schedule = cms.Schedule(
    process.end_path
)
