import axios from 'axios';

const testAxios = async () => {
  try {
    const response = await axios.get('https://jsonplaceholder.typicode.com/todos/1');
    console.log('Axios Response:', response.data);
  } catch (error) {
    console.error('Axios Error:', error);
  }
};

export default testAxios;