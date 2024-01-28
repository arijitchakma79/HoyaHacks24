import axios from "axios";

const serverURL = 'http://161.35.251.92/'; 

const deleteReport = async (id) => {
  try {
    const endpoint = `${serverURL}/delete-report/${id}`;
    const response = await axios.delete(endpoint);

    if (response.status === 200) {
      console.log('Report deleted successfully');
    } else {
      console.error('Error deleting report:', response.data);
    }
  } catch (error) {
    console.error('Error deleting report:', error.message);
  }
};

export default deleteReport;