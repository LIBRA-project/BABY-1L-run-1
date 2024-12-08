from libra_toolbox.tritium.model import ureg, Model
import numpy as np
from libra_toolbox.tritium.lsc_measurements import (
    LSCFileReader,
    LIBRASample,
    LIBRARun,
    LSCSample,
    GasStream,
)

data_folder = "../../data/tritium_detection"

# read files
file_reader_1 = LSCFileReader(
    f"{data_folder}/1L_OV_IV_1-0-X_IV_1-1-X.csv",
    vial_labels=[
        "OV-1-0-1",
        "OV-1-0-2",
        "OV-1-0-3",
        "OV-1-0-4",
        None,
        "IV-1-0-1",
        "IV-1-0-2",
        "IV-1-0-3",
        "IV-1-0-4",
        None,
        "IV-1-1-1",
        "IV-1-1-2",
        "IV-1-1-3",
        "IV-1-1-4",
    ],
)
file_reader_1.read_file()

file_reader_2 = LSCFileReader(
    f"{data_folder}/1L_IV_1-2-X.csv",
    vial_labels=[
        "IV-1-2-1",
        "IV-1-2-2",
        "IV-1-2-3",
        "IV-1-2-4",
    ],
)
file_reader_2.read_file()

file_reader_3 = LSCFileReader(
    f"{data_folder}/IV_1-3-X_BL-1.csv",
    vial_labels=[
        "IV-BL-1",
        None,
        "IV-1-3-1",
        "IV-1-3-2",  # probably has a statistic issue
        "IV-1-3-3",
        "IV-1-3-4",
    ],
)
file_reader_3.read_file()

file_reader_4 = LSCFileReader(
    f"{data_folder}/Report1.csv",
    vial_labels=[
        "BL-1_count_4",
        None,
        "IV-1-4-1",
        "IV-1-4-2",
        "IV-1-4-3",
        "IV-1-4-4",
        None,
        "OV-1-1-1",
        "OV-1-1-2",
        "OV-1-1-3",
        "OV-1-1-4",
        None,
        "IV-1-3-2 (repeat)",
    ],
)
file_reader_4.read_file()


file_reader_OV_1_recount = LSCFileReader(
    f"{data_folder}/OV-1-1_with_avg.csv",
    vial_labels=[
        "BL-1_1",
        "BL-1_2",
        "BL-1_3",
        "BL-1_4",
        "BL-1_5",
        "BL-1_6",
        "BL-1_avg",
        None,
        "OV-1-1-1_1",
        "OV-1-1-1_2",
        "OV-1-1-1_3",
        "OV-1-1-1_4",
        "OV-1-1-1_5",
        "OV-1-1-1_6",
        "OV-1-1-1_avg",
        "OV-1-1-2_1",
        "OV-1-1-2_2",
        "OV-1-1-2_3",
        "OV-1-1-2_4",
        "OV-1-1-2_5",
        "OV-1-1-2_6",
        "OV-1-1-2_avg",
        "OV-1-1-3_1",
        "OV-1-1-3_2",
        "OV-1-1-3_3",
        "OV-1-1-3_4",
        "OV-1-1-3_5",
        "OV-1-1-3_6",
        "OV-1-1-3_avg",
        "OV-1-1-4_1",
        "OV-1-1-4_2",
        "OV-1-1-4_3",
        "OV-1-1-4_4",
        "OV-1-1-4_5",
        "OV-1-1-4_6",
        "OV-1-1-4_avg",
    ],
)
file_reader_OV_1_recount.read_file()

file_reader_5 = LSCFileReader(
    f"{data_folder}/1L_BL-1_IV-1-5_OV-1-2.csv",
    vial_labels=[
        "1L-BL-1",
        None,
        "IV-1-5-1",
        "IV-1-5-2",
        "IV-1-5-3",
        "IV-1-5-4",
        None,
        "OV-1-2-1",
        "OV-1-2-2",
        "OV-1-2-3",
        "OV-1-2-4",
    ],
)
file_reader_5.read_file()


file_reader_6 = LSCFileReader(
    f"{data_folder}/1L_BL-1_IV-1-6_OV-1-3.csv",
    vial_labels=[
        "1L-BL-1",
        None,
        "IV 1-6-1",
        "IV 1-6-2",
        "IV 1-6-3",
        "IV 1-6-4",
        None,
        "OV 1-3-1",
        "OV 1-3-2",
        "OV 1-3-3",
        "OV 1-3-4",
    ],
)
file_reader_6.read_file()

