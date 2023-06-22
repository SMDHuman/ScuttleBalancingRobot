	# Scuttle Self-Balance robot
This project of mine was made with the support of [SCUTTLE™](https://www.scuttlerobot.org/). 

## About The Project
This project's subject is to make Scuttle robot balance it self on it's two wheels only editing it's default shape and use external IMU sensor. Main idea of this project comes from David Malawey who's Founder of Scuttle™ and I am the person who's made this idea come true. Before this project i have one project similar to this and it's called [LOTP_BalanceWheel](https://github.com/SMDHuman/BalanceWheel) and it's purpose is to make 3D Printed, small, stepper motor driven and Raspberry Pi Pico based two wheel self balancing robot.

## Requirements 
If you want to replicate this project on your own, you'll need;
1. Raspberry Pi Computer,
2. [Scuttle Robot Base Parts](https://github.com/SMDHuman/ScuttleBalancingRobot/blob/main/docs/Item%20Links%2020230606.pdf),
3. MPU6050,
4. Custom 3D Printed Parts,
5. Basic Python Knowledge,
6. Basic understanding of PID Controller (in case of re-tuning PID)

With all of those you can easily remake or iterate on top of it. 

# Getting Started
First of all you need the robot it self to install and run the programs. If you have one, then you are lucky! You just need to edit the shape of the robot and attach external MPU6050 sensor by 3D Print the mount of it. You can start this process by looking up my step by step [Youtube](https://youtu.be/XI1HBQYeNek) guide with English subtitle or check out the [PDF](https://github.com/SMDHuman/ScuttleBalancingRobot/blob/main/docs/Self%20Balanced%20Robot%20Transformation.pdf) of the transformation of the robot from base model to self-balancing configuration.

If you don't have the robot, then you can obtain all the parts from [Scuttle Shop](https://www.scuttlerobot.org/shop/) or in your local shops. You can look the parts and specification of those parts from this [PDF](https://github.com/SMDHuman/ScuttleBalancingRobot/blob/main/docs/Item%20Links%2020230606.pdf) or in that [Link](https://www.scuttlerobot.org/resources/). You will find lots of documentation about Scuttle robot in this link too.

## Wiring of Necessary Components
You have to wire all electrical components each other that are in use of our project. We need 
* Batteries to Regulator
* Batteries to Motor driver
* Regulator to Raspberry Pi
* Raspberry Pi to Motor Drivers
* Motor Driver to DC Motors
* MPU6050 to Raspberry Pi

You can check out how to connects of all parts and more from this [Link](https://www.scuttlerobot.org/resource/guide/wiring-guide/) except MPU6050. MPU6050 needs to connect to Raspberry Pi as the picture under this text shown.

<img src="https://github.com/SMDHuman/ScuttleBalancingRobot/blob/main/images/Raspbery%20Pi%20to%20MPU6050.jpeg"  width="300">

If you can't see the picture here is a table of the wiring under here.
| MPU6050 | Raspberry Pi |
|---------|--------------|
| VCC     | 3.3V         |
| GND     | GND          |
| SCL     | GPIO 3       |
| SDA     | GPIO 2       |

## Instillation 
WIP...
