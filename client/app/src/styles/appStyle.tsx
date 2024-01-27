import { StyleSheet } from "react-native";

const Appstyles = StyleSheet.create({
  mapContainer: {
    height: '60%',
    width: '100%',
  },
  notificationTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: "#384B5A",
    marginTop: 20,
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
  },
  container: {
    flex: 1,
  },
  notificationContainer: {
    flex: 1,
    paddingHorizontal: 20,
  },
});

export default Appstyles;