file_reader_7 = LSCFileReader(
    f"{data_folder}/1L_BL-1_IV-1-6_OV-1-3_recount.csv",
    vial_labels=[
        "1L-BL-1",
        None,
        "IV 1-6-1",
        "IV 1-6-2",
        "IV 1-6-3",
        "IV 1-6-4",
        None,
        "OV 1-3-1",
        "OV 1-3-2",
        "OV 1-3-3",
        "OV 1-3-4",
    ],
)
file_reader_7.read_file()

file_reader_8 = LSCFileReader(
    f"{data_folder}/1L_BL-1_IV-1-7_OV-1-4.csv",
    vial_labels=[
        "1L-BL-1",
        None,
        "IV 1-7-1",
        "IV 1-7-2",
        "IV 1-7-3",
        "IV 1-7-4",
        None,
        "OV 1-4-1",
        "OV 1-4-2",
        "OV 1-4-3",
        "OV 1-4-4",
    ],
)
file_reader_8.read_file()


# Make samples

sample_0_IV = LIBRASample(
    samples=[
        LSCSample.from_file(file_reader_1, label)
        for label in ["IV-1-0-1", "IV-1-0-2", "IV-1-0-3", "IV-1-0-4"]
    ],
    time="before run",
)

sample_1_IV = LIBRASample(
    samples=[
        LSCSample.from_file(file_reader_1, label)
        for label in ["IV-1-1-1", "IV-1-1-2", "IV-1-1-3", "IV-1-1-4"]
    ],
    time="11/5/2024 12:32 PM",
)

sample_2_IV = LIBRASample(
    samples=[
        LSCSample.from_file(file_reader_2, label)
        for label in ["IV-1-2-1", "IV-1-2-2", "IV-1-2-3", "IV-1-2-4"]
    ],
    time="11/7/2024 8:49 AM",
)

sample_3_IV = LIBRASample(
    samples=[
        LSCSample.from_file(file_reader_3, "IV-1-3-1"),
        LSCSample.from_file(
            file_reader_4, "IV-1-3-2 (repeat)"
        ),  # the first one has a statistic issue
        LSCSample.from_file(file_reader_3, "IV-1-3-3"),
        LSCSample.from_file(file_reader_3, "IV-1-3-4"),
    ],
    time="11/10/2024 1:33 PM",
)
blank_sample_3_IV = LSCSample.from_file(file_reader_3, "IV-BL-1")


sample_4_IV = LIBRASample(
    samples=[
        LSCSample.from_file(file_reader_4, label)
        for label in ["IV-1-4-1", "IV-1-4-2", "IV-1-4-3", "IV-1-4-4"]
    ],
    time="11/13/2024 2:31 PM",
)
blank_sample_4 = LSCSample.from_file(file_reader_4, "BL-1_count_4")

sample_1_OV = LIBRASample(
    samples=[
        LSCSample.from_file(file_reader_OV_1_recount, label)
        for label in ["OV-1-1-1_avg", "OV-1-1-2_avg", "OV-1-1-3_avg", "OV-1-1-4_avg"]
    ],
    time="11/13/2024 2:31 PM",
)
blank_sample_1_OV = LSCSample.from_file(file_reader_OV_1_recount, "BL-1_avg")


sample_5_IV = LIBRASample(
    samples=[
        LSCSample.from_file(file_reader_5, label)
        for label in ["IV-1-5-1", "IV-1-5-2", "IV-1-5-3", "IV-1-5-4"]
    ],
    time="11/18/2024 1:40 PM",
)
sample_5_IV_background = LSCSample.from_file(file_reader_5, "1L-BL-1")
sample_2_OV_background = sample_5_IV_background

sample_2_OV = LIBRASample(
    samples=[
        LSCSample.from_file(file_reader_5, label)
        for label in ["OV-1-2-1", "OV-1-2-2", "OV-1-2-3", "OV-1-2-4"]
    ],
    time="11/18/2024 1:40 PM",
)

sample_6_IV = LIBRASample(
    samples=[
        LSCSample.from_file(file_reader_7, label)
        for label in ["IV 1-6-1", "IV 1-6-2", "IV 1-6-3", "IV 1-6-4"]
    ],
    time="11/23/2024 4:19 PM",
)

