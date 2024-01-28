/*import twilio from 'twilio';

const accountSid = 'ACfba00d58fc89a8aff6edf5b71527e2f5';
const authToken = '0882124ec426b5702170ff4a0d22c9ca';
const client = twilio(accountSid, authToken);

const sendSms = async (to, body) => {
    const TWILIO_PHONE_NUMBER = '+18885788168';

    try {
        const message = await client.messages.create({
            body: body,
            from: TWILIO_PHONE_NUMBER,
            to: to,
        });

        console.log('SMS sent successfully', message.sid);
        return message.sid; // Optionally return Twilio message SID
    } catch (error) {
        console.error('Error sending SMS:', error);
        throw error; // Propagate the error
    }
};

export default sendSms;
*/