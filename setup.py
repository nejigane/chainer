#!/usr/bin/env python
from setuptools import setup

setup(
    name='chainer',
    version='1.3.0',
    description='A flexible framework of neural networks',
    author='Seiya Tokui',
    author_email='tokui@preferred.jp',
    url='http://chainer.org/',
    packages=['chainer',
              'chainer.functions',
              'chainer.functions.activation',
              'chainer.functions.array',
              'chainer.functions.caffe',
              'chainer.functions.connection',
              'chainer.functions.evaluation',
              'chainer.functions.loss',
              'chainer.functions.math',
              'chainer.functions.noise',
              'chainer.functions.normalization',
              'chainer.functions.pooling',
              'chainer.optimizers',
              'chainer.serializers',
              'chainer.testing',
              'chainer.utils',
              'cupy',
              'cupy.binary',
              'cupy.creation',
              'cupy.cuda',
              'cupy.indexing',
              'cupy.io',
              'cupy.linalg',
              'cupy.logic',
              'cupy.manipulation',
              'cupy.math',
              'cupy.padding',
              'cupy.random',
              'cupy.sorting',
              'cupy.statistics',
              'cupy.testing'],
    package_data={
        'cupy': ['carray.cuh'],
    },
    install_requires=['filelock',
                      'h5py>=2.5.0',
                      'nose',
                      'numpy>=1.9.0',
                      'protobuf',
                      'six>=1.9.0'],
    tests_require=['mock',
                   'nose'],
)
