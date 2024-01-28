import sendSms from "./sendSms";

export const handleTickPress = (id) => {
    console.log(`Notification ${id} has been accepted`);
   
    
}

export const handleCrossPress = (id) => {
    console.log(`Notification ${id} has been rejected`);
}
