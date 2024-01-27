import { StyleSheet, Dimensions } from "react-native";

const screenHeight = Dimensions.get("screen").height;

const Mapstyles = StyleSheet.create({
    map: {
      width: '100%',
      height: '100%' , 
    },
  });

export default Mapstyles;