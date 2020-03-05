
import setuptools

setuptools.setup(
    name='sengkalancli',  
    version='0.1',
    author="lantip",
    author_email="lantip@gmail.comm",
    description="Sengkalan atau Candra Sengkala adalah cara orang Jawa menyembunyikan atau mengubah angka tahun menjadi kalimat. Contohnya adalah tahun runtuhnya kerajaan Majapahit, didapat dari candra sengkala Sirna Ilang Kertaning Bumi.",
    long_description="Sengkalan atau Candra Sengkala adalah cara orang Jawa menyembunyikan atau mengubah angka tahun menjadi kalimat. Contohnya adalah tahun runtuhnya kerajaan Majapahit, didapat dari candra sengkala Sirna Ilang Kertaning Bumi.",
    url="https://github.com/lantip/sengkalancli",
    packages=["sengkalancli"],
    entry_points = {
        "console_scripts": ['sengkalancli = sengkalancli.sengkalancli:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
