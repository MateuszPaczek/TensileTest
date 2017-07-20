from abaqusGui import getAFXApp
toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerKernelMenuButton(buttonText='TensileTestGenerator',
                                 moduleName='TensileTest',
                                 functionName='TensileFunction()',
                                 author='Mateusz Paczek',
                                 description='Abaqus Tensile Test Generator')

