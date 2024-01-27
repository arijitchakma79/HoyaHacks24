import React from "react";
import { View,Text } from "react-native";
import MapView, {Marker} from "react-native-maps";
import Mapstyles from "../../styles/mapstyle";

const MapComponent = ():JSX.Element => {
    return(
        <View >
            <MapView style={Mapstyles.map}
            initialRegion={{
                latitude: 38.906646,
                longitude: -77.07483766666,
                latitudeDelta: 0.0922,
                longitudeDelta: 0.0421,
            
            }}>
                <Marker
                    coordinate={{
                         latitude: 38.906646,
                        longitude: -77.07483766666 
                    }}
                    title="Marker Title"
                    description="Marker Description"
                />
            </MapView>
        </View>
    )
}

export default MapComponent;