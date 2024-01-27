import React, { useEffect } from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { MapComponent } from './components';
import { Appstyles } from './styles';
import NotificationComponent from './components/notification';
import getLocation from './services/location';

const notificationData = [
  { id: '1', address: '123 Main St', date: '2024-02-01', time: '10:00 AM', description: 'Notification 1' },
  { id: '2', address: '456 Oak St', date: '2024-02-02', time: '2:30 PM', description: 'Notification 2' },
  { id: '3', address: '456 Oak St', date: '2024-02-02', time: '2:30 PM', description: 'Notification 2' },
  { id: '4', address: '456 Oak St', date: '2024-02-02', time: '2:30 PM', description: 'Notification 2' },
  { id: '5', address: '456 Oak St', date: '2024-02-02', time: '2:30 PM', description: 'Notification 2' },
  { id: '6', address: '456 Oak St', date: '2024-02-02', time: '2:30 PM', description: 'Notification 2' },
  { id: '7', address: '456 Oak St', date: '2024-02-02', time: '2:30 PM', description: 'Notification 2' },
];

const generateRandomCoordinates = () => {
  const initialLatitude = 38.906646;
  const initialLongitude = -77.07483766666;

  const randomCoordinates = Array.from({ length: 10 }, () => ({
    latitude: initialLatitude + 0.01,
    longitude: initialLongitude + 0.01,
  }));

  return randomCoordinates;
};

interface RobotLocation {
  latitude: number;
  longitude: number;
}

const App: React.FC = (): JSX.Element => {
  const [currentLocation, setCurrentLocation] = React.useState<RobotLocation>({ latitude: 38.906646, longitude: -77.07483766666 });
  const [previousLocations, setPreviousLocations] = React.useState<RobotLocation[]>([]);

  useEffect(() => {
    const intervalID = setInterval(async () => {
      try {
        // Assuming getLocation returns an object with latitude and longitude properties
        const newLocation = await getLocation();
        
        setPreviousLocations((prevLocations) => [...prevLocations, currentLocation]); 
        setCurrentLocation({
          latitude: newLocation.latitude,
          longitude: newLocation.longitude,
        });
      } catch (error) {
        console.error('Error fetching location:', error);
      }
    }, 5000); 

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
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => <NotificationComponent notification={item} />}
        />
      </View>
    </View>
  );
};


export default App;
