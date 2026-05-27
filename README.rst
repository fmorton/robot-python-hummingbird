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
.. |docs| image:: https://readthedocs.org/projects/robot-motor-controller/badge/?style=flat
    :target: https://robot-motor-controller.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/fmorton/robot-python-motor-controller/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/fmorton/robot-python-motor-controller/actions

.. |requires| image:: https://requires.io/github/fmorton/robot-motor-controller/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/fmorton/robot-motor-controller/requirements/?branch=main

.. |codecov| image:: https://codecov.io/gh/fmorton/robot-motor-controller/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/fmorton/robot-motor-controller

.. |version| image:: https://img.shields.io/pypi/v/robot-motor-controller.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/robot-motor-controller

.. |wheel| image:: https://img.shields.io/pypi/wheel/robot-motor-controller.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/robot-motor-controller

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/robot-motor-controller.svg
    :alt: Supported versions
    :target: https://pypi.org/project/robot-motor-controller

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/robot-motor-controller.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/robot-motor-controller


.. end-badges

General python support for single and dual motor controllers.

* Free software: MIT License

Installation
============

::

    pip install robot-motor-controller

You can also install the in-development version with::

    pip install https://github.com/fmorton/robot-python-hummingbird/archive/main.zip


Motor Controller Example with a Birdbrain Hummingbird
=====================================================

.. code-block:: python

  from robot.hummingbird import Hummingbird
  from robot.l298n_dual_motor_controller import L298nDualMotorController
  from time import sleep

  hummingbird = Hummingbird()

  motors = L298nDualMotorController(hummingbird)

  motors.move_left_motor(40)  # left motor forward
  sleep(1.0)
  motors.move_left_motor(0)  # stop left motor

  motors.move_right_motor(-40)  # right motor backwards
  sleep(1.0)

  motors.move(50, 50)  # move both motors forward
  sleep(1.0)

  motors.stop()



Testing
=======

To run all the tests run::

    pytest
