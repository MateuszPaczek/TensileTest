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
            self.notebook.add(self.tab2D, text="2D model")
            self.notebook.add(self.tab3D, text="3D model")

            self.notebook.pack()

            self.abaqus = AbaqusCommands.AbacusCommands()

            self.vfaz = (self.tab3D.register(self.specimen_dimension_validate),
                         '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

            self.upperFrame2D = ttk.Frame(self.tab2D)
            self.midleFrame2D = ttk.Frame(self.tab2D)

            self.upperFrame2D.grid(row=0, column=0)
            self.midleFrame2D.grid(row=1, column=0)

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

            self.buttonDone = Button(self.upperFrame2D, text="Go", command=self.done)
            self.buttonExample = Button(self.upperFrame2D, text="Create example", command=self.example)
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

        def done(self):
            self.abaqus.createSpecimen(float(self.gripLength2D.get()), float(self.gripWidth2D.get()),
                                       float(self.gageLength2D.get()), float(self.gageWidth2D.get()),
                                       float(self.radius2D.get()), float(self.thickness2D.get()))
            self.abaqus.assemblyStep(float(self.displacement2D.get()))
            self.abaqus.mesh()
            self.abaqus.job()

        def example(self):
            self.abaqus.createSpecimen(40.0, 20.0, 75.0, 10.0, 12.5, 10)
            self.abaqus.assemblyStep(10.0)
            self.abaqus.mesh()
            self.abaqus.job()

    app = GuiApplication()


if __name__ == '__main__':
    TensileFunction()
