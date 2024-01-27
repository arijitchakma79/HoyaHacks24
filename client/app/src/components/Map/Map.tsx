import React from "react";
import { View } from "react-native";
import MapView, { Marker, Polyline } from "react-native-maps";
import Mapstyles from "../../styles/mapstyle";

interface MapComponentProps {
    currentLocation: { latitude: number; longitude: number };
    previousLocations: { latitude: number; longitude: number }[];
}

const MapComponent: React.FC<MapComponentProps> = ({ currentLocation, previousLocations }): JSX.Element => {
  return (
    <View>
      <MapView
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
        <Marker
          coordinate={{
            latitude: 38.906646,
            longitude: -77.07483766666,
          }}
          title="Robot"
          description="Marker Description"
        />
        <Polyline coordinates={previousLocations} strokeWidth={5} strokeColor="red" />
      </MapView>
    </View>
  );
};

export default MapComponent;
