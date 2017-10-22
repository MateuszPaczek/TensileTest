from abaqus import *
from abaqusConstants import *


class MaterialManager:
    def __init__(self):
        pass

    def addExampleMaterial(self):
        mdb.models['Model-1'].Material(name='AISI 1005 Steel',
                                       description='Example Steel, please use any material model instead')
        mdb.models['Model-1'].materials['AISI 1005 Steel'].Density(table=((
                                                                              7.872e-09,),))
        mdb.models['Model-1'].materials['AISI 1005 Steel'].Elastic(table=((
                                                                              2e6, 0.29),))
        mdb.models['Model-1'].materials['AISI 1005 Steel'].Plastic(table=((
                                                                              9.205642707, 0.0), (107.2286726, 0.005),
                                                                          (130.9438672, 0.01), (147.1786568, 0.015),
                                                                          (159.904025, 0.02), (170.5275133, 0.025),
                                                                          (179.7293766, 0.03), (187.8957685, 0.035),
                                                                          (195.2691467, 0.04), (202.0127311, 0.045),
                                                                          (208.2421754, 0.05), (214.0427168, 0.055),
                                                                          (219.4791657, 0.06), (
                                                                              224.6020664, 0.065), (229.451675, 0.07),
                                                                          (234.060627, 0.075), (
                                                                              238.455784, 0.08), (242.6595468, 0.085),
                                                                          (246.6908111, 0.09), (
                                                                              250.5656775, 0.095), (254.2979884, 0.1),
                                                                          (257.8997402, 0.105), (
                                                                              261.3814047, 0.11), (264.7521821, 0.115),
                                                                          (268.0202041, 0.12), (
                                                                              271.1926958, 0.125), (274.2761094, 0.13),
                                                                          (277.276233, 0.135), (
                                                                              280.1982801, 0.14), (283.0469659, 0.145),
                                                                          (285.8265695, 0.15), (
                                                                              288.5409877, 0.155), (291.19378, 0.16),
                                                                          (293.7882077, 0.165), (
                                                                              296.3272666, 0.17), (298.8137162, 0.175),
                                                                          (301.2501042, 0.18), (
                                                                              303.638788, 0.185), (305.9819541, 0.19),
                                                                          (308.2816343, 0.195), (
                                                                              310.5397203, 0.2), (312.7579768, 0.205),
                                                                          (314.9380524, 0.21), (
                                                                              317.0814906, 0.215), (319.1897381, 0.22),
                                                                          (321.264153, 0.225), (
                                                                              323.3060125, 0.23), (325.3165188, 0.235),
                                                                          (327.2968054, 0.24), (
                                                                              329.2479422, 0.245), (331.1709402, 0.25),
                                                                          (333.0667561, 0.255), (
                                                                              334.936296, 0.26), (336.7804191, 0.265),
                                                                          (338.5999409, 0.27), (
                                                                              340.3956361, 0.275), (342.1682417, 0.28),
                                                                          (343.918459, 0.285), (
                                                                              345.6469562, 0.29), (347.3543704, 0.295),
                                                                          (349.0413099, 0.3), (
                                                                              350.7083552, 0.305), (352.3560615, 0.31),
                                                                          (353.9849596, 0.315), (
                                                                              355.5955577, 0.32), (357.1883427, 0.325),
                                                                          (358.7637812, 0.33), (
                                                                              360.3223205, 0.335), (361.8643903, 0.34),
                                                                          (363.3904029, 0.345), (
                                                                              364.9007547, 0.35), (366.3958267, 0.355),
                                                                          (367.8759855, 0.36), (
                                                                              369.341584, 0.365), (370.7929618, 0.37),
                                                                          (372.2304465, 0.375), (
                                                                              373.6543536, 0.38), (375.0649874, 0.385),
                                                                          (376.4626418, 0.39), (
                                                                              377.8476002, 0.395), (379.2201367, 0.4),
                                                                          (380.5805157, 0.405), (
                                                                              381.928993, 0.41), (383.2658162, 0.415),
                                                                          (384.5912244, 0.42), (
                                                                              385.9054494, 0.425), (387.2087154, 0.43),
                                                                          (388.5012397, 0.435), (
                                                                              389.7832327, 0.44), (391.0548985, 0.445),
                                                                          (392.316435, 0.45), (
                                                                              393.5680339, 0.455), (394.8098816, 0.46),
                                                                          (396.0421588, 0.465), (
                                                                              397.2650409, 0.47), (398.4786984, 0.475),
                                                                          (399.683297, 0.48), (
                                                                              400.8789974, 0.485), (402.0659563, 0.49),
                                                                          (403.2443256, 0.495), (
                                                                              404.4142535, 0.5), (405.5758839, 0.505),
                                                                          (406.729357, 0.51), (
                                                                              407.8748091, 0.515), (409.0123731, 0.52),
                                                                          (410.1421784, 0.525), (
                                                                              411.2643511, 0.53), (412.379014, 0.535),
                                                                          (413.4862868, 0.54), (
                                                                              414.5862863, 0.545), (415.6791264, 0.55),
                                                                          (416.764918, 0.555), (
                                                                              417.8437697, 0.56), (418.915787, 0.565),
                                                                          (419.9810732, 0.57), (
                                                                              421.039729, 0.575), (422.0918529, 0.58),
                                                                          (423.1375409, 0.585), (
                                                                              424.1768869, 0.59), (425.2099826, 0.595),
                                                                          (426.2369177, 0.6), (
                                                                              427.2577798, 0.605), (428.2726546, 0.61),
                                                                          (429.2816258, 0.615), (
                                                                              430.2847753, 0.62), (431.2821832, 0.625),
                                                                          (432.2739281, 0.63), (
                                                                              433.2600866, 0.635), (434.2407337, 0.64),
                                                                          (435.215943, 0.645), (
                                                                              436.1857865, 0.65), (437.1503345, 0.655),
                                                                          (438.1096562, 0.66), (
                                                                              439.0638191, 0.665), (440.0128894, 0.67),
                                                                          (440.956932, 0.675), (
                                                                              441.8960105, 0.68), (442.8301872, 0.685),
                                                                          (443.7595232, 0.69), (
                                                                              444.6840784, 0.695), (445.6039115, 0.7),
                                                                          (446.5190801, 0.705), (
                                                                              447.4296406, 0.71), (448.3356486, 0.715),
                                                                          (449.2371583, 0.72), (
                                                                              450.1342231, 0.725), (451.0268954, 0.73),
                                                                          (451.9152264, 0.735), (
                                                                              452.7992667, 0.74), (453.6790658, 0.745),
                                                                          (454.5546722, 0.75), (
                                                                              455.4261337, 0.755), (456.2934972, 0.76),
                                                                          (457.1568087, 0.765), (
                                                                              458.0161134, 0.77), (458.8714559, 0.775),
                                                                          (459.7228796, 0.78), (
                                                                              460.5704276, 0.785), (461.4141419, 0.79),
                                                                          (462.2540642, 0.795), (
                                                                              463.0902349, 0.8), (463.9226943, 0.805),
                                                                          (464.7514817, 0.81), (
                                                                              465.5766358, 0.815), (466.3981946, 0.82),
                                                                          (467.2161957, 0.825), (
                                                                              468.0306759, 0.83), (468.8416713, 0.835),
                                                                          (469.6492176, 0.84), (
                                                                              470.4533499, 0.845), (471.2541027, 0.85),
                                                                          (472.05151, 0.855), (
                                                                              472.8456051, 0.86), (473.6364211, 0.865),
                                                                          (474.4239901, 0.87), (
                                                                              475.2083442, 0.875), (475.9895147, 0.88),
                                                                          (476.7675325, 0.885), (
                                                                              477.5424281, 0.89), (478.3142313, 0.895),
                                                                          (479.0829718, 0.9), (
                                                                              479.8486786, 0.905), (480.6113802, 0.91),
                                                                          (481.371105, 0.915), (
                                                                              482.1278808, 0.92), (482.8817348, 0.925),
                                                                          (483.6326941, 0.93), (
                                                                              484.3807853, 0.935), (485.1260346, 0.94),
                                                                          (485.8684677, 0.945), (
                                                                              486.6081103, 0.95), (487.3449872, 0.955),
                                                                          (488.0791234, 0.96), (
                                                                              488.8105432, 0.965), (489.5392706, 0.97),
                                                                          (490.2653293, 0.975), (
                                                                              490.9887428, 0.98), (491.7095341, 0.985),
                                                                          (492.4277259, 0.99), (
                                                                              493.1433406, 0.995), (493.8564005, 1.0)))
