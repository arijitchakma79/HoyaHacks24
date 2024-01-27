import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import { MapComponent } from './components';
import { Appstyles } from './styles';
import NotificationComponent from './components/notification';

const App = (): JSX.Element => {
  const notificationData = [
    { id: '1', address: '123 Main St', date: '2024-02-01', time: '10:00 AM', description: 'Notification 1' },
    { id: '2', address: '456 Oak St', date: '2024-02-02', time: '2:30 PM', description: 'Notification 2' },
    { id: '3', address: '456 Oak St', date: '2024-02-02', time: '2:30 PM', description: 'Notification 2' },
    { id: '4', address: '456 Oak St', date: '2024-02-02', time: '2:30 PM', description: 'Notification 2' },
    { id: '5', address: '456 Oak St', date: '2024-02-02', time: '2:30 PM', description: 'Notification 2' },
    { id: '6', address: '456 Oak St', date: '2024-02-02', time: '2:30 PM', description: 'Notification 2' },
    { id: '7', address: '456 Oak St', date: '2024-02-02', time: '2:30 PM', description: 'Notification 2' },
    // Add more data as needed
  ];

  return (
    <View style={styles.container}>
      <View style={Appstyles.mapContainer}>
        <MapComponent />
      </View>
      <Text style={Appstyles.notificationTitle}>Notifications</Text>
      <View style={styles.notificationContainer}>
        <FlatList
          data={notificationData}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => <NotificationComponent notification={item} />}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  notificationContainer: {
    flex: 1,
    paddingHorizontal: 20, // Add padding to the sides
  },
});

export default App;
