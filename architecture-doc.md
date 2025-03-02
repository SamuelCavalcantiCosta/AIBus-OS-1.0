# AIBus-OS System Architecture

## Overview

The AIBus-OS system follows a modular architecture designed for safety, reliability, and extensibility. The system is divided into six main subsystems that work together to enable autonomous operation of public transit buses.

## System Diagram

```
                      ┌─────────────────┐
                      │                 │
                      │    Perception   │
                      │                 │
                      └────────┬────────┘
                               │
                               ▼
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│                 │   │                 │   │                 │
│ Infrastructure  │◄──│    Decision     │──►│     Safety      │
│                 │   │                 │   │                 │
└────────┬────────┘   └────────┬────────┘   └────────┬────────┘
         │                     │                     │
         │            ┌────────▼────────┐            │
         │            │                 │            │
         └───────────►│     Control     │◄───────────┘
                      │                 │
                      └─────────────────┘
```

## Subsystem Descriptions

### 1. Perception

The perception subsystem serves as the "eyes and ears" of the autonomous bus, collecting and processing data from the environment.

**Key Components:**
- **LiDAR Processing**: 3D point cloud processing for precise distance measurements and object detection
- **Camera Vision**: Object detection, classification, and tracking using deep learning models
- **Radar Processing**: Velocity measurement and object detection in adverse weather conditions
- **Sensor Fusion**: Integration of data from multiple sensors for a unified world model
- **Localization**: High-precision positioning using GPS, IMU, and map matching

**Interfaces:**
- Outputs detected objects, road features, and localization data to the Decision subsystem
- Receives calibration and configuration updates from the Safety subsystem

### 2. Decision

The decision subsystem determines the optimal behavior of the bus based on perception data and mission goals.

**Key Components:**
- **Route Planning**: Long-term planning to follow designated bus routes
- **Behavior Planning**: Selection of appropriate behaviors in traffic situations
- **Path Planning**: Generation of feasible, comfortable, and safe trajectories
- **Traffic Prediction**: Anticipation of other road users' future movements
- **Mission Manager**: Management of high-level goals like passenger pickup/dropoff

**Interfaces:**
- Receives perception data from the Perception subsystem
- Outputs trajectory commands to the Control subsystem
- Communicates with Infrastructure for route information and traffic updates
- Receives safety constraints from the Safety subsystem

### 3. Control

The control subsystem executes the planned trajectories by controlling the physical bus systems.

**Key Components:**
- **Longitudinal Control**: Acceleration and braking systems management
- **Lateral Control**: Steering system management
- **Vehicle Dynamics**: Models for accurate prediction of vehicle response
- **Execution Monitoring**: Verification that commands are properly executed

**Interfaces:**
- Receives trajectory commands from the Decision subsystem
- Outputs control signals to the bus drive-by-wire system
- Provides feedback to the Safety subsystem
- Receives override commands from the Safety subsystem when necessary

### 4. Infrastructure

The infrastructure subsystem manages communication with external systems and provides supporting services.

**Key Components:**
- **V2X Communication**: Vehicle-to-everything protocols for interacting with smart city infrastructure
- **Fleet Management**: Coordination with central dispatch and other buses
- **Passenger Interface**: Management of passenger information systems
- **Software Updates**: Secure over-the-air update mechanisms
- **Data Logging**: Collection of operational data for analysis and improvement

**Interfaces:**
- Communicates with external traffic management systems
- Exchanges information with the Decision subsystem
- Provides system health data to the Safety subsystem
- Manages external communication channels

### 5. Safety

The safety subsystem ensures the overall safety of the autonomous bus operation.

**Key Components:**
- **System Monitor**: Continuous monitoring of all subsystem functions
- **Fault Detection**: Identification of component failures or degradation
- **Redundancy Management**: Coordination of redundant systems
- **Emergency Protocols**: Execution of safe fallback behaviors
- **Safety Case Validator**: Runtime verification that operations meet safety requirements

**Interfaces:**
- Monitors all subsystems for failures or anomalies
- Can override any subsystem in case of safety concerns
- Maintains independent sensing and actuation capabilities for emergency situations
- Communicates with infrastructure for emergency reporting

### 6. Simulation

The simulation subsystem enables testing and validation in virtual environments.

**Key Components:**
- **Environment Simulator**: Physics-based simulation of road environments
- **Sensor Models**: Realistic simulation of sensor behavior
- **Traffic Simulation**: Models of other road users with realistic behaviors
- **Scenario Generation**: Creation of diverse test scenarios
- **Performance Analysis**: Automatic evaluation of system behavior

**Interfaces:**
- Can replace real-world inputs to all subsystems for testing
- Records and analyzes system performance in simulated scenarios
- Facilitates training of machine learning components

## Cross-Cutting Concerns

**Security**:
- Secure communications using TLS/DTLS
- Access control for system components
- Intrusion detection systems
- Regular security assessments

**Real-Time Performance**:
- Deterministic processing guarantees
- Worst-case execution time analysis
- Resource monitoring and management

**Validation & Verification**:
- Formal methods for critical components
- Extensive test coverage
- Runtime monitoring
- Regular validation against safety requirements

## Hardware Architecture

The AIBus-OS software is designed to run on a redundant hardware platform with the following components:

- 2× High-performance computing units (main and backup)
- 3× LiDAR sensors (front, left, right)
- 8× Cameras (providing 360° coverage)
- 5× Radar units (front, corners, rear)
- High-precision GNSS with RTK
- Redundant CAN bus networks
- Hardware watchdogs and safety controllers
- Redundant power supply systems

## Deployment Model

The system uses a containerized deployment model based on Docker, allowing:

- Isolated component execution
- Simplified updates and rollbacks
- Resource allocation and prioritization
- Consistent development and production environments

Each subsystem is deployed in dedicated containers with appropriate resource allocations and security policies.

## Extensibility

The AIBus-OS architecture is designed to be extensible in several ways:

1. **Plugin System**: Each subsystem supports plugins for specific implementations
2. **Configuration-Driven**: Behavior can be modified through configuration without code changes
3. **Service-Oriented**: Well-defined interfaces allow component replacement
4. **Open Data Formats**: Standard formats ensure compatibility with third-party tools

## Conclusion

The AIBus-OS system architecture provides a comprehensive framework for developing autonomous bus systems with a focus on safety, reliability, and openness. By following modular design principles and well-defined interfaces, the architecture supports collaborative development and continuous improvement.