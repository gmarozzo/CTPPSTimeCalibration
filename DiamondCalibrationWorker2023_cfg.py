import FWCore.ParameterSet.Config as cms

process = cms.Process("PPSTiming2")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('RecoPPS.Local.totemTimingLocalReconstruction_cff')
#process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.a1 = cms.EDAnalyzer("StreamThingAnalyzer",
    product_to_get = cms.string('m1')
)

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_Prompt_Candidate_2023_04_07_14_18_21', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_Express_v3')
#process.GlobalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_Prompt_v3')

process.load("EventFilter.CTPPSRawToDigi.ctppsRawToDigi_cff")
process.load("RecoPPS.Configuration.recoCTPPS_cff")
#process.ctppsDiamondRecHits.timingCalibrationTag=cms.string("GlobalTag:PPSTestCalibration")
process.ctppsDiamondRecHits.applyCalibration = False
#process.ctppsDiamondRecHits.digiTag = cms.InputTag("ctppsDiamondRawToDigiAlCaRecoProducer", "TimingDiamond")
process.ctppsDiamondRecHits.digiTag = cms.InputTag("ctppsDiamondRawToDigi","TimingDiamond")

#process.load('CondCore.CondDB.CondDB_cfi')
#process.CondDB.connect = 'sqlite_file:ppsDiamondTiming_calibration355933.sqlite' # SQLite input
#process.PoolDBESSource = cms.ESSource('PoolDBESSource',
#        process.CondDB,
#        DumpStats = cms.untracked.bool(True),
#        toGet = cms.VPSet(
#            cms.PSet(
#                record = cms.string('PPSTimingCalibrationRcd'),
#                tag = cms.string('DiamondTimingCalibration')
#        )
#    )
#)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/01f3728c-4307-43e6-9806-bbcb4dc79959.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/034638ca-f116-4f41-9eef-ac2760c62ce8.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/037476be-99b3-4f96-9cf9-611e446ad5ac.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/04b135c8-3039-45eb-a37e-e6f7b24d1683.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/07230a95-ef2a-43ac-9565-7bea94a9cf01.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/0b356c45-1e79-46d5-9972-395fa33ac954.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/0b814922-128a-4134-bca8-44630e5aeb70.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/0be0dff9-4058-4d27-b533-fe776e18d251.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/0cbad0d4-1ac1-4cca-8a27-33dff81ab6ec.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/101e17f7-b19f-4a25-8671-60ceeacea217.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/107bf18f-8142-451f-bd02-4576946bc6c9.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/15561d8b-f8b5-4946-bd41-372654d0fb18.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/19a0b8f7-e79f-4dd2-ba53-d06420db3d5f.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/1b775a4e-eeb9-416a-923a-ddf73debbfea.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/1bf7e474-2255-4657-8e2d-aeed1cde4c5b.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/1e809cba-1351-4ce6-853a-4b4082c5687e.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/22d1758a-7ae5-4249-a62e-abf4d57bbeaf.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/245f4c49-f76e-452f-a1b0-a7c4fa2b890e.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/2a8ed4cd-b312-4d27-9709-b2accf54907b.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/31989524-fe7b-4231-91fd-3e16e12a5194.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/31c2d906-cf31-4c12-90fb-0aeccd94c10b.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/326496f5-dee5-49f5-aee1-41519b5b4459.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/333c19d2-38cd-44ec-9e0c-2b96ede5078a.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/35486453-037d-48ef-bd2d-969769a6f853.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/406d8952-db17-4429-90df-86a42d196889.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/4276fc0a-be2f-4d24-b5f0-d8e2777293c8.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/446e31d8-c299-4cc4-b3f8-7f3fcc9b0085.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/4a9f3a34-5c25-4a90-9b55-d1ba10b18164.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/4bf517e8-a9ab-4748-bd02-01b30764ec0b.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/4c0719a1-9100-41cf-bd30-149b2383c2a6.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/4f111ad7-f20a-4f2f-8efb-b172147c9026.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/52522551-f56e-4974-96c1-ac72ef1893f3.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/5326ad11-8cd8-45cb-a46b-49df4f67c794.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/53c5da81-a779-492e-998a-94daf9e560d7.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/587753e0-8f4b-45c9-8597-bafdafbf2dda.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/5ac31660-517f-47b9-b91d-8253e274440b.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/5e8fe798-0280-4d83-acef-e2d5bb9c9c77.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/60831672-80f2-4e3d-8ec4-afe0fe7ce8d3.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/62fa735e-78c6-44b5-b630-247d1cb1e074.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/63cb3366-9eae-4751-b816-517d05e7f4e7.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/691be1ae-635c-435d-868c-ad3d80b6df2d.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/6ec4b6c0-fac7-42dc-9b47-2d873d7862af.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/7412e071-1a1b-4be2-ab40-ac53e42bc06f.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/74394f01-b246-4a99-9fc9-fdd71c83d1ff.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/764d87c0-6630-498f-bce2-f8b76be12e49.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/772d055a-9024-4832-825f-18779f41ff69.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/78a85068-37a9-4e4e-a0d7-9b647721dab0.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/796e61f5-c4ac-40f7-a8b3-f57e199a5060.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/7a27baa5-95c6-44b4-92e6-f86069d13f7e.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/7d329351-34ef-4a95-ba95-a15e6589f359.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/82659e32-5adf-40e9-abf8-54f1a71130f2.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/85979def-3006-4980-9426-cf8798809f4c.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/859ebac6-a712-428c-b9d4-95a444bcdf78.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/86cf8096-b331-413a-acda-67abc2ea9b41.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/886e1c1e-9e97-4239-82a0-020daccd7e58.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/886e55cb-8196-4ec9-b052-0bd58919c83e.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/899ba33f-aabd-46c9-8eb9-8139125bfca5.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/8a6e454a-b6ea-4083-9292-b21dbb4df4f4.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/8fed8a1c-e572-4b19-b030-5f6e276000c2.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/a872a54b-308b-4630-9444-70ee8968c11f.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/ab1f5188-c06a-4449-8cd3-7eb830a461fd.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/ac2b6604-696c-4343-897c-48f0ef539831.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/af22895c-7579-4a19-818a-0152e832650a.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/b251f9c3-f882-4768-9424-9b3d507aa4f7.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/b549cc31-d991-430d-ac9b-1a6c9769e587.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/b67ea9e6-cf21-4975-8abc-08c5370407c4.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/b978509a-eafb-4838-b09b-7cedc089e073.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/b9799256-5c5e-4eb2-aa06-222dd11ec397.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/ba4c2648-2b56-4773-bcc1-d120fb61c5ee.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/ba76f7d9-56f7-481b-b4d9-eb3abf1bba87.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/bb0564aa-2ffb-4ed4-9cbc-4d52dd2ba8f8.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/bc990a02-844d-4567-afc8-796c9a783d9a.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/bf848809-2a6f-47a1-a577-df196b0bfb3f.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/bf86b6b6-4b53-4df5-97ff-46b0b360c479.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/bf9bafed-ac81-48f3-a1d6-8cb6da4ec4e4.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/c0b3ff53-b2fb-4491-88de-72e403c38ab0.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/c6465676-7517-4c86-9e4f-7c30124466bc.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/c74ae9a8-9575-4547-8abe-847d1f9b3069.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/cc0d63d5-8eb2-483e-96fe-4b83e85590da.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/cc75761c-f7fa-4ef7-ab45-89b7565407af.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/cdf113bb-2180-4a1d-9653-ee4883d04fc7.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/ce25bc63-c876-4e76-b450-5e28a9797872.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/cf98e5d9-b9d5-42b7-a7d6-da00d4559396.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/d0b25f98-b46d-4382-ba64-6ca679855b9e.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/d0d6c52e-245d-4f96-a6f7-dbcf87c8decc.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/d0f54959-f396-4a81-a38b-a6ba24f84080.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/d12464cf-a451-4df5-a09b-5d2af5140bc1.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/d270ac27-8630-4d5b-b3b1-6065f0e867e9.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/da9c7039-2d34-41dc-92c8-b3517a11f0f4.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/de9aa01a-90b7-48f7-a5e8-012251ffa1c3.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/e0d854ec-7dce-4f33-8dd6-cb57295ef64c.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/e147866c-3ff8-4aca-b800-c261b11b00b3.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/e3447890-be9f-4629-973d-d3dedb6d17e8.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/e4699552-fafd-4638-aecf-13c4bed11d45.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/e85a8629-0ad9-49d5-854c-df41ba0d8494.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/eacb2d8a-2a61-4083-a03e-ee589bfcc537.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/ec1c02ec-ddee-4de7-8464-ff250fcf3198.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/ef3e0a3c-f2fe-4380-9312-e4046fbffeb0.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/f03b08df-c1a2-4bdf-80a1-ebc3600809bd.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/f5977678-a85b-4220-9c65-147379b4e6a5.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/f5fd0396-9a72-45b6-b8ac-be6734015435.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/f89315b8-1d5d-466a-a392-38acf798e93b.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/f8b5c733-0e75-441a-ad05-0ff33ee91209.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/fa9c66bd-0dc0-4cfb-ad0b-845a2925da47.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/fbd1c64b-e0de-4a71-af3a-aa383b08a8c4.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/fc502fc8-884d-46ea-a507-e614d0787d9e.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/fcd648d8-b16d-428c-9803-39ee7e26e49f.root',
                                  'file:/eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000/fd31e4af-ba71-47e2-ad6f-665285cc56c8.root',
),
)

