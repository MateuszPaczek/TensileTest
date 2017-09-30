from Tkinter import *
import ttk

import AbaqusCommands


def TensileFunction():
    class GuiApplication:
        def __init__(self):
            self.master = Tk()
            self.notebook = ttk.Notebook(self.master)

            self.tab2D = ttk.Frame(self.notebook)
            self.tab3D = ttk.Frame(self.notebook)
            self.tabAxis = ttk.Frame(self.notebook)
            self.notebook.add(self.tab2D, text="2D model")
            self.notebook.add(self.tabAxis, text="Axisymmetric")
            self.notebook.add(self.tab3D, text="3D model")

            self.notebook.pack()

            self.abaqus = AbaqusCommands.AbacusCommands()

            self.vfaz = (self.tab3D.register(self.specimen_dimension_validate),
                         '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

            self.upperFrame2D = ttk.Frame(self.tab2D)
            self.middleFrame2D = ttk.Frame(self.tab2D)

            self.upperFrame2D.grid(row=0, column=0)
            self.middleFrame2D.grid(row=1, column=0)

            self.gripLength2D = StringVar()
            self.gripWidth2D = StringVar()
            self.gageLength2D = StringVar()
            self.gageWidth2D = StringVar()
            self.radius2D = StringVar()
            self.thickness2D = StringVar()
            self.displacement2D = StringVar()
            self.displacement2D.set("10.0")

            self.gripLength2DLabel = ttk.Label(self.upperFrame2D, text="Grip length")
            self.gripLength2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                               textvariable=self.gripLength2D)

            self.gripWidth2DLabel = ttk.Label(self.upperFrame2D, text="Grip width")
            self.gripWidth2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                              textvariable=self.gripWidth2D)

            self.gageLength2DLabel = ttk.Label(self.upperFrame2D, text="Gage length")
            self.gageLength2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                               textvariable=self.gageLength2D)

            self.gageWidth2DLabel = ttk.Label(self.upperFrame2D, text="Gage width")
            self.gageWidth2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                              textvariable=self.gageWidth2D)

            self.radius2DLabel = ttk.Label(self.upperFrame2D, text="Radius")
            self.radius2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                           textvariable=self.radius2D)

            self.thickness2DLabel = ttk.Label(self.upperFrame2D, text="Thickness")
            self.thickness2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                              textvariable=self.thickness2D)

            self.displacement2DLabel = ttk.Label(self.upperFrame2D, text="Displacement")
            self.displacement2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                                 textvariable=self.displacement2D)

            self.gripLength2DLabel.grid(row=0, column=0)
            self.gripLength2DEntry.grid(row=0, column=1)
            self.gripWidth2DLabel.grid(row=1, column=0)
            self.gripWidth2DEntry.grid(row=1, column=1)
            self.gageLength2DLabel.grid(row=3, column=0)
            self.gageLength2DEntry.grid(row=3, column=1)
            self.gageWidth2DLabel.grid(row=4, column=0)
            self.gageWidth2DEntry.grid(row=4, column=1)
            self.radius2DLabel.grid(row=5, column=0)
            self.radius2DEntry.grid(row=5, column=1)
            self.thickness2DLabel.grid(row=6, column=0)
            self.thickness2DEntry.grid(row=6, column=1)
            self.displacement2DLabel.grid(row=0, column=3)
            self.displacement2DEntry.grid(row=0, column=4)

            self.buttonDone = Button(self.upperFrame2D, text="Go", command=self.done2D)
            self.buttonExample = Button(self.upperFrame2D, text="Create example", command=self.example2D)
            self.buttonDone.grid()
            self.buttonExample.grid()

            # Axisimmetric

            self.upperFrameAxis = ttk.Frame(self.tabAxis)
            self.middleFrameAxis = ttk.Frame(self.tabAxis)

            self.upperFrameAxis.grid(row=0, column=0)
            self.middleFrameAxis.grid(row=1, column=0)

            self.gripLengthAxis = StringVar()
            self.gripWidthAxis = StringVar()
            self.gageLengthAxis = StringVar()
            self.gageWidthAxis = StringVar()
            self.radiusAxis = StringVar()
            self.displacementAxis = StringVar()
            self.displacementAxis.set("10.0")

            self.gripLengthAxisLabel = ttk.Label(self.upperFrameAxis, text="Grip length")
            self.gripLengthAxisEntry = ttk.Entry(self.upperFrameAxis, validate='key', validatecommand=self.vfaz,
                                                 textvariable=self.gripLengthAxis)

            self.gripWidthAxisLabel = ttk.Label(self.upperFrameAxis, text="Grip width")
            self.gripWidthAxisEntry = ttk.Entry(self.upperFrameAxis, validate='key', validatecommand=self.vfaz,
                                                textvariable=self.gripWidthAxis)

            self.gageLengthAxisLabel = ttk.Label(self.upperFrameAxis, text="Gage length")
            self.gageLengthAxisEntry = ttk.Entry(self.upperFrameAxis, validate='key', validatecommand=self.vfaz,
                                                 textvariable=self.gageLengthAxis)

            self.gageWidthAxisLabel = ttk.Label(self.upperFrameAxis, text="Gage width")
            self.gageWidthAxisEntry = ttk.Entry(self.upperFrameAxis, validate='key', validatecommand=self.vfaz,
                                                textvariable=self.gageWidthAxis)

            self.radiusAxisLabel = ttk.Label(self.upperFrameAxis, text="Radius")
            self.radiusAxisEntry = ttk.Entry(self.upperFrameAxis, validate='key', validatecommand=self.vfaz,
                                             textvariable=self.radiusAxis)

            self.displacementAxisLabel = ttk.Label(self.upperFrameAxis, text="Displacement")
            self.displacementAxisEntry = ttk.Entry(self.upperFrameAxis, validate='key', validatecommand=self.vfaz,
                                                   textvariable=self.displacementAxis)

            self.gripLengthAxisLabel.grid(row=0, column=0)
            self.gripLengthAxisEntry.grid(row=0, column=1)
            self.gripWidthAxisLabel.grid(row=1, column=0)
            self.gripWidthAxisEntry.grid(row=1, column=1)
            self.gageLengthAxisLabel.grid(row=3, column=0)
            self.gageLengthAxisEntry.grid(row=3, column=1)
            self.gageWidthAxisLabel.grid(row=4, column=0)
            self.gageWidthAxisEntry.grid(row=4, column=1)
            self.radiusAxisLabel.grid(row=5, column=0)
            self.radiusAxisEntry.grid(row=5, column=1)
            self.displacementAxisLabel.grid(row=0, column=3)
            self.displacementAxisEntry.grid(row=0, column=4)

            self.buttonDone = Button(self.upperFrameAxis, text="Go", command=self.doneAxis)
            self.buttonExample = Button(self.upperFrameAxis, text="Create example", command=self.exampleAxis)
            self.buttonDone.grid()
            self.buttonExample.grid()

            # 3D

            self.upperFrame3D = ttk.Frame(self.tab3D)
            self.middleFrame3D = ttk.Frame(self.tab3D)

            self.upperFrame3D.grid(row=0, column=0)
            self.middleFrame3D.grid(row=1, column=0)

            self.gripLength3D = StringVar()
            self.gripWidth3D = StringVar()
            self.gageLength3D = StringVar()
            self.gageWidth3D = StringVar()
            self.radius3D = StringVar()
            self.depth3D = StringVar()
            self.displacement3D = StringVar()
            self.displacement3D.set("10.0")

            self.gripLength3DLabel = ttk.Label(self.upperFrame3D, text="Grip length")
            self.gripLength3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                                 textvariable=self.gripLength3D)

            self.gripWidth3DLabel = ttk.Label(self.upperFrame3D, text="Grip width")
            self.gripWidth3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                                textvariable=self.gripWidth3D)

            self.gageLength3DLabel = ttk.Label(self.upperFrame3D, text="Gage length")
            self.gageLength3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                                 textvariable=self.gageLength3D)

            self.gageWidth3DLabel = ttk.Label(self.upperFrame3D, text="Gage width")
            self.gageWidth3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                                textvariable=self.gageWidth3D)

            self.radius3DLabel = ttk.Label(self.upperFrame3D, text="Radius")
            self.radius3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                             textvariable=self.radius3D)

            self.depth3DLabel = ttk.Label(self.upperFrame3D, text="Depth")
            self.depth3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                             textvariable=self.depth3D)

            self.displacement3DLabel = ttk.Label(self.upperFrame3D, text="Displacement")
            self.displacement3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                                   textvariable=self.displacement3D)

            self.gripLength3DLabel.grid(row=0, column=0)
            self.gripLength3DEntry.grid(row=0, column=1)
            self.gripWidth3DLabel.grid(row=1, column=0)
            self.gripWidth3DEntry.grid(row=1, column=1)
            self.gageLength3DLabel.grid(row=3, column=0)
            self.gageLength3DEntry.grid(row=3, column=1)
            self.gageWidth3DLabel.grid(row=4, column=0)
            self.gageWidth3DEntry.grid(row=4, column=1)
            self.radius3DLabel.grid(row=5, column=0)
            self.radius3DEntry.grid(row=5, column=1)
            self.depth3DLabel.grid(row=6, column=0)
            self.depth3DEntry.grid(row=6, column=1)

            self.displacement3DLabel.grid(row=0, column=3)
            self.displacement3DEntry.grid(row=0, column=4)

            self.buttonDone = Button(self.upperFrame3D, text="Go", command=self.done3D)
            self.buttonExample = Button(self.upperFrame3D, text="Create example", command=self.example3D)
            self.buttonDone.grid()
            self.buttonExample.grid()
            mainloop()

        def specimen_dimension_validate(self, action, index, value_if_allowed,
                                        prior_value, text, validation_type, trigger_type, widget_name):
            if text in '0123456789.-+':
                try:
                    float(value_if_allowed)
                    if value_if_allowed <= 0.0:
                        return False
                    return True
                except ValueError:
                    if value_if_allowed == ' ' or value_if_allowed == '':
                        return True
                    return False
            else:
                return False

        def done2D(self):
            self.abaqus.createSpecimen2D(float(self.gripLength2D.get()), float(self.gripWidth2D.get()),
                                         float(self.gageLength2D.get()), float(self.gageWidth2D.get()),
                                         float(self.radius2D.get()), float(self.thickness2D.get()))
            self.abaqus.assemblyStep2D(float(self.displacement2D.get()))
            self.abaqus.mesh2D()
            self.abaqus.job2D()

        def doneAxis(self):
            self.abaqus.createSpecimenAxis(float(self.gripLengthAxis.get()), float(self.gripWidthAxis.get()),
                                           float(self.gageLengthAxis.get()), float(self.gageWidthAxis.get()),
                                           float(self.radiusAxis.get()))
            self.abaqus.assemblyStepAxis(float(self.displacementAxis.get()))
            self.abaqus.meshAxis()
            self.abaqus.jobAxis()

        def done3D(self):
            self.abaqus.createSpecimen2D(float(self.gripLength3D.get()), float(self.gripWidth3D.get()),
                                         float(self.gageLength3D.get()), float(self.gageWidth3D.get()),
                                         float(self.radius3D.get()), float(self.depth3D.get()))
            self.abaqus.assemblyStep2D(float(self.displacement3D.get()))
            self.abaqus.mesh3D()
            self.abaqus.job3D()

        def example2D(self):
            self.abaqus.createSpecimen2D(40.0, 20.0, 75.0, 10.0, 12.5, 10)
            self.abaqus.assemblyStep2D(10.0)
            self.abaqus.mesh2D()
            self.abaqus.job2D()

        def exampleAxis(self):
            self.abaqus.createSpecimenAxis(40.0, 20.0, 75.0, 10.0, 12.5)
            self.abaqus.assemblyStepAxis(10.0)
            self.abaqus.meshAxis()
            self.abaqus.jobAxis()

        def example3D(self):
            self.abaqus.createSpecimen3D(40.0, 20.0, 75.0, 10.0, 12.5, 10)
            self.abaqus.assemblyStep3D(10.0)
            self.abaqus.mesh3D()
            self.abaqus.job3D()


    app = GuiApplication()


if __name__ == '__main__':
    TensileFunction()
