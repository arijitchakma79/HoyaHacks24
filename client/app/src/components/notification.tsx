import React from "react";
import {View, Text, StyleSheet} from "react-native";
import { notificationBoxStyles } from "../styles";
interface Notifications {
    id:string,
    address: string,
    date: string,
    time: string,
    description: string,
}

interface NotificationsComponentProps {
    notification: Notifications;
}


const NotificationComponent: React.FC<NotificationsComponentProps> = ({ notification }) => {
    return (
        <View style={notificationBoxStyles.notificationItem}>
            <Text>{`Address: ${notification.address}`}</Text>
            <Text>{`Date: ${notification.date}`}</Text>
            <Text>{`Time: ${notification.time}`}</Text>
            <Text>{`Description: ${notification.description}`}</Text>
        </View>
    )
}

export default NotificationComponent;