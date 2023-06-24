# Scuttle Self-Balancing robot

This project of mine was built with the support of [SCUTTLE™](https://www.scuttlerobot.org/). 

## About The Project

This project's subject is to make SCUTTLE Robot balance itself on its two wheels only modifying its default shape and use external MPU6050 sensor in addition. Main idea of this project comes from David Malawey who is Founder of The Scuttle™ and I am glad to bring this idea to reality. Before working on this project i had one project similar to this and it's called [LOTP_BalanceWheel](https://github.com/SMDHuman/BalanceWheel) and its purpose is to make a 3D printed frame, stepper motor driven and Raspberry Pi Pico based two wheels self-balancing robot.

However I have built a two wheels self-balancing robot before, there were a few challenges on this project which I enjoyed a lot. Scuttle Robot has already a predefined setup and I was limited to transform current model in a most easiest and efficient way. Also a new part was designed and printed for this project to be able to hold MPU6050 sensor on the chassis.

Final result is a milestone and an evolutionary progress at SCUTTLE development for all community.
SCUTTLE Robot is designed very efficiently and maker friendly.  Standard form is a very good start for different purpose designs. It may be adapted for various potential tasks. There are still many challenges hidden at SCUTTLE Robot for curious makers. This project is a very good sample of that. I hope you enjoy while you are building your own.


## Requirements 

If you want to replicate this project on your own, you'll need;
1.	Raspberry Pi Computer,
2. [Scuttle Robot Base Parts](https://github.com/SMDHuman/ScuttleBalancingRobot/blob/main/docs/Item%20Links%2020230606.pdf),
3.	MPU6050
4.	Custom 3D Printed Parts,
5.	Basic Python Knowledge,
6.	Basic understanding of PID Controller (in case of re-tuning PID)

With all of those you can easily remake or iterate on top of it.

# Getting Started

First of all you need the robot itself to install and run the programs. If you have one, then you are lucky! You just need to transform the shape of the robot and attach external MPU6050 sensor and a [3D print part](https://github.com/SMDHuman/ScuttleBalancingRobot/tree/main/3D%20Models) to mount it. You can start this process by looking up my step by step [YouTube](https://youtu.be/XI1HBQYeNek) guide with English subtitle or check out the [PDF](https://github.com/SMDHuman/ScuttleBalancingRobot/blob/main/docs/Self%20Balanced%20Robot%20Transformation.pdf) of the transformation of the robot from base model to self-balancing configuration.

If you don't have the robot, then you can obtain all the parts from [Scuttle Shop](https://www.scuttlerobot.org/shop/) or from your local shops. You can look the parts and specification of those parts from this [PDF](https://github.com/SMDHuman/ScuttleBalancingRobot/blob/main/docs/Item%20Links%2020230606.pdf) or in that [Link](https://www.scuttlerobot.org/resources/). You will find lots of documentation about SCUTTLE Robot in this link too.

## Wiring of Necessary Components

You have to wire all electrical components to each other that are in use of our project. We need to wire
*	Batteries to Regulator,
*	Batteries to Motor driver,
*	Regulator to Raspberry Pi,
*	Raspberry Pi to Motor Drivers,
*	Motor Driver to DC Motors,
*	MPU6050 to Raspberry Pi.

You can check out the connections of all parts and more from this Link except MPU6050. MPU6050 needs to connect to Raspberry Pi as the picture shows under below.

<img src="https://github.com/SMDHuman/ScuttleBalancingRobot/blob/main/images/Raspbery%20Pi%20to%20MPU6050.jpeg"  width="300">

If you can't see the picture, here is a table of the wiring of the pins between MPU6050 and Raspberry Pi.

| MPU6050 | Raspberry Pi |
|---------|--------------|
| VCC     | 3.3V         |
| GND     | GND          |
| SCL     | GPIO 3       |
| SDA     | GPIO 2       |

## Instillation 
WIP...