process.source.bypassVersionCheck = cms.untracked.bool(True)

#process.load("ALCARECOPPSCalTrackBasedSel_cff")

process.load("CalibPPS.TimingCalibration.ppsTimingCalibrationPCLWorker_cfi")
process.DQMStore = cms.Service("DQMStore")

process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string("testoutput.root")
)

process.load("CalibPPS.TimingCalibration.ALCARECOPromptCalibProdPPSTimingCalib_cff")

process.ctppsPixelDigis.inputLabel = "hltPPSCalibrationRaw"
process.ctppsDiamondRawToDigi.rawDataTag = "hltPPSCalibrationRaw"
process.totemRPRawToDigi.rawDataTag = "hltPPSCalibrationRaw"
process.totemTimingRawToDigi.rawDataTag = "hltPPSCalibrationRaw"
process.ctppsDiamondRecHits.digiTag = cms.InputTag("ctppsDiamondRawToDigiAlCaRecoProducer", "TimingDiamond")

# define the HLT base path                                                                                                                                                                                 
from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel as _hlt
process.ALCARECOPPSCalTrackBasedSelHLT = _hlt.clone(
    andOr = True,
    #HLTPaths = ['HLT_EphemeralZeroBias_v*'],
    HLTPaths = ['HLT_PPSMaxTracks*'],
    #eventSetupPathKey = 'SiStripCalZeroBias', # in case we have a proper base key                                                                                                                         
    throw = False
)

