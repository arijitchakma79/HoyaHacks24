import { StyleSheet } from "react-native";

const notificationStyles = StyleSheet.create({
  notificationItem: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    padding: 10,
    marginVertical: 5,
    backgroundColor: "#eee",
    borderRadius: 5,
  },
  notificationContent: {
    flex: 1,
  },
  buttonContainer: {
    flexDirection: "row",
  },
  button: {
    marginLeft: 10,
    padding: 10,
    borderRadius: 5,
    borderWidth: 1,
    borderColor: "#333",
  },
});

export default notificationStyles;
