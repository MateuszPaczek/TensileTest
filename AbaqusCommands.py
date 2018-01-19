# coding=utf-8
from abaqus import *
from abaqusConstants import *

import MaterialManager


######################################

# odległość przy łuku
# mesh 3d
#

# długosc próbki
# dane z pliku
# dr Paćko
# normy literatura
#

######################################

class AbacusCommands:
    def createSpecimen2D(self, overallLength, gripLength, gripWidth, gageLength, gageWidth, radius, thickness):
        # print(gripLength, gripWidth, gageLength, gageWidth, radius)

        space = (overallLength - 2 * gripLength - gageLength)/2

        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                                    sheetSize=400.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)

        s.rectangle(point1=(0.0, gripWidth), point2=(gripLength, 0.0))  # left grip
        s.rectangle(point1=(gripLength + space, gripWidth - (gripWidth - gageWidth) / 2),
                    point2=(gripLength + space + gageLength, (gripWidth - gageWidth) / 2))  # gage
        s.rectangle(point1=(gripLength + space + gageLength + space, gripWidth),
                    point2=(gripLength + space + gageLength + space + gripLength, 0.0))

        #  s.ArcByStartEndTangent(point1=(50.0, 15.0), point2=(40.0, 20.0), vector=(-0.5, -0.5))
        #  s.ArcByStartEndTangent(point1=(50.0, 5.0), point2=(40.0, 0.0), vector=(-0.5, 0.5))
        #  s.ArcByStartEndTangent(point1=(125.0, 5.0), point2=(135.0, 0.0), vector=(150, -1.0))
        #  s.ArcByStartEndTangent(point1=(125.0, 15.0), point2=(135.0, 20.0), vector=(150, 10.0))

        s.ArcByStartEndTangent(point1=(gripLength + space, gripWidth - (gripWidth - gageWidth) / 2),
                               point2=(gripLength, gripWidth), vector=(-150.0, space))

        s.ArcByStartEndTangent(point1=(gripLength + space, (gripWidth - gageWidth) / 2),
                               point2=(gripLength, 0.0), vector=(-150, 10.0))

        s.ArcByStartEndTangent(point1=(gripLength + space + gageLength, gripWidth - (gripWidth - gageWidth) / 2),
                               point2=(gripLength + space + gageLength + space, gripWidth), vector=(150, -1.0))

        s.ArcByStartEndTangent(point1=(gripLength + space + gageLength, (gripWidth - gageWidth) / 2),
                               point2=(gripLength + space + gageLength + space, 0.0), vector=(150, 10.0))
        if radius != 0:
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

        del mdb.models['Model-1'].sketches['__profile__']

        # RP
        p = mdb.models['Model-1'].parts['Specimen']
        v1, e1, d1, n1 = p.vertices, p.edges, p.datums, p.nodes
        p.ReferencePoint(point=p.InterestingPoint(edge=e1[1], rule=MIDDLE))

        # material dodac inne mateialy
        m = MaterialManager.MaterialManager()
        m.addExampleMaterial()

        # surface
        p = mdb.models['Model-1'].parts['Specimen']
        s = p.edges
        side1Edges = s.getSequenceFromMask(mask=('[#80 ]',), )
        p.Surface(side1Edges=side1Edges, name='right')
        p = mdb.models['Model-1'].parts['Specimen']
        s = p.edges
        side1Edges = s.getSequenceFromMask(mask=('[#2 ]',), )
        p.Surface(side1Edges=side1Edges, name='left')

        # section  poprawić na nowe materiały
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

        # parition
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

    def assemblyStep2D(self, displacement):
        a = mdb.models['Model-1'].rootAssembly
        a.DatumCsysByDefault(CARTESIAN)
        p = mdb.models['Model-1'].parts['Specimen']
        a.Instance(name='Specimen-1', part=p, dependent=ON)

        mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', maxNumInc=100, minInc=1e-005, maxInc=1.0)

        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Specimen-1'].edges
        edges1 = e1.getSequenceFromMask(mask=('[#4000 ]',), )
        region = a.Set(edges=edges1, name='Set-1')
        mdb.models['Model-1'].DisplacementBC(name='bottom', createStepName='Step-1',
                                             region=region, u1=0.0, u2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF,
                                             distributionType=UNIFORM, fieldName='', localCsys=None)
        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Specimen-1'].edges
        edges1 = e1.getSequenceFromMask(mask=('[#4 ]',), )
        region = a.Set(edges=edges1, name='Set-2')
        mdb.models['Model-1'].DisplacementBC(name='top', createStepName='Step-1',
                                             region=region, u1=displacement, u2=0.0, ur3=0.0, amplitude=UNSET,
                                             fixed=OFF,
                                             distributionType=UNIFORM, fieldName='', localCsys=None)

    def mesh2D(self):
        p = mdb.models['Model-1'].parts['Specimen']
        p.seedPart(size=10.0, deviationFactor=0.1, minSizeFactor=0.1)

        p = mdb.models['Model-1'].parts['Specimen']
        p.generateMesh()
        a = mdb.models['Model-1'].rootAssembly
        a.regenerate()

    def job2D(self):
        mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
                atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
                memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
                explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
                modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
                scratch='', resultsFormat=ODB)

    # Axis
    def createSpecimenAxis(self, overallLength, gripLength, gripWidth, gageLength, gageWidth, radius):
        space = (overallLength - 2 * gripLength - gageLength) / 2
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                                    sheetSize=500.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.sketchOptions.setValues(viewStyle=AXISYM)
        s.setPrimaryObject(option=STANDALONE)
        s.ConstructionLine(point1=(0.0, -250.0), point2=(0.0, 250.0))
        s.FixedConstraint(entity=g[2])
        s.Line(point1=(0.0, 0.0), point2=(gripWidth / 2, 0.0))
        s.HorizontalConstraint(entity=g[3], addUndoState=False)
        s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
        s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
        s.Line(point1=(gripWidth / 2, 0.0), point2=(gripWidth / 2, gripLength))
        s.VerticalConstraint(entity=g[4], addUndoState=False)
        s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)

        s.Line(point1=(gageWidth / 2, gripLength + space), point2=(gageWidth / 2, gripLength + space + gageLength))
        s.VerticalConstraint(entity=g[5], addUndoState=False)
        s.Line(point1=(gripWidth / 2, gripLength + space + gageLength + space),
               point2=(gripWidth / 2, gripLength + space + gageLength + space + gripLength))
        s.VerticalConstraint(entity=g[6], addUndoState=False)
        s.Line(point1=(gripWidth / 2, gripLength + space + gageLength + space + gripLength),
               point2=(0.0, gripLength + space + gageLength + space + gripLength))
        s.HorizontalConstraint(entity=g[7], addUndoState=False)
        s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
        s.CoincidentConstraint(entity1=v[7], entity2=g[2], addUndoState=False)

        s.Line(point1=(0.0, gripLength + space + gageLength + space + gripLength), point2=(0.0, 0.0))
        s.VerticalConstraint(entity=g[8], addUndoState=False)
        s.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)

        s.ArcByStartEndTangent(point1=(gageWidth / 2, gripLength + space + gageLength),
                               point2=(gripWidth / 2, gripLength + space + gageLength + space), entity=g[5])
        s.ArcByStartEndTangent(point1=(gageWidth / 2, gripLength + space),
                               point2=(gripWidth / 2, gripLength), entity=g[5])
        if radius != 0:
            s.RadialDimension(curve=g[10], textPoint=(17.5, 105.0), radius=radius)
            s.RadialDimension(curve=g[9], textPoint=(17.5, 30.0), radius=radius)

        p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=AXISYMMETRIC,
                                       type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-1']
        p.BaseShell(sketch=s)
        s.unsetPrimaryObject()

        del mdb.models['Model-1'].sketches['__profile__']

        # material dodac inne mateialy
        m = MaterialManager.MaterialManager()
        m.addExampleMaterial()

        p = mdb.models['Model-1'].parts['Part-1']
        s = p.edges
        side1Edges = s.getSequenceFromMask(mask=('[#2 ]',), )
        p.Surface(side1Edges=side1Edges, name='bottom')

        p = mdb.models['Model-1'].parts['Part-1']
        s = p.edges
        side1Edges = s.getSequenceFromMask(mask=('[#80 ]',), )
        p.Surface(side1Edges=side1Edges, name='top')

        p = mdb.models['Model-1'].parts['Part-1']
        s = p.edges
        side1Edges = s.getSequenceFromMask(mask=('[#1 ]',), )
        p.Surface(side1Edges=side1Edges, name='symmetryLine')

        mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1',
                                                      material='AISI 1005 Steel')
        p = mdb.models['Model-1'].parts['Part-1']
        f = p.faces
        faces = f.getSequenceFromMask(mask=('[#1 ]',), )
        region = p.Set(faces=faces, name='Set-1')
        p = mdb.models['Model-1'].parts['Part-1']
        p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)

    def assemblyStepAxis(self, displacement):
        a = mdb.models['Model-1'].rootAssembly
        a.DatumCsysByThreePoints(coordSysType=CYLINDRICAL, origin=(0.0, 0.0, 0.0),
                                 point1=(1.0, 0.0, 0.0), point2=(0.0, 0.0, -1.0))
        p = mdb.models['Model-1'].parts['Part-1']
        a.Instance(name='Part-1-1', part=p, dependent=ON)

        mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', maxNumInc=100, minInc=1e-005, maxInc=1.0)

        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Part-1-1'].edges
        edges1 = e1.getSequenceFromMask(mask=('[#2 ]',), )
        region = a.Set(edges=edges1, name='Set-1')
        mdb.models['Model-1'].EncastreBC(name='Bottom', createStepName='Step-1',
                                         region=region, localCsys=None)
        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Part-1-1'].edges
        edges1 = e1.getSequenceFromMask(mask=('[#1 ]',), )
        region = a.Set(edges=edges1, name='Set-2')
        mdb.models['Model-1'].XsymmBC(name='Symmetric', createStepName='Step-1',
                                      region=region, localCsys=None)

        a = mdb.models['Model-1'].rootAssembly
        e1 = a.instances['Part-1-1'].edges
        edges1 = e1.getSequenceFromMask(mask=('[#80 ]',), )
        region = a.Set(edges=edges1, name='Set-3')
        mdb.models['Model-1'].DisplacementBC(name='top', createStepName='Step-1',
                                             region=region, u1=0.0, u2=displacement, ur3=0.0, amplitude=UNSET,
                                             fixed=OFF,
                                             distributionType=UNIFORM, fieldName='', localCsys=None)

    def meshAxis(self):
        p = mdb.models['Model-1'].parts['Part-1']
        p.seedPart(size=10.0, deviationFactor=0.1, minSizeFactor=0.1)
        p.generateMesh()

    def jobAxis(self):
        mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
                atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
                memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
                explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
                modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
                scratch='', resultsFormat=ODB)

    def createSpecimen3D(self, overallLength, gripLength, gripWidth, gageLength, gageWidth, radius, depth):

        space = (overallLength - 2 * gripLength - gageLength) / 2
        s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                                     sheetSize=500.0)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=STANDALONE)
        s1.rectangle(point1=(0.0, gripWidth), point2=(gripLength, 0.0))  # left grip
        s1.rectangle(point1=(gripLength + space, gripWidth - (gripWidth - gageWidth) / 2),
                     point2=(gripLength + space + gageLength, (gripWidth - gageWidth) / 2))  # gage
        s1.rectangle(point1=(gripLength + space + gageLength + space, gripWidth),
                     point2=(gripLength + space + gageLength + space + gripLength, 0.0))

        s1.delete(objectList=(g[6], g[8], g[10], g[4]))

        s1.ArcByStartEndTangent(point1=(gripLength + space, gripWidth - (gripWidth - gageWidth) / 2),
                                point2=(gripLength, gripWidth), vector=(-150.0, 10.0))

        s1.ArcByStartEndTangent(point1=(gripLength + space, (gripWidth - gageWidth) / 2),
                                point2=(gripLength, 0.0), vector=(-150, 10.0))

        s1.ArcByStartEndTangent(point1=(gripLength + space + gageLength, gripWidth - (gripWidth - gageWidth) / 2),
                                point2=(gripLength + space + gageLength + space, gripWidth), vector=(150, -1.0))

        s1.ArcByStartEndTangent(point1=(gripLength + space + gageLength, (gripWidth - gageWidth) / 2),
                                point2=(gripLength + space + gageLength + space, 0.0), vector=(150, 10.0))
        if radius != 0:
            s1.RadialDimension(curve=g[12], textPoint=(50.0, 27.5), radius=radius)
            s1.RadialDimension(curve=g[13], textPoint=(50.0, -7.5), radius=radius)
            s1.RadialDimension(curve=g[14], textPoint=(125.0, -7.5), radius=radius)
            s1.RadialDimension(curve=g[15], textPoint=(125.0, 27.5), radius=radius)

        p1 = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D,
                                        type=DEFORMABLE_BODY)
        p1 = mdb.models['Model-1'].parts['Part-1']
        p1.BaseSolidExtrude(sketch=s1, depth=depth)
        s1.unsetPrimaryObject()
        p1 = mdb.models['Model-1'].parts['Part-1']
        del mdb.models['Model-1'].sketches['__profile__']

        # material dodac inne mateialy
        m = MaterialManager.MaterialManager()
        m.addExampleMaterial()

        # surfaces
        p1 = mdb.models['Model-1'].parts['Part-1']
        s = p1.faces
        side1Faces = s.getSequenceFromMask(mask=('[#10 ]',), )
        p1.Surface(side1Faces=side1Faces, name='bottom')

        p1 = mdb.models['Model-1'].parts['Part-1']
        s = p1.faces
        side1Faces = s.getSequenceFromMask(mask=('[#400 ]',), )
        p1.Surface(side1Faces=side1Faces, name='top')

        # section
        mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1',
                                                      material='AISI 1005 Steel', thickness=None)
        p1 = mdb.models['Model-1'].parts['Part-1']
        c = p1.cells
        cells = c.getSequenceFromMask(mask=('[#1 ]',), )
        region = p1.Set(cells=cells, name='Set-1')
        p1 = mdb.models['Model-1'].parts['Part-1']
        p1.SectionAssignment(region=region, sectionName='Section-1', offset=0.0,
                             offsetType=MIDDLE_SURFACE, offsetField='',
                             thicknessAssignment=FROM_SECTION)

    def assemblyStep3D(self, displacement):
        a = mdb.models['Model-1'].rootAssembly
        a.DatumCsysByDefault(CARTESIAN)
        p = mdb.models['Model-1'].parts['Part-1']
        a.Instance(name='Part-1-1', part=p, dependent=ON)

        # step

        # default
        # mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')

        mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial',
                                         timePeriod=2.0, maxNumInc=1000, stabilizationMethod=NONE,
                                         continueDampingFactors=False, adaptiveDampingRatio=None,
                                         initialInc=1.0, minInc=2.1e-05, maxInc=2.0, matrixSolver=ITERATIVE,
                                         matrixStorage=SOLVER_DEFAULT, solutionTechnique=FULL_NEWTON)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-1-1'].faces
        faces1 = f1.getSequenceFromMask(mask=('[#10 ]',), )
        region = a.Set(faces=faces1, name='Set-1')
        mdb.models['Model-1'].DisplacementBC(name='bottom', createStepName='Step-1',
                                             region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0,
                                             amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                             localCsys=None)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-1-1'].faces
        faces1 = f1.getSequenceFromMask(mask=('[#400 ]',), )
        region = a.Set(faces=faces1, name='Set-2')
        mdb.models['Model-1'].DisplacementBC(name='top', createStepName='Step-1',
                                             region=region, u1=-displacement, u2=0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0,
                                             amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                             localCsys=None)

    def mesh3D(self):
        p1 = mdb.models['Model-1'].parts['Part-1']
        p1.seedPart(size=7.5, deviationFactor=0.1, minSizeFactor=0.1)
        p1 = mdb.models['Model-1'].parts['Part-1']
        p1.generateMesh()
        a = mdb.models['Model-1'].rootAssembly
        a.regenerate()

    def job3D(self):
        mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
                atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
                memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
                explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
                modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
                scratch='', resultsFormat=ODB)

    def createSpecimenCylinder(self, overallLength, gripLength, gripWidth, gageLength, gageWidth, radius):
        space = (overallLength - 2 * gripLength - gageLength) / 2
        s1 = mdb.models['Model-1'].ConstrainedSketch(name='__sweep__', sheetSize=200.0)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=STANDALONE)
        s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(-10.0, 0.0))
        s1.unsetPrimaryObject()
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                                    sheetSize=200.0,
                                                    transform=(-1.0, -1.22464679914735e-16, 0.0, 0.0, 0.0,
                                                               1.0, -1.22464679914735e-16, 1.0, 0.0, -10.0,
                                                               1.22464679914735e-15,
                                                               0.0))
        g1, v1, d1, c1 = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=SUPERIMPOSE)
        s.ConstructionLine(point1=(-100.0, 0.0), point2=(100.0, 0.0))
        s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))

        s.Line(point1=(10.0, 0.0), point2=(10.0, gageLength / 2 + space + gripLength))
        s.VerticalConstraint(entity=g1[4], addUndoState=False)
        s.PerpendicularConstraint(entity1=g1[2], entity2=g1[4], addUndoState=False)
        s.CoincidentConstraint(entity1=v1[0], entity2=g1[2], addUndoState=False)

        s.Line(point1=(10.0, gageLength / 2 + space + gripLength),
               point2=(10 + gripWidth / 2, gageLength / 2 + space + gripLength))
        s.HorizontalConstraint(entity=g1[5], addUndoState=False)
        s.PerpendicularConstraint(entity1=g1[4], entity2=g1[5], addUndoState=False)
        s.Line(point1=(10 + gripWidth / 2, gageLength / 2 + space + gripLength),
               point2=(10 + gripWidth / 2, gageLength / 2 + space))
        s.VerticalConstraint(entity=g1[6], addUndoState=False)
        s.PerpendicularConstraint(entity1=g1[5], entity2=g1[6], addUndoState=False)

        s.Line(point1=(10.0, 0.0), point2=(10 + gageWidth / 2, 0.0))
        s.HorizontalConstraint(entity=g1[7], addUndoState=False)
        s.PerpendicularConstraint(entity1=g1[4], entity2=g1[7], addUndoState=False)

        s.Line(point1=(10 + gageWidth / 2, 0.0), point2=(10 + gageWidth / 2, gageLength / 2))
        s.VerticalConstraint(entity=g1[8], addUndoState=False)
        s.PerpendicularConstraint(entity1=g1[7], entity2=g1[8], addUndoState=False)
        s.ArcByStartEndTangent(point1=(10 + gageWidth / 2, gageLength / 2),
                               point2=(10 + gripWidth / 2, gageLength / 2 + space), entity=g1[8])

        s.copyMirror(mirrorLine=g1[2], objectList=(g1[2], g1[4], g1[5], g1[6], g1[7],
                                                   g1[8], g1[9]))

        s.move(vector=(-20.0, 0.0), objectList=(g1[2], g1[4], g1[5], g1[6], g1[7],
                                                g1[8], g1[9], g1[10], g1[11], g1[12], g1[13], g1[14], g1[15], g1[16]))

        s.delete(objectList=(g1[2], g1[7], g1[10], g1[14], c1[17], c1[42]))

        p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D,
                                       type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['Part-1']
        p.BaseSolidSweep(sketch=s, path=s1)
        s.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['Part-1']

        del mdb.models['Model-1'].sketches['__profile__']
        del mdb.models['Model-1'].sketches['__sweep__']

        # material dodac inne mateialy
        m = MaterialManager.MaterialManager()
        m.addExampleMaterial()

        mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1',
                                                      material='AISI 1005 Steel', thickness=None)
        p = mdb.models['Model-1'].parts['Part-1']
        c = p.cells
        cells = c.getSequenceFromMask(mask=('[#1 ]',), )
        region = p.Set(cells=cells, name='Set-1')
        p = mdb.models['Model-1'].parts['Part-1']
        p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)

    def assemblyStepCylinder(self, displacement):
        a = mdb.models['Model-1'].rootAssembly
        a.DatumCsysByDefault(CARTESIAN)
        p = mdb.models['Model-1'].parts['Part-1']
        a.Instance(name='Part-1-1', part=p, dependent=ON)

        mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-1-1'].faces
        faces1 = f1.getSequenceFromMask(mask=('[#40 ]',), )
        region = a.Set(faces=faces1, name='Set-1')
        mdb.models['Model-1'].DisplacementBC(name='bottom', createStepName='Step-1',
                                             region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0,
                                             amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                             localCsys=None)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['Part-1-1'].faces
        faces1 = f1.getSequenceFromMask(mask=('[#1 ]',), )
        region = a.Set(faces=faces1, name='Set-2')
        mdb.models['Model-1'].DisplacementBC(name='top', createStepName='Step-1',
                                             region=region, u1=0, u2=0.0, u3=-displacement, ur1=0.0, ur2=0.0, ur3=0.0,
                                             amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                             localCsys=None)

    def meshCylinder(self):
        import mesh
        p = mdb.models['Model-1'].parts['Part-1']
        c = p.cells
        pickedRegions = c.getSequenceFromMask(mask=('[#1 ]',), )
        p.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
        elemType1 = mesh.ElemType(elemCode=C3D20R)
        elemType2 = mesh.ElemType(elemCode=C3D15)
        elemType3 = mesh.ElemType(elemCode=C3D10)
        p = mdb.models['Model-1'].parts['Part-1']
        c = p.cells
        cells = c.getSequenceFromMask(mask=('[#1 ]',), )
        pickedRegions = (cells,)
        p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,
                                                           elemType3))
        p = mdb.models['Model-1'].parts['Part-1']
        p.seedPart(size=4.0, deviationFactor=0.1, minSizeFactor=0.1)
        p = mdb.models['Model-1'].parts['Part-1']
        p.generateMesh()

    def jobCylinder(self):
        mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
                atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
                memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
                explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
                modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
                scratch='', resultsFormat=ODB)
