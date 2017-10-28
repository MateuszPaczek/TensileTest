from Tkinter import *
import ttk

import AbaqusCommands
import TestCommands

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def TensileFunction():
    class GuiApplication:
        def __init__(self):
            self.master = Tk()
            self.notebook = ttk.Notebook(self.master)

            self.tab2D = ttk.Frame(self.notebook)
            self.tab3D = ttk.Frame(self.notebook)
            self.tabAxis = ttk.Frame(self.notebook)
            self.tabCylinder = ttk.Frame(self.notebook)
            self.notebook.add(self.tab2D, text="Flat 2D")
            self.notebook.add(self.tab3D, text="Flat 3D")
            self.notebook.add(self.tabCylinder, text="Cylinder")
            self.notebook.add(self.tabAxis, text="Cylinder axisymmetric")

            self.notebook.pack()

            self.abaqus = AbaqusCommands.AbacusCommands()
            # self.abaqus = TestCommands.TestCommands()

            self.vfaz = (self.tab3D.register(self.specimen_dimension_validate),
                         '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')


            self.upperFrame2D = ttk.Frame(self.tab2D)
            self.imageFrame2D = ttk.Frame(self.tab2D)

            self.upperFrame2D.grid(row=1, column=0)
            self.imageFrame2D.grid(row=0, column=0)

            self.specimenImmage = PhotoImage(file=dir_path + "\\" + "tensile_specimen.gif")
            self.specimenImageLabel2D = ttk.Label(self.imageFrame2D, image=self.specimenImmage)
            self.specimenImageLabel2D.image = self.specimenImmage
            self.specimenImageLabel2D.grid()

            self.specimens2D = ( 'Test', 'PN EN ISO 6892-1 2009')
            self.specimenComboBox2D = ttk.Combobox(self.imageFrame2D, values=self.specimens2D,
                                                   textvariable=self.specimens2D)
            self.specimenComboBox2D.current(newindex=0)
            self.specimenComboBox2D.bind("<<ComboboxSelected>>", self.update_gui_on_selected_specimen2D)
            self.specimenComboBox2D.grid()

            self.overallLength2D = StringVar()
            self.gripLength2D = StringVar()
            self.gripWidth2D = StringVar()
            self.gageLength2D = StringVar()
            self.gageWidth2D = StringVar()
            self.radius2D = StringVar()
            self.thickness2D = StringVar()
            self.displacement2D = StringVar()
            self.displacement2D.set("10.0")

            self.overallLength2DLabel = ttk.Label(self.upperFrame2D, text="L0 - Overall length")
            self.overallLength2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                               textvariable=self.overallLength2D)

            self.gripLength2DLabel = ttk.Label(self.upperFrame2D, text="D - Grip tab length")
            self.gripLength2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                               textvariable=self.gripLength2D)

            self.gripWidth2DLabel = ttk.Label(self.upperFrame2D, text="W0 - Overall width")
            self.gripWidth2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                              textvariable=self.gripWidth2D)

            self.gageLength2DLabel = ttk.Label(self.upperFrame2D, text="L - Length of narrow section")
            self.gageLength2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                               textvariable=self.gageLength2D)

            self.gageWidth2DLabel = ttk.Label(self.upperFrame2D, text="Wc - Width of narrow section")
            self.gageWidth2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                              textvariable=self.gageWidth2D)

            self.radius2DLabel = ttk.Label(self.upperFrame2D, text="R - Radius")
            self.radius2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                           textvariable=self.radius2D)

            self.thickness2DLabel = ttk.Label(self.upperFrame2D, text="T - Thickness")
            self.thickness2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                              textvariable=self.thickness2D)

            self.displacement2DLabel = ttk.Label(self.upperFrame2D, text="Displacement")
            self.displacement2DEntry = ttk.Entry(self.upperFrame2D, validate='key', validatecommand=self.vfaz,
                                                 textvariable=self.displacement2D)

            self.overallLength2DLabel.grid(row=0, column=0)
            self.overallLength2DEntry.grid(row=0, column=1)
            self.gripLength2DLabel.grid(row=1, column=0)
            self.gripLength2DEntry.grid(row=1, column=1)
            self.gripWidth2DLabel.grid(row=2, column=0)
            self.gripWidth2DEntry.grid(row=2, column=1)
            self.gageLength2DLabel.grid(row=3, column=0)
            self.gageLength2DEntry.grid(row=3, column=1)
            self.gageWidth2DLabel.grid(row=4, column=0)
            self.gageWidth2DEntry.grid(row=4, column=1)
            self.radius2DLabel.grid(row=5, column=0)
            self.radius2DEntry.grid(row=5, column=1)
            self.thickness2DLabel.grid(row=6, column=0)
            self.thickness2DEntry.grid(row=6, column=1)
            self.displacement2DLabel.grid(row=7, column=0)
            self.displacement2DEntry.grid(row=7, column=1)

            self.buttonDone = Button(self.upperFrame2D, text="Create", command=self.done2D)
            self.buttonExample = Button(self.upperFrame2D, text="Create example ISO 6892-1", command=self.example2D)
            self.buttonDone.grid()
            self.buttonExample.grid()

            # Axisimmetric

            self.upperFrameAxis = ttk.Frame(self.tabAxis)
            self.imageFrameAxis = ttk.Frame(self.tabAxis)

            self.upperFrameAxis.grid(row=1, column=0)
            self.imageFrameAxis.grid(row=0, column=0)

            self.specimensAxis = ('Test', 'PN EN ISO 6892-1 2009')
            self.specimenComboBoxAxis = ttk.Combobox(self.imageFrameAxis, values=self.specimensAxis,
                                                   textvariable=self.specimensAxis)
            self.specimenComboBoxAxis.current(newindex=0)
            self.specimenComboBoxAxis.bind("<<ComboboxSelected>>", self.update_gui_on_selected_specimenAxis)
            self.specimenComboBoxAxis.grid()

            self.overallLengthAxis = StringVar()
            self.gripLengthAxis = StringVar()
            self.gripWidthAxis = StringVar()
            self.gageLengthAxis = StringVar()
            self.gageWidthAxis = StringVar()
            self.radiusAxis = StringVar()
            self.displacementAxis = StringVar()
            # self.displacementAxis.set("10.0")

            self.overallLengthAxisLabel = ttk.Label(self.upperFrameAxis, text="Overall length")
            self.overallLengthAxisEntry = ttk.Entry(self.upperFrameAxis, validate='key', validatecommand=self.vfaz,
                                                  textvariable=self.overallLengthAxis)

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
            self.overallLengthAxisLabel.grid(row=0, column=0)
            self.overallLengthAxisEntry.grid(row=0, column=1)
            self.gripLengthAxisLabel.grid(row=1, column=0)
            self.gripLengthAxisEntry.grid(row=1, column=1)
            self.gripWidthAxisLabel.grid(row=2, column=0)
            self.gripWidthAxisEntry.grid(row=2, column=1)
            self.gageLengthAxisLabel.grid(row=3, column=0)
            self.gageLengthAxisEntry.grid(row=3, column=1)
            self.gageWidthAxisLabel.grid(row=4, column=0)
            self.gageWidthAxisEntry.grid(row=4, column=1)
            self.radiusAxisLabel.grid(row=5, column=0)
            self.radiusAxisEntry.grid(row=5, column=1)
            self.displacementAxisLabel.grid(row=6, column=0)
            self.displacementAxisEntry.grid(row=6, column=1)

            self.buttonDone = Button(self.upperFrameAxis, text="Create", command=self.doneAxis)
            self.buttonExample = Button(self.upperFrameAxis, text="Create example", command=self.exampleAxis)
            self.buttonDone.grid()
            self.buttonExample.grid()

            # 3D

            self.upperFrame3D = ttk.Frame(self.tab3D)
            self.imageFrame3D = ttk.Frame(self.tab3D)

            self.specimenImageLabel3D = ttk.Label(self.imageFrame3D, image=self.specimenImmage)
            self.specimenImageLabel3D.image = self.specimenImmage
            self.specimenImageLabel3D.grid()

            self.imageFrame3D.grid(row=0, column=0)
            self.upperFrame3D.grid(row=1, column=0)

            self.specimens3D = ('Test', 'PN EN ISO 6892-1 2009')
            self.specimenComboBox3D = ttk.Combobox(self.imageFrame3D, values=self.specimens3D,
                                                   textvariable=self.specimens3D)
            self.specimenComboBox3D.current(newindex=0)
            self.specimenComboBox3D.bind("<<ComboboxSelected>>", self.update_gui_on_selected_specimen3D)
            self.specimenComboBox3D.grid()

            self.overallLength3D = StringVar()
            self.gripLength3D = StringVar()
            self.gripWidth3D = StringVar()
            self.gageLength3D = StringVar()
            self.gageWidth3D = StringVar()
            self.radius3D = StringVar()
            self.depth3D = StringVar()
            self.displacement3D = StringVar()
            # self.displacement3D.set("10.0")


            self.overallLength3DLabel = ttk.Label(self.upperFrame3D, text="L0 - Overall length")
            self.overallLength3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                                  textvariable=self.overallLength3D)

            self.gripLength3DLabel = ttk.Label(self.upperFrame3D, text="D - Grip tab length")
            self.gripLength3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                               textvariable=self.gripLength3D)

            self.gripWidth3DLabel = ttk.Label(self.upperFrame3D, text="W0 - Overall width")
            self.gripWidth3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                              textvariable=self.gripWidth3D)

            self.gageLength3DLabel = ttk.Label(self.upperFrame3D, text="L - Length of narrow section")
            self.gageLength3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                               textvariable=self.gageLength3D)

            self.gageWidth3DLabel = ttk.Label(self.upperFrame3D, text="Wc - width of narrow section")
            self.gageWidth3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                              textvariable=self.gageWidth3D)

            self.radius3DLabel = ttk.Label(self.upperFrame3D, text="R - Radius")
            self.radius3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                           textvariable=self.radius3D)

            self.depth3DLabel = ttk.Label(self.upperFrame3D, text="T- Thickness")
            self.depth3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                          textvariable=self.depth3D)

            self.displacement3DLabel = ttk.Label(self.upperFrame3D, text="Displacement")
            self.displacement3DEntry = ttk.Entry(self.upperFrame3D, validate='key', validatecommand=self.vfaz,
                                                 textvariable=self.displacement3D)

            self.overallLength3DLabel.grid(row=0, column=0)
            self.overallLength3DEntry.grid(row=0, column=1)
            self.gripLength3DLabel.grid(row=1, column=0)
            self.gripLength3DEntry.grid(row=1, column=1)
            self.gripWidth3DLabel.grid(row=2, column=0)
            self.gripWidth3DEntry.grid(row=2, column=1)
            self.gageLength3DLabel.grid(row=3, column=0)
            self.gageLength3DEntry.grid(row=3, column=1)
            self.gageWidth3DLabel.grid(row=4, column=0)
            self.gageWidth3DEntry.grid(row=4, column=1)
            self.radius3DLabel.grid(row=5, column=0)
            self.radius3DEntry.grid(row=5, column=1)
            self.depth3DLabel.grid(row=6, column=0)
            self.depth3DEntry.grid(row=6, column=1)

            self.displacement3DLabel.grid(row=7, column=0)
            self.displacement3DEntry.grid(row=7, column=1)

            self.buttonDone = Button(self.upperFrame3D, text="Create", command=self.done3D)
            self.buttonExample = Button(self.upperFrame3D, text="Create example", command=self.example3D)
            self.buttonDone.grid()
            self.buttonExample.grid()

            # cylinder

            self.upperFrameCylinder = ttk.Frame(self.tabCylinder)
            self.imageFrameCylinder = ttk.Frame(self.tabCylinder)

            self.upperFrameCylinder.grid(row=1, column=0)
            self.imageFrameCylinder.grid(row=0, column=0)

            self.specimensCylinder = ('Test', 'PN EN ISO 6892-1 2009')
            self.specimenComboBoxCylinder = ttk.Combobox(self.imageFrameCylinder, values=self.specimensCylinder,
                                                   textvariable=self.specimensCylinder)
            self.specimenComboBoxCylinder.current(newindex=0)
            self.specimenComboBoxCylinder.bind("<<ComboboxSelected>>", self.update_gui_on_selected_specimenCylinder)
            self.specimenComboBoxCylinder.grid()

            self.overallLengthCylinder = StringVar()
            self.gripLengthCylinder = StringVar()
            self.gripWidthCylinder = StringVar()
            self.gageLengthCylinder = StringVar()
            self.gageWidthCylinder = StringVar()
            self.radiusCylinder = StringVar()
            self.displacementCylinder = StringVar()
            # self.displacementCylinder.set("10.0")

            self.overallLengthCylinderLabel = ttk.Label(self.upperFrameCylinder, text="Overall length")
            self.overallLengthCylinderEntry = ttk.Entry(self.upperFrameCylinder, validate='key', validatecommand=self.vfaz,
                                                  textvariable=self.overallLengthCylinder)

            self.gripLengthCylinderLabel = ttk.Label(self.upperFrameCylinder, text="Grip length")
            self.gripLengthCylinderEntry = ttk.Entry(self.upperFrameCylinder, validate='key', validatecommand=self.vfaz,
                                                     textvariable=self.gripLengthCylinder)

            self.gripWidthCylinderLabel = ttk.Label(self.upperFrameCylinder, text="Grip width")
            self.gripWidthCylinderEntry = ttk.Entry(self.upperFrameCylinder, validate='key', validatecommand=self.vfaz,
                                                    textvariable=self.gripWidthCylinder)

            self.gageLengthCylinderLabel = ttk.Label(self.upperFrameCylinder, text="Gage length")
            self.gageLengthCylinderEntry = ttk.Entry(self.upperFrameCylinder, validate='key', validatecommand=self.vfaz,
                                                     textvariable=self.gageLengthCylinder)

            self.gageWidthCylinderLabel = ttk.Label(self.upperFrameCylinder, text="Gage width")
            self.gageWidthCylinderEntry = ttk.Entry(self.upperFrameCylinder, validate='key', validatecommand=self.vfaz,
                                                    textvariable=self.gageWidthCylinder)

            self.radiusCylinderLabel = ttk.Label(self.upperFrameCylinder, text="Radius")
            self.radiusCylinderEntry = ttk.Entry(self.upperFrameCylinder, validate='key', validatecommand=self.vfaz,
                                                 textvariable=self.radiusCylinder)

            self.displacementCylinderLabel = ttk.Label(self.upperFrameCylinder, text="Displacement")
            self.displacementCylinderEntry = ttk.Entry(self.upperFrameCylinder, validate='key',
                                                       validatecommand=self.vfaz,
                                                       textvariable=self.displacementCylinder)

            self.overallLengthCylinderLabel.grid(row=0, column=0)
            self.overallLengthCylinderEntry.grid(row=0, column=1)
            self.gripLengthCylinderLabel.grid(row=1, column=0)
            self.gripLengthCylinderEntry.grid(row=1, column=1)
            self.gripWidthCylinderLabel.grid(row=2, column=0)
            self.gripWidthCylinderEntry.grid(row=2, column=1)
            self.gageLengthCylinderLabel.grid(row=3, column=0)
            self.gageLengthCylinderEntry.grid(row=3, column=1)
            self.gageWidthCylinderLabel.grid(row=4, column=0)
            self.gageWidthCylinderEntry.grid(row=4, column=1)
            self.radiusCylinderLabel.grid(row=5, column=0)
            self.radiusCylinderEntry.grid(row=5, column=1)
            self.displacementCylinderLabel.grid(row=6, column=0)
            self.displacementCylinderEntry.grid(row=6, column=1)

            self.buttonDone = Button(self.upperFrameCylinder, text="Create", command=self.doneCylinder)
            self.buttonExample = Button(self.upperFrameCylinder, text="Create example", command=self.exampleCylinder)
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
            self.abaqus.createSpecimen2D(float(self.overallLength2D.get()), float(self.gripLength2D.get()),
                                         float(self.gripWidth2D.get()),
                                         float(self.gageLength2D.get()), float(self.gageWidth2D.get()),
                                         float(self.radius2D.get()), float(self.thickness2D.get()))
            self.abaqus.assemblyStep2D(float(self.displacement2D.get()))
            self.abaqus.mesh2D()
            self.abaqus.job2D()

        def doneAxis(self):
            self.abaqus.createSpecimenAxis(float(self.overallLengthAxis.get()), float(self.gripLengthAxis.get()), float(self.gripWidthAxis.get()),
                                           float(self.gageLengthAxis.get()), float(self.gageWidthAxis.get()),
                                           float(self.radiusAxis.get()))
            self.abaqus.assemblyStepAxis(float(self.displacementAxis.get()))
            self.abaqus.meshAxis()
            self.abaqus.jobAxis()

        def done3D(self):
            self.abaqus.createSpecimen3D(float(self.overallLength3D.get()), float(self.gripLength3D.get()), float(self.gripWidth3D.get()),
                                         float(self.gageLength3D.get()), float(self.gageWidth3D.get()),
                                         float(self.radius3D.get()), float(self.depth3D.get()))
            self.abaqus.assemblyStep3D(float(self.displacement3D.get()))
            self.abaqus.mesh3D()
            self.abaqus.job3D()

        def doneCylinder(self):
            self.abaqus.createSpecimenCylinder(float(self.overallLengthCylinder.get()), float(self.gripLengthCylinder.get()),
                                               float(self.gripWidthCylinder.get()),
                                               float(self.gageLengthCylinder.get()),
                                               float(self.gageWidthCylinder.get()),
                                               float(self.radiusCylinder.get()))
            self.abaqus.assemblyStepCylinder(float(self.displacementCylinder.get()))
            self.abaqus.meshCylinder()
            self.abaqus.jobCylinder()

        def example2D(self):
            self.abaqus.createSpecimen2D(167.5, 40, 20.0, 75.0, 12.5, 12.5, 2)
            self.abaqus.assemblyStep2D(10.0)
            self.abaqus.mesh2D()
            self.abaqus.job2D()

        def exampleAxis(self):
            self.abaqus.createSpecimenAxis(175, 40.0, 20.0, 75.0, 10.0, 12.5)
            self.abaqus.assemblyStepAxis(10.0)
            self.abaqus.meshAxis()
            self.abaqus.jobAxis()

        def example3D(self):
            self.abaqus.createSpecimen3D(175, 40.0, 20.0, 75.0, 10.0, 12.5, 2)
            self.abaqus.assemblyStep3D(10.0)
            self.abaqus.mesh3D()
            self.abaqus.job3D()

        def exampleCylinder(self):
            self.abaqus.createSpecimenCylinder(175, 40.0, 20.0, 75.0, 10.0, 12.5)
            self.abaqus.assemblyStepCylinder(10.0)
            self.abaqus.meshCylinder()
            self.abaqus.jobCylinder()

        def update_gui_on_selected_specimen2D(self, event):
            if self.specimenComboBox2D.get() == 'PN EN ISO 6892-1 2009':
                self.overallLength2D.set("167.5")
                self.gripLength2D.set("40")
                self.gripWidth2D.set("20")
                self.gageLength2D.set("75")
                self.gageWidth2D.set("12.5")
                self.radius2D.set("7.29")
                self.thickness2D.set("2")

        def update_gui_on_selected_specimen3D(self, event):
            if self.specimenComboBox3D.get() == 'PN EN ISO 6892-1 2009':
                self.overallLength3D.set("167.5")
                self.gripLength3D.set("40")
                self.gripWidth3D.set("20")
                self.gageLength3D.set("75")
                self.gageWidth3D.set("12.5")
                self.radius3D.set("7.29")
                self.depth3D.set("2")

        def update_gui_on_selected_specimenCylinder(self, event):
            if self.specimenComboBoxCylinder.get() == 'PN EN ISO 6892-1 2009':
                self.overallLengthCylinder.set("212.5")
                self.gripLengthCylinder.set("40")
                self.gripWidthCylinder.set("30")
                self.gageLengthCylinder.set("120")
                self.gageWidthCylinder.set("20")
                self.radiusCylinder.set("6.41")

        def update_gui_on_selected_specimenAxis(self, event):
            if self.specimenComboBoxAxis.get() == 'PN EN ISO 6892-1 2009':
                self.overallLengthAxis.set("212.5")
                self.gripLengthAxis.set("40")
                self.gripWidthAxis.set("30")
                self.gageLengthAxis.set("120")
                self.gageWidthAxis.set("20")
                self.radiusAxis.set("6.41")

    app = GuiApplication()


if __name__ == '__main__':
    TensileFunction()
