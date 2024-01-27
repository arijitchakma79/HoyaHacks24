import axios from 'axios';


const getLocation = async() => {
    try{
        const response = await axios.get('http://161.35.251.92/robot-get-location');
        return response.data;
    }
    catch(error){
        console.error('Axios Error:', error);
        throw error;
    }
}


export default getLocation;