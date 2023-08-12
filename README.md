# 0x00. AirBnB clone - The console

## AirBnB Command Interpreter

This is the first step towards building the AirBnB clone web application. The command interpreter allows you to manage the objects of the project, such as creating new objects, retrieving objects from files or databases, performing operations on objects, updating object attributes, and destroying objects.

## Features

- Parent class (BaseModel) for initialization, serialization, and deserialization of instances
- Flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- Classes for AirBnB objects (User, State, City, Place, etc.) that inherit from BaseModel
- File storage engine for storing objects
- Unit tests to validate classes and storage engine

## Usage

The command interpreter provides the following commands:

- `create`: Create a new object
- `retrieve`: Retrieve an object from a file or database
- `operations`: Perform operations on objects (e.g., count, compute stats)
- `update`: Update attributes of an object
- `destroy`: Destroy an object

## Getting Started
This project is created and tested on Ubuntu 20.04 LTS
1. Clone the repository.
2. Run the command interpreter script. `./console.py`
3. Use the available commands to manage the objects.

---
LAST UPDATED: 12 AUG 2023