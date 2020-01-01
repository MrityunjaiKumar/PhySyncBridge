***********
Get Started
***********

Introduction
============
The physical computing bridge (PhyCom bridge) provides a platform from hardware as well as software side environment to achieve physical computing scope elaborated in the above section. 

PhyCom is platform which have server side implementation of firmata(discussed below), client-server (request-response) model in its MCU. This PhyCom is controlled by a host computer.  This host computer acts as client in this client-server model.

The communication link between PhyCom and host computer is achieved via serial communication, On host side this link enumerated as a COM port with the help of USB-To-Serial bridge. The data transfer is binary in nature and if of full duplex type.
On server side, we have pre-burned firmata image which exposes firmata API over COM  port. On client side we uses PhySyncFirmata, a package to send commands to (request), and receives response from PhyCom Hardware side


What You Need
=============

* PhyCom Board
* USB cable
* Sensors with kit

PhyCom Board Overviews
===========================
.. image:: ../_static/images/phycom_board.png
    :width: 200px
    :align: center
    :height: 200px
    :alt: Phycom board

Installation Step by Step
=========================

Setting up Development Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install python library use following command

.. code-block:: bash

    pip3 install physyncfirmata

To install jupyter, use following commands

.. code-block:: bash

    pip3 install jupyter


Creating Your First Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python 

    # selecting a board
    from phySyncFirmata import ArduinoNano
    # selecting the port 
    board = ArduinoNano('COM40')
    PIN = 6  
    board.digital[PIN].write(1)#high
    board.digital[PIN].write(0)#low
