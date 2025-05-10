from setuptools import setup, find_packages

setup(
    name="face-detection-haar-cascade",
    version="0.1.0",
    description="Real-time face detection using Haar Cascade classifiers",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.20.0",
        "requests>=2.25.0",
    ],
    python_requires=">=3.6",
)
