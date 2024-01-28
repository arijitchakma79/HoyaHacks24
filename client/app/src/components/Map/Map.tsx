import React, { useEffect, useRef } from "react";
import { View, Animated, Image } from "react-native";
import MapView, { Marker, Polyline } from "react-native-maps";
import Mapstyles from "../../styles/mapstyle";

interface MapComponentProps {
  currentLocation: { latitude: number; longitude: number };
  previousLocations: { latitude: number; longitude: number }[];
}

const MapComponent: React.FC<MapComponentProps> = ({
  currentLocation,
  previousLocations,
}): JSX.Element => {
  const mapViewRef = useRef<MapView>(null);

  useEffect(() => {
    // Move the map to the current location when it changes
    if (mapViewRef.current) {
      mapViewRef.current.animateToRegion({
        latitude: currentLocation.latitude,
        longitude: currentLocation.longitude,
        latitudeDelta: 0.005,
        longitudeDelta: 0.005,
      });
    }
  }, [currentLocation]);

  return (
    <View>
      <MapView.Animated
        ref={mapViewRef}
        style={Mapstyles.map}
        mapType="satellite"
        zoomTapEnabled={false}
        initialRegion={{
          latitude: currentLocation.latitude,
          longitude: currentLocation.longitude,
          latitudeDelta: 0.005,
          longitudeDelta: 0.005,
        }}
      >
        {/* Use Marker.Animated for smooth animation */}
        <Marker.Animated
        
          coordinate={{
            latitude: currentLocation.latitude,
            longitude: currentLocation.longitude,
          }}
          
          title="Robot"
          description="Marker Description"
         >
           <Image source={require('../../assets/robot.png')} style={{ width: 40, height: 40 }} />
         </Marker.Animated>
        
        
        <Polyline coordinates={previousLocations} strokeWidth={5} strokeColor="red" />
      </MapView.Animated>
    </View>
  );
};

export default MapComponent;
