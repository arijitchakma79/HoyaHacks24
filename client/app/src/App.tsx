import React from 'react';
import {View, Text, StyleSheet} from 'react-native';
import { MapComponent } from './components';
import { Appstyles } from './styles';

const App = ():JSX.Element => {
  return (
    <View >
      <View style={Appstyles.mapContainer}>
        <MapComponent />
      </View>
      <Text>Notifications</Text>
    </View>
  )
};



export default App;