import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { MapComponent } from './components';
import { Appstyles } from './styles';
import NotificationComponent from './components/notification';
import getLocation from './services/location';
import axios from 'axios';



interface RobotLocation {
  latitude: number;
  longitude: number;
}

const App: React.FC = (): JSX.Element => {
  const [currentLocation, setCurrentLocation] = useState({ latitude: 38.906646, longitude: -77.07483766666 });
  const [previousLocations, setPreviousLocations] = useState<Array<{ latitude: number; longitude: number }>>([]);
  const [notificationData, setNotificationData] = useState([]);

  useEffect(() => {
    // Fetch notification data using Axios
    const fetchNotificationData = async () => {
      try {
        const response = await axios.get('http://161.35.251.92/robot-get-all-reports');
        setNotificationData(response.data.report);
      } catch (error) {
        console.error('Error fetching notification data:', error);
      }
    };

    // Fetch location data every 5 seconds
    const intervalID = setInterval(async () => {
      try {
        // Assuming getLocation returns an object with latitude and longitude properties
        const newLocation = await getLocation();

        setPreviousLocations((prevLocations) => [...prevLocations, currentLocation]);
        setCurrentLocation({
          latitude: newLocation.latitude,
          longitude: newLocation.longitude,
        });

        // Fetch notification data after updating location
        fetchNotificationData();
      } catch (error) {
        console.error('Error fetching location:', error);
      }
    }, 5000);

    // Initial fetch of notification data
    fetchNotificationData();

    return () => clearInterval(intervalID);
  }, [currentLocation]);

  return (
    <View style={Appstyles.container}>
      <View style={Appstyles.mapContainer}>
        <MapComponent currentLocation={currentLocation} previousLocations={previousLocations} />
      </View>
      <Text style={Appstyles.notificationTitle}>Notifications</Text>
      <View style={Appstyles.notificationContainer}>
        <FlatList
          data={notificationData}
          
          renderItem={({ item }) => <NotificationComponent notification={item} />}
        />
      </View>
    </View>
  );
};

export default App;