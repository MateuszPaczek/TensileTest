from abaqus import *
from abaqusConstants import *
import MaterialManager

class AbacusCommands():
    def __init__(self):
        self.indentationDepth = 0.4

    def createSpecimen(self, gripLength, gripWidth, gageLength, gageWidth, radius, thickness):
        print(gripLength, gripWidth, gageLength, gageWidth, radius)

        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                                    sheetSize=400.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.rectangle(point1=(0.0, gripWidth), point2=(gripLength, 0.0))  #left grip

        s.rectangle(point1=(gripLength+10.0, gripWidth-(gripWidth-gageWidth)/2), point2=(gripLength+10.0+gageLength, (gripWidth-gageWidth)/2)) #gage

        s.rectangle(point1=(gripLength+10.0+gageLength+10, gripWidth), point2=(gripLength+10.0+gageLength+10+gripLength, 0.0))

      #  s.ArcByStartEndTangent(point1=(50.0, 15.0), point2=(40.0, 20.0), vector=(-0.5, -0.5))
      #  s.ArcByStartEndTangent(point1=(50.0, 5.0), point2=(40.0, 0.0), vector=(-0.5, 0.5))
      #  s.ArcByStartEndTangent(point1=(125.0, 5.0), point2=(135.0, 0.0), vector=(150, -1.0))
      #  s.ArcByStartEndTangent(point1=(125.0, 15.0), point2=(135.0, 20.0), vector=(150, 10.0))



        s.ArcByStartEndTangent(point1=(gripLength+10.0, gripWidth-(gripWidth-gageWidth)/2),
                               point2=(gripLength, gripWidth), vector=(-150.0, -1.0))

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

    #    s.RadialDimension(curve=g[12], textPoint=(38.0411643981934, 10.0), radius=12.5)
    #    s.RadialDimension(curve=g[13], textPoint=(38.0411643981934, -10.0), radius=12.5)
    #    s.RadialDimension(curve=g[14], textPoint=(138.0411643981934, 10.0), radius=12.5)
    #    s.RadialDimension(curve=g[15], textPoint=(138.0411643981934, -10.0), radius=12.5)

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

        #material
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

        #section
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






