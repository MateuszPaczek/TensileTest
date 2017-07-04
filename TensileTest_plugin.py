from abaqusGui import getAFXApp
toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerKernelMenuButton(buttonText='TensileTestGenerator',
                                 moduleName='Tensile',
                                 functionName='TensileFunction()',
                                 author='Mateusz Pączek',
                                 description='Abaqus Tensile Test Generator')

