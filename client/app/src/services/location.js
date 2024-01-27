import axios from "axios";

const fetchRobotLocation = async (setRobotLocation, setPathCoordinates) => {
    try {
        const res = await axios.get("https://161.35.251.92/robot-get-location");
        const data = res.data;

        setRobotLocation({ latitude: data.latitude, longitude: data.longitude });
        setPathCoordinates(prevPathCoordinates => [...prevPathCoordinates, { latitude: data.latitude, longitude: data.longitude }]);
    } catch (err) {
        console.log('Error fetching robot location', err);
    }
}

export default fetchRobotLocation;
