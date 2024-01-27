import React from 'react';
import {View, Text, StyleSheet} from 'react-native';
import MapView,{Marker} from 'react-native-maps';

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  map: {
    flex: 1,
  },
});

const App = ():JSX.Element => {
  return (
    <View style={styles.container}>
    <MapView
      style={styles.map}
      initialRegion={{
        latitude: 38.906646,
        longitude: -77.07483766666,
        latitudeDelta: 0.0922,
        longitudeDelta: 0.0421,
      }}
    >
      <Marker
        coordinate={{ latitude: 37.78825, longitude: -122.4324 }}
        title="Marker Title"
        description="Marker Description"
      />
    </MapView>
  </View>
  )
};

export default App;