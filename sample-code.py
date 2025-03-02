# perception/sensor_fusion.py
import numpy as np
from typing import Dict, List, Tuple
import time

class SensorFusion:
    """
    Integrates data from multiple sensors (LiDAR, cameras, radar) to create
    a unified representation of the environment around the autonomous bus.
    """
    
    def __init__(self, config: Dict):
        """
        Initialize the sensor fusion module with configuration parameters.
        
        Args:
            config: Dictionary containing configuration parameters
                - sensor_weights: Relative weights for different sensors
                - time_sync_threshold: Maximum allowed time difference between sensor readings
                - confidence_threshold: Minimum confidence level for object detection
        """
        self.config = config
        self.sensor_data = {}
        self.fused_objects = []
        self.last_fusion_timestamp = 0
        
    def register_sensor_data(self, sensor_id: str, data: Dict, timestamp: float) -> None:
        """
        Register new data from a sensor for fusion.
        
        Args:
            sensor_id: Identifier for the sensor
            data: Detected objects and their properties
            timestamp: Time when the data was captured
        """
        self.sensor_data[sensor_id] = {
            'data': data,
            'timestamp': timestamp
        }
        
    def _check_time_synchronization(self) -> bool:
        """
        Check if all sensor data is synchronized within the acceptable threshold.
        
        Returns:
            bool: True if data is properly synchronized
        """
        timestamps = [info['timestamp'] for info in self.sensor_data.values()]
        return max(timestamps) - min(timestamps) < self.config['time_sync_threshold']
        
    def _match_objects(self) -> List[Dict]:
        """
        Match objects detected by different sensors based on spatial proximity.
        
        Returns:
            List of matched objects with confidence scores
        """
        matched_objects = []
        # Implementation of object matching algorithm would go here
        # This is a complex algorithm involving spatial and temporal alignment
        return matched_objects
        
    def _calculate_fusion_confidence(self, matched_object: Dict) -> float:
        """
        Calculate confidence score for a fused object based on sensor reliability.
        
        Args:
            matched_object: Object with detections from multiple sensors
            
        Returns:
            float: Confidence score between 0 and 1
        """
        # Weight the confidence based on sensor reliability and consistency
        sensor_weights = self.config['sensor_weights']
        confidence = 0.0
        
        for detection in matched_object['detections']:
            sensor_type = detection['sensor_type']
            detection_conf = detection['confidence']
            confidence += sensor_weights[sensor_type] * detection_conf
            
        return min(confidence, 1.0)
    
    def perform_fusion(self) -> List[Dict]:
        """
        Fuse the registered sensor data to create a unified world model.
        
        Returns:
            List of fused objects with positions, velocities, and classifications
        """
        current_time = time.time()
        
        # Check if we have data from all required sensors
        required_sensors = {'lidar', 'camera', 'radar'}
        if not required_sensors.issubset(self.sensor_data.keys()):
            raise ValueError(f"Missing data from required sensors. Have: {self.sensor_data.keys()}")
            
        # Check time synchronization
        if not self._check_time_synchronization():
            raise ValueError("Sensor data is not properly time-synchronized")
            
        # Match objects across different sensors
        matched_objects = self._match_objects()
        
        # Calculate final properties and confidence for each fused object
        self.fused_objects = []
        for obj in matched_objects:
            confidence = self._calculate_fusion_confidence(obj)
            
            if confidence >= self.config['confidence_threshold']:
                fused_obj = {
                    'id': obj['id'],
                    'position': obj['position'],
                    'velocity': obj['velocity'],
                    'dimensions': obj['dimensions'],
                    'classification': obj['classification'],
                    'confidence': confidence,
                    'first_detected': obj['first_detected'],
                    'last_updated': current_time
                }
                self.fused_objects.append(fused_obj)
        
        self.last_fusion_timestamp = current_time
        return self.fused_objects
    
    def get_object_by_id(self, object_id: str) -> Dict:
        """
        Retrieve a specific object by its ID from the fused objects.
        
        Args:
            object_id: Unique identifier for the object
            
        Returns:
            Dict containing the object properties or None if not found
        """
        for obj in self.fused_objects:
            if obj['id'] == object_id:
                return obj
        return None
    
    def get_nearest_objects(self, max_distance: float, object_type: str = None) -> List[Dict]:
        """
        Get objects within a specified distance, optionally filtered by type.
        
        Args:
            max_distance: Maximum distance in meters
            object_type: Optional filter for object type (vehicle, pedestrian, etc.)
            
        Returns:
            List of objects sorted by distance
        """
        nearby_objects = []
        
        for obj in self.fused_objects:
            # Calculate distance from ego vehicle (assumed to be at origin)
            position = np.array(obj['position'])
            distance = np.linalg.norm(position)
            
            if distance <= max_distance and (object_type is None or obj['classification'] == object_type):
                obj_copy = obj.copy()
                obj_copy['distance'] = distance
                nearby_objects.append(obj_copy)
                
        # Sort by distance
        return sorted(nearby_objects, key=lambda x: x['distance'])


# Example usage:
if __name__ == "__main__":
    # Configuration for sensor fusion
    fusion_config = {
        'sensor_weights': {
            'lidar': 0.6,
            'camera': 0.3,
            'radar': 0.1
        },
        'time_sync_threshold': 0.1,  # 100ms
        'confidence_threshold': 0.75
    }
    
    # Initialize sensor fusion
    fusion = SensorFusion(fusion_config)
    
    # Example sensor data (in practice, this would come from actual sensors)
    lidar_data = {
        'objects': [
            {
                'id': 'obj_1',
                'position': [10.5, 1.2, 0.0],
                'dimensions': [4.5, 1.8, 1.5],
                'confidence': 0.95
            }
        ]
    }
    
    camera_data = {
        'objects': [
            {
                'id': 'obj_1',
                'position': [10.7, 1.3, 0.0],
                'classification': 'vehicle',
                'confidence': 0.9
            }
        ]
    }
    
    radar_data = {
        'objects': [
            {
                'id': 'obj_1',
                'position': [10.6, 1.25, 0.0],
                'velocity': [5.0, 0.0, 0.0],
                'confidence': 0.85
            }
        ]
    }
    
    # Register sensor data
    current_time = time.time()
    fusion.register_sensor_data('lidar', lidar_data, current_time - 0.01)
    fusion.register_sensor_data('camera', camera_data, current_time - 0.02)
    fusion.register_sensor_data('radar', radar_data, current_time - 0.03)
    
    # Perform fusion
    try:
        fused_objects = fusion.perform_fusion()
        print(f"Successfully fused {len(fused_objects)} objects")
        for obj in fused_objects:
            print(f"Object ID: {obj['id']}")
            print(f"Position: {obj['position']}")
            print(f"Classification: {obj['classification']}")
            print(f"Confidence: {obj['confidence']:.2f}")
    except ValueError as e:
        print(f"Fusion failed: {e}")
