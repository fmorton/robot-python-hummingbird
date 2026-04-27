========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - package
      - | |version| |wheel| |supported-versions|
.. |docs| image:: https://readthedocs.org/projects/robot-hummingbird/badge/?style=flat
    :target: https://robot-hummingbird.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/fmorton/robot-hummingbird/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/fmorton/robot-hummingbird/actions

.. |requires| image:: https://requires.io/github/fmorton/robot-hummingbird/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/fmorton/robot-hummingbird/requirements/?branch=main

.. |codecov| image:: https://codecov.io/gh/fmorton/robot-hummingbird/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/fmorton/robot-hummingbird

.. |version| image:: https://img.shields.io/pypi/v/robot-hummingbird.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/robot-hummingbird

.. |wheel| image:: https://img.shields.io/pypi/wheel/robot-hummingbird.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/robot-hummingbird

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/robot-hummingbird.svg
    :alt: Supported versions
    :target: https://pypi.org/project/robot-hummingbird

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/robot-hummingbird.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/robot-hummingbird


.. end-badges

Hummingbird general python support (dual motor controllers).

* Free software: MIT License

Installation
============

::

    pip install robot-hummingbird

You can also install the in-development version with::

    pip install https://github.com/fmorton/robot-python-hummingbird/archive/main.zip


Motor Driver Example with a Birdbrain Hummingbird
=================================================

.. code-block:: python

  from robot.hummingbird import Hummingbird
  from robot.hummingbird_l298n_dual_motor_driver import HummingbirdL298nDualMotorDriver
  from time import sleep

  hummingbird = Hummingbird()

  hummingbird_motors = HummingbirdL298nDualMotorDriver(hummingbird)

  hummingbird_motors.move_left_motor(40)  # left motor forward
  sleep(1.0)
  hummingbird_motors.move_left_motor(0)  # stop left motor

  hummingbird_motors.move_right_motor(-40)  # right motor backwards
  sleep(1.0)

  hummingbird_motors.move(50, 50)  # move both motors forward
  sleep(1.0)

  hummingbird_motors.stop()



Testing
=======

To run all the tests run::

    pytest
