# coding=utf-8
from abaqus import *
from abaqusConstants import *
import MaterialManager

class AbacusCommands():
    def __init__(self):
        self.indentationDepth = 0.4

    def createSpecimen(self, gripLength, gripWidth, gageLength, gageWidth, radius, thickness):
        #print(gripLength, gripWidth, gageLength, gageWidth, radius)

        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                                    sheetSize=400.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)

        s.rectangle(point1=(0.0, gripWidth), point2=(gripLength, 0.0))  #left grip
        s.rectangle(point1=(gripLength+10.0, gripWidth-(gripWidth-gageWidth)/2),
                    point2=(gripLength+10.0+gageLength, (gripWidth-gageWidth)/2)) #gage
        s.rectangle(point1=(gripLength+10.0+gageLength+10, gripWidth),
                    point2=(gripLength+10.0+gageLength+10+gripLength, 0.0))

      #  s.ArcByStartEndTangent(point1=(50.0, 15.0), point2=(40.0, 20.0), vector=(-0.5, -0.5))
      #  s.ArcByStartEndTangent(point1=(50.0, 5.0), point2=(40.0, 0.0), vector=(-0.5, 0.5))
      #  s.ArcByStartEndTangent(point1=(125.0, 5.0), point2=(135.0, 0.0), vector=(150, -1.0))
      #  s.ArcByStartEndTangent(point1=(125.0, 15.0), point2=(135.0, 20.0), vector=(150, 10.0))


        s.ArcByStartEndTangent(point1=(gripLength+10.0, gripWidth-(gripWidth-gageWidth)/2),
                               point2=(gripLength, gripWidth), vector=(-150.0, 10.0))

        s.ArcByStartEndTangent(point1=(gripLength + 10.0, (gripWidth-gageWidth)/2),
                               point2=(gripLength, 0.0), vector=(-150, 10.0))

        s.ArcByStartEndTangent(point1=(gripLength+10.0+gageLength, gripWidth-(gripWidth-gageWidth)/2),
                               point2=(gripLength+10.0+gageLength+10, gripWidth), vector=(150, -1.0))

        s.ArcByStartEndTangent(point1=(gripLength + 10.0 + gageLength, (gripWidth - gageWidth) / 2),
                               point2=(gripLength + 10.0 + gageLength + 10, 0.0), vector=(150, 10.0))

        s.RadialDimension(curve=g[12], textPoint=(50.0, 27.5), radius=radius)
        s.RadialDimension(curve=g[13], textPoint=(50.0, -7.5), radius=radius)
        s.RadialDimension(curve=g[14], textPoint=(125.0, -7.5), radius=radius)
        s.RadialDimension(curve=g[15], textPoint=(125.0, 27.5), radius=radius)

       # s.ArcByStartEndTangent(point1=(gripLength+10.0, 15.0), point2=(gripLength, gripWidth), entity=g[8])


        s.delete(objectList=(g[6],))
        s.delete(objectList=(g[4],))
        s.delete(objectList=(g[8],))
        s.delete(objectList=(g[10],))

        p = mdb.models['Model-1'].Part(name='Specimen', dimensionality=TWO_D_PLANAR,
                                       type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Specimen']
        p.BaseShell(sketch=s)
        s.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Specimen']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']

        #RP
        p = mdb.models['Model-1'].parts['Specimen']
        v1, e1, d1, n1 = p.vertices, p.edges, p.datums, p.nodes
        p.ReferencePoint(point=p.InterestingPoint(edge=e1[1], rule=MIDDLE))

        #material dodac inne mateialy
        m = MaterialManager.MaterialManager()
        m.addExampleMaterial()

        #surface
        p = mdb.models['Model-1'].parts['Specimen']
        s = p.edges
        side1Edges = s.getSequenceFromMask(mask=('[#80 ]',), )
        p.Surface(side1Edges=side1Edges, name='right')
        p = mdb.models['Model-1'].parts['Specimen']
        s = p.edges
        side1Edges = s.getSequenceFromMask(mask=('[#2 ]',), )
        p.Surface(side1Edges=side1Edges, name='left')

        #section  poprawić na nowe materiały
        mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1',
                                                      material='AISI 1005 Steel', thickness=thickness)
        p = mdb.models['Model-1'].parts['Specimen']
        f = p.faces
        faces = f.getSequenceFromMask(mask=('[#1 ]',), )
        region = p.Set(faces=faces, name='Set-1')
        p = mdb.models['Model-1'].parts['Specimen']
        p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)


        #parition
        p = mdb.models['Model-1'].parts['Specimen']
        f = p.faces
        pickedFaces = f.getSequenceFromMask(mask=('[#1 ]',), )
        v2, e, d = p.vertices, p.edges, p.datums
        p.PartitionFaceByShortestPath(point1=v2[0], point2=v2[3], faces=pickedFaces)
        p = mdb.models['Model-1'].parts['Specimen']
        f = p.faces
        pickedFaces = f.getSequenceFromMask(mask=('[#1 ]',), )
        v1, e1, d2 = p.vertices, p.edges, p.datums
        p.PartitionFaceByShortestPath(point1=v1[9], point2=v1[2], faces=pickedFaces)
        p = mdb.models['Model-1'].parts['Specimen']
        f = p.faces
        pickedFaces = f.getSequenceFromMask(mask=('[#1 ]',), )
        v2, e, d = p.vertices, p.edges, p.datums
        p.PartitionFaceByShortestPath(point1=v2[7], point2=v2[2], faces=pickedFaces)
        p = mdb.models['Model-1'].parts['Specimen']
        f = p.faces
        pickedFaces = f.getSequenceFromMask(mask=('[#1 ]',), )
        v1, e1, d2 = p.vertices, p.edges, p.datums
        p.PartitionFaceByShortestPath(point1=v1[5], point2=v1[2], faces=pickedFaces)

    def assemblyStep(self, displacement):


        a = mdb.models['Model-1'].rootAssembly
        a.DatumCsysByDefault(CARTESIAN)
        p = mdb.models['Model-1'].parts['Specimen']
        a.Instance(name='Specimen-1', part=p, dependent=ON)

        mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', maxNumInc=100, minInc=1e-005, maxInc=1.0)

        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Specimen-1'].edges
        edges1 = e1.getSequenceFromMask(mask=('[#4000 ]',), )
        region = a.Set(edges=edges1, name='Set-1')
        mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Step-1',
                                             region=region, u1=0.0, u2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF,
                                             distributionType=UNIFORM, fieldName='', localCsys=None)
        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Specimen-1'].edges
        edges1 = e1.getSequenceFromMask(mask=('[#4 ]',), )
        region = a.Set(edges=edges1, name='Set-2')
        mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1',
                                             region=region, u1=displacement, u2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF,
                                             distributionType=UNIFORM, fieldName='', localCsys=None)


    def mesh(self):

        p = mdb.models['Model-1'].parts['Specimen']

        p = mdb.models['Model-1'].parts['Specimen']
        p.seedPart(size=10.0, deviationFactor=0.1, minSizeFactor=0.1)


        p = mdb.models['Model-1'].parts['Specimen']
        p.generateMesh()
        a = mdb.models['Model-1'].rootAssembly
        a.regenerate()

    def job(self):
        mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
                atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
                memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
                explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
                modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
                scratch='', resultsFormat=ODB)