# select events passing the filter on pixel tracks                                                                                                                                                         
#from HLTrigger.special.hltPPSPerPotTrackFilter_cfi import hltPPSPerPotTrackFilter as _filter
#process.hltPPSPerPotTrackFilter_45 = _filter.clone(
#    pixelFilter = cms.VPSet(
#        cms.PSet( # sector 45, near pot                                                                                                                                                                  #  
#            detid = cms.uint32(2022703104),
#            minTracks = cms.int32(0),
#            maxTracks = cms.int32(1000),
#        ),
#        cms.PSet( # sector 45, far pot                                                                                                                                                                   #  
#            detid = cms.uint32(2023227392),
#            minTracks = cms.int32(1),
#            maxTracks = cms.int32(4),
#        ),
#    )
#)
#process.hltPPSPerPotTrackFilter_45.
#process.hltPPSPerPotTrackFilter_56 = _filter.clone(
#    pixelFilter = cms.VPSet(
#        cms.PSet( # sector 56, near pot                                                                                                                                                                  #  
#            detid = cms.uint32(2039480320),
#            minTracks = cms.int32(0),
#            maxTracks = cms.int32(1000),
#        ),
#        cms.PSet( # sector 56, far pot                                                                                                                                                                   #  
#            detid = cms.uint32(2040004608),
#            minTracks = cms.int32(1),
#            maxTracks = cms.int32(4),
#        ),
#    )
#)



#process.ppsTimingCalibrationPCLWorker.diamondRecHitTags = cms.InputTag("ctppsDiamondRecHits","","PPSTiming2")
process.ppsTimingCalibrationPCLWorker.diamondRecHitTags=cms.VInputTag(cms.InputTag("ctppsDiamondRecHits","","PPSTiming2"))

process.path = cms.Path(
    #process.a1* 
    #process.ctppsRawToDigi *
    process.ctppsDiamondRecHits *
    process.recoCTPPS *
    process.ALCARECOPPSCalTrackBasedSelHLT *
    #(process.hltPPSPerPotTrackFilter_45 + process.hltPPSPerPotTrackFilter_56)*
    #process.seqALCARECOPPSCalTrackBasedSel*
    process.ppsTimingCalibrationPCLWorker
    )

process.end_path = cms.EndPath(
    process.dqmOutput
)

process.schedule = cms.Schedule(
    process.path,
    process.end_path
)
