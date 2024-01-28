import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import Geocoding from 'react-native-geocoding';
import { notificationStyles } from '../styles';
import { handleTickPress, handleCrossPress } from '../services/handleNB';

Geocoding.init('AIzaSyDYlE5EHSkVSUw0KbMqbjws0-XEAtV0FMU');

interface Notifications {
  _id: string;
  latitude: number;
  longitude: number;
  reportTime: string;
  reportDate: string;
  description: string;
}

interface NotificationsComponentProps {
  notification: Notifications;
}

const NotificationComponent: React.FC<NotificationsComponentProps> = ({ notification }) => {
  const [address, setAddress] = useState<string>('');

  useEffect(() => {
   
    Geocoding.from(notification.latitude, notification.longitude)
      .then((json) => {

        
        const extractedAddress = json.results[0]?.formatted_address || 'Address not available';
        setAddress(extractedAddress);
      })
      .catch((error) => console.error('Error fetching address:', error));
  }, [notification.latitude, notification.longitude]);


  return (
    <View style={notificationStyles.notificationItem}>
      <View style={notificationStyles.notificationContent}>
        <Text>{`Date: ${notification.reportDate}`}</Text>
        <Text>{`Time: ${notification.reportTime}`}</Text>
        <Text>{`Address: ${address}`}</Text>
      </View>
      <View style={notificationStyles.buttonContainer}>
        <TouchableOpacity style={notificationStyles.button} onPress={() => handleTickPress(notification._id)}>
          <Text>✓</Text>
        </TouchableOpacity>
          <TouchableOpacity style={notificationStyles.button} onPress={() => handleCrossPress(notification._id)}>
          <Text>✗</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default NotificationComponent;