sample_3_OV = LIBRASample(
    samples=[
        LSCSample.from_file(file_reader_7, label)
        for label in ["OV 1-3-1", "OV 1-3-2", "OV 1-3-3", "OV 1-3-4"]
    ],
    time="11/23/2024 4:19 PM",
)

background_file_7 = LSCSample.from_file(file_reader_7, "1L-BL-1")

sample_7_IV = LIBRASample(
    samples=[
        LSCSample.from_file(file_reader_8, label)
        for label in ["IV 1-7-1", "IV 1-7-2", "IV 1-7-3", "IV 1-7-4"]
    ],
    time="11/29/2024 11:43 AM",
)

sample_4_OV = LIBRASample(
    samples=[
        LSCSample.from_file(file_reader_8, label)
        for label in ["OV 1-4-1", "OV 1-4-2", "OV 1-4-3", "OV 1-4-4"]
    ],
    time="11/29/2024 11:43 AM",
)

background_file_8 = LSCSample.from_file(file_reader_8, "1L-BL-1")

# Make streams

start_time = "11/4/2024 10:07 AM"

IV_stream = GasStream(
    [
        sample_1_IV,
        sample_2_IV,
        sample_3_IV,
        sample_4_IV,
        sample_5_IV,
        sample_6_IV,
        sample_7_IV,
    ],
    start_time=start_time,
)
OV_stream = GasStream(
    [sample_1_OV, sample_2_OV, sample_3_OV, sample_4_OV], start_time=start_time
)

# substract background
for sample in [sample_1_IV, sample_2_IV]:
    sample.substract_background(
        background_sample=LSCSample(activity=0.320 * ureg.Bq, name="background")
    )  # TODO don't have a real background here

sample_3_IV.substract_background(background_sample=blank_sample_3_IV)
sample_4_IV.substract_background(background_sample=blank_sample_4)
sample_5_IV.substract_background(background_sample=sample_5_IV_background)
sample_6_IV.substract_background(background_sample=background_file_7)
sample_7_IV.substract_background(background_sample=background_file_8)
sample_1_OV.substract_background(background_sample=blank_sample_1_OV)
sample_2_OV.substract_background(background_sample=sample_2_OV_background)
sample_3_OV.substract_background(background_sample=background_file_7)
sample_4_OV.substract_background(background_sample=background_file_8)

# create run
run = LIBRARun(streams=[IV_stream, OV_stream], start_time=start_time)

# check that background is always substracted
for stream in run.streams:
    for sample in stream.samples:
        for lsc_vial in sample.samples:
            assert (
                lsc_vial.background_substracted
            ), f"Background not substracted for {sample}"


replacement_times_top = [
    sample.get_relative_time(start_time) for sample in IV_stream.samples
]
replacement_times_walls = [
    sample.get_relative_time(start_time) for sample in OV_stream.samples
]

# convert timedelta to pint quantity  # TODO add this to libra-toolbox

replacement_times_top = [
    time.total_seconds() * ureg.second for time in replacement_times_top
]
replacement_times_walls = [
    time.total_seconds() * ureg.second for time in replacement_times_walls
]

replacement_times_top = sorted(replacement_times_top)

replacement_times_walls = sorted(replacement_times_walls)


# Model

baby_diameter = 14 * ureg.cm  # TODO confirm with CAD
baby_radius = 0.5 * baby_diameter
baby_volume = 1 * ureg.L
baby_cross_section = np.pi * baby_radius**2
baby_height = baby_volume / baby_cross_section

# from OpenMC
calculated_TBR = 1.9e-3 * ureg.particle * ureg.neutron**-1

optimised_ratio = 1.7e-2
k_top = 8.9e-8 * ureg.m * ureg.s**-1
k_wall = optimised_ratio * k_top

exposure_time = 12 * ureg.hour

irradiations = [
    [0 * ureg.hour, 0 + exposure_time],
]

# calculated from Kevin's activation foil analysis from run 100 mL #7
# TODO replace for values for this run
P383_neutron_rate = 4.95e8 * ureg.neutron * ureg.s**-1
A325_neutron_rate = 2.13e8 * ureg.neutron * ureg.s**-1

neutron_rate_relative_uncertainty = 0.089
neutron_rate = (
    A325_neutron_rate
) / 2  # the neutron rate is divided by two to acount for the double counting (two detectors)

baby_model = Model(
    radius=baby_radius,
    height=baby_height,
    TBR=calculated_TBR,
    neutron_rate=neutron_rate,
    irradiations=irradiations,
    k_top=k_top,
    k_wall=k_wall,
)